from fastapi import FastAPI, File, UploadFile, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import os
import xml.etree.ElementTree as ET
import re
from transformers import BartForConditionalGeneration, BartTokenizer
from sentence_transformers import SentenceTransformer, util

app = FastAPI()

# Define the template directory
templates = Jinja2Templates(directory=os.getcwd())

# Define model and tokenizer
model_name = 'facebook/bart-large-cnn'
model = BartForConditionalGeneration.from_pretrained(model_name)
tokenizer = BartTokenizer.from_pretrained(model_name)

# List of legal categories
categories = ['Criminal Law','Civil Law','Family Law','Administrative Law','Labor Law','Environmental Law','Tax Law','Intellectual Property Law','Commercial Law','International Law','Real Estate Law','Health Law','Bankruptcy Law','Elder Law','Immigration Law']

# Function to extract text from XML
def extract_text_from_xml(xml_content):
    root = ET.fromstring(xml_content)
    text_content = []
    for i in ['name', 'sentence', 'catchphrase', 'text', 'citphrase']:
        for elem in root.iter(i):
            if elem.text:
                text_content.append(elem.text.strip())
    return ' '.join(text_content)

# Function to clean text
def clean_text(text):
    cleaned_text = re.sub(r'\s+', ' ', text)  # Remove extra whitespaces
    cleaned_text = cleaned_text.strip()
    return cleaned_text

# Function to summarize text
def summarize_text(text):
    prompt = f"Analyze the following text for key insights and central themes. :\n\n{text}"
    inputs = tokenizer(prompt, max_length=1024, return_tensors='pt', truncation=True)

    # For summarization using --- facebook/bart-large-cnn model
    summary_ids = model.generate(inputs['input_ids'], max_length=350, min_length=200, length_penalty=2.0, num_beams=4, early_stopping=True, temperature=1)
    summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
    return summary

# Function to classify text into legal categories
def classify_text(text, categories):
    model = SentenceTransformer('all-MiniLM-L6-v2')
    text_embedding = model.encode(text, convert_to_tensor=True)
    category_embeddings = model.encode(categories, convert_to_tensor=True)
    similarities = util.pytorch_cos_sim(text_embedding, category_embeddings)
    most_similar_index = similarities.argmax().item()
    return categories[most_similar_index]

@app.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/uploadfile/")
async def process_xml(file: UploadFile = File(...)):
    # Process the uploaded file here
    return {"filename": file.filename, "content_type": file.content_type}

@app.post("/process_xml/")
async def process_xml(file: UploadFile):
    # Check if file is XML
    if not file.filename.endswith(".xml"):
        raise HTTPException(status_code=400, detail="Only XML files are allowed")
    
    # Read XML content
    xml_content = await file.read()

    xml_content = xml_content.decode('utf-8')
    
    # Replacing the content
    modified_xml_content = xml_content.replace('"id=', 'id="').replace('type=cited', 'type="cited"').replace('type=citing', 'type="citing"')

    # Extract text from XML
    full_text = extract_text_from_xml(modified_xml_content)

    # Clean text
    cleaned_text = clean_text(full_text)

    # Summarize text
    summary = summarize_text(cleaned_text)

    # Classify text
    category = classify_text(cleaned_text, categories)

    return {"Summary": summary, "Legal_Category": category}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)
