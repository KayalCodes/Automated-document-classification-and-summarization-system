# Automated Document Classification And Summarization System
This project involves building a web application that allows users to upload XML documents and receive a summarized version of the document along with its classification into a predefined legal category. The application leverages advanced NLP models from the transformers library and the sentence-transformers library to perform these tasks. The project is built using FastAPI for the backend, providing an efficient and scalable way to handle HTTP requests.

### Key Components:
- **FastAPI:** *A modern, fast (high-performance) web framework for building APIs with Python.*
- **Transformers:** *Library by Hugging Face for state-of-the-art NLP models, used here for text summarization.*
- **Sentence-Transformers:** *Library for easy-to-use sentence embeddings, used here for text classification.*
- **HTML and JavaScript:** *For the frontend, allowing users to upload files and view results.*

### Functionality:
- **File Upload:** *Users can upload XML files through the web interface.*
- **Text Extraction:** *The application extracts relevant text from the XML structure.*
- **Text Cleaning:** *The extracted text is cleaned to remove unnecessary whitespace and characters.*
- **Text Summarization:** *Using the BART model from the transformers library, the application generates a summary of the cleaned text.*
- **Text Classification:** *Using sentence embeddings, the application classifies the text into one of several predefined legal categories.*
- **Result Display:** *The summarized text and its legal category are displayed to the user.*

### Detailed Components:
**Backend (main.py):**
- **Import Libraries:** *Imported necessary libraries including FastAPI, transformers, sentence-transformers, and others.*
- **Model Initialization:** *Initialized the BART model and tokenizer for summarization and SentenceTransformer for classification.*
- **Text Extraction Function:** *Function to parse XML content and extract relevant text.*
- **Text Cleaning Function:** *Function to clean the extracted text.*
- **Summarization Function:** *Function to summarize the cleaned text using the BART model.*
- **Classification Function:** *Function to classify the text into a legal category using sentence embeddings.*
  
**Routes:**
- **GET /:** *Serve the frontend HTML file.*
- **POST /process_xml/:** *Handle file uploads, perform text extraction, cleaning, summarization, and classification, then return the results as JSON.*
  
**Frontend (index.html):**
- **HTML Structure:** *Provide a form for file upload and buttons to trigger the analysis.*
- **JavaScript:** *Handle file uploads via JavaScript, send the file to the backend, and display the results returned by the backend.*
- **Styling:** *Use Bootstrap and custom CSS for styling the form and results display.*

## To clone the directory and set up the project, follow these steps:

1. Prerequisites
   - Ensure you have git installed on your machine.
   - Ensure you have Python (version: 3.10.0) installed.
   - Ensure you have pip (version: 24.1) installed.
2. Cloning the Repository and run the application
   - Open a terminal or command prompt on your machine.
   - Navigate to the directory where you want to clone the project repository and follow the below commands.
   - Clone the repository
     
     ```
     git clone https://github.com/KayalCodes/Automated-document-classification-and-summarization-system.git
     ```
     
   - Navigate to the project directory
     
     ```
     cd Automated-document-classification-and-summarization-system-main/Automated-document-classification-and-summarization-system-main
     ```
     
   - Create a virtual environment
     
     ```
     python -m venv myenv
     ```
     
   - Activate the virtual environment
     
     ```
      # On Windows
      .\myenv\Scripts\activate
     
      # On macOS/Linux
      source myenv/bin/activate
     ```
     
   - Install the required dependencies
     
     ```
     pip install -r requirements.txt
     ```
     
   - Run the FastAPI server
     
     ```
     uvicorn main:app --reload
     ```
     
    
 <!-- ```
  # Navigate to the desired directory
  cd path/to/your/directory

  # Clone the repository
  git clone https://github.com/KayalCodes/Automated-document-classification-and-summarization-system.git

  # Navigate to the project directory
  cd Automated-document-classification-and-summarization-system-main/Automated-document-classification-and-summarization-system-main

  # Create a virtual environment
  python -m venv myenv

  # Activate the virtual environment
  # On Windows
  .\myenv\Scripts\activate
  # On macOS/Linux
  source myenv/bin/activate

  # Install the required dependencies
  pip install -r requirements.txt

  # Run the FastAPI server
  uvicorn main:app --reload

  # after running the application, open web browser and go to the below link
  http://localhost:8000/
  ```
  -->
  
## Flow of the system after running the application

**Application Front-End**

![image](https://github.com/KayalCodes/Automated-document-classification-and-summarization-system/assets/35140705/dff0ef4f-13b2-4b41-a114-8e8d128449d2)

**Flow of the System:**
1. User visits the web page http://localhost:8000/
2. Uploads an XML file via the provided form  (or use the ***example.xml*** file in the repo)
   - Visit this link [Legal Case Reports Dataset](https://archive.ics.uci.edu/dataset/239/legal+case+reports)
   - Download the dataset
   - Extract all the files
   - Upload any XML file from the path (legal+case+reports/corpus/fulltext) 
3. Clicks the ***Analyze Document*** button.
4. Backend Processing starts
   - The uploaded file is sent to the /process_xml/ endpoint.
   - The backend reads and processes the file: extracts, cleans, summarizes, and classifies the text.
   - Results are returned to the frontend as JSON.
   - Summary and the legal category of the uploaded case will be displayed in the Result section.
