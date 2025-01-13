import logging
import os
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from langchain_community.vectorstores import FAISS 
from langchain_openai.embeddings import AzureOpenAIEmbeddings  
from langchain_openai import AzureChatOpenAI 
from langchain.schema import Document 
from langchain.text_splitter import RecursiveCharacterTextSplitter
from bs4 import BeautifulSoup

# Configure logging
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

# Azure OpenAI Configuration
os.environ["AZURE_OPENAI_API_KEY"] = "AZURE_OPENAI_API_KEY"
os.environ["AZURE_OPENAI_ENDPOINT"] = "AZURE_OPENAI_ENDPOINT"
os.environ["AZURE_OPENAI_API_VERSION"] = "2024-08-01-preview"
os.environ["AZURE_OPENAI_CHAT_DEPLOYMENT_NAME"] = "gstgpt35t"

# Initialize embeddings with chunk_size specified
embeddings = AzureOpenAIEmbeddings(
    azure_deployment="gsttextemb002",
    openai_api_version="2024-08-01-preview",
    azure_endpoint=os.environ["AZURE_OPENAI_ENDPOINT"],
    api_key=os.environ["AZURE_OPENAI_API_KEY"],  # Use environment variable for the API key
    chunk_size=1024  # Specify chunk_size to avoid KeyError
)

# Function to load and preprocess documentation HTML files
def load_and_process_docs(doc_folder):
    docs = []
    for filename in os.listdir(doc_folder):
        if filename.endswith(".html"):
            file_path = os.path.join(doc_folder, filename)
            with open(file_path, "r", encoding="utf-8") as file:
                content = file.read()
                soup = BeautifulSoup(content, "html.parser")
                # Extract text from the HTML, ignore scripts, styles, etc.
                text = soup.get_text(separator="\n", strip=True)
                docs.append(text)
    return docs

# Load and preprocess documentation from the db folder
doc_folder = "C:/Users/SIVABALAJI S/Desktop/zeotap chat/db"
docs = load_and_process_docs(doc_folder)

# Convert text documents to Document objects
documents = [Document(page_content=doc) for doc in docs]

# Split the documents into smaller chunks
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1024, chunk_overlap=128)
split_docs = text_splitter.split_documents(documents)

# Load the vector store using the embeddings
vectorstore = FAISS.from_documents(split_docs, embeddings)

# Initialize LLM for Chat
llm = AzureChatOpenAI(
    azure_deployment="gstgpt35t",
    openai_api_version="2024-08-01-preview",
    azure_endpoint=os.environ["AZURE_OPENAI_ENDPOINT"],
    api_key=os.environ["AZURE_OPENAI_API_KEY"]
)

# FastAPI app
app = FastAPI()

class Query(BaseModel):
    question: str

@app.post("/ask")
async def ask_question(query: Query):
    question = query.question
    results = []

    # Perform similarity search using the vectorstore
    docs = vectorstore.similarity_search(question, k=1)  
    if docs:
        results.append({"cdp": "Documentation", "content": docs[0].page_content})

    if not results:
        raise HTTPException(status_code=404, detail="No relevant information found.")

    
    prompt = f"User question: {question}\n"
    for result in results:
        prompt += f"\nDocumentation: {result['content']}\n"

    
    try:
        response = llm(prompt)
    except Exception as e:
        logging.error(f"Error generating response: {e}")
        raise HTTPException(status_code=500, detail="Failed to generate response")

    return {"response": response}

if __name__ == "__main__":

    pass
