# Chatbot-for-CDP

# Zeotap Documentation Chatbot

This project is an AI-powered chatbot designed to interact with users and answer questions about documentation for various Customer Data Platform (CDP) services. It uses FastAPI for backend API services, FAISS for similarity search, LangChain for text management,  OpenAI for natural language processing, and Streamlit for a user-friendly interface.

---

## Features

- Fetches and processes documentation from popular CDPs:
  - Segment
  - mParticle
  - Lytics
  - Zeotap
- Preprocesses and indexes the documentation for efficient similarity-based search.
- API endpoint for querying documentation through natural language questions.
- Interactive chatbot interface built using Streamlit.
- Scalable and modular design, allowing easy integration with additional services.

---
## Technologies Used

**FastAPI:** For creating and serving RESTful APIs.
**Streamlit:** For building an interactive chatbot interface.
**FAISS:** For efficient similarity search in vectorized text.
**LangChain:** For preprocessing and managing text data.
**BeautifulSoup:** For parsing and cleaning HTML documents.




## Installation

### Prerequisites

- Python 3.8 or higher
- Required Python packages (see `requirements.txt`)

### Steps

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/sivabalaji29/Chatbot-for-CDP.git
   cd zeotap-chatbot

# Install Dependencies:
  pip install -r requirements.txt



# Step 1: Fetch Documentation
Run the fetch_documentation function to download and save the CDP documentation to the db folder:

python preprocess.py

# Step 2: Start the Backend API
Launch the FastAPI server to expose the /ask endpoint:

uvicorn app:app --reload

# Step 3: Run the Streamlit Interface
Start the Streamlit app to access the interactive chatbot UI:

streamlit run streamlit.py

# Step 4: Query the Documentation
Open the Streamlit app in your browser.
Enter your question about the documentation in the input field.
Receive AI-generated answers based on the indexed documentation.

![Screenshot 2025-01-14 000153](https://github.com/user-attachments/assets/8b105158-6e91-48c5-a0b9-197f51afcca5)


![Screenshot 2025-01-14 000231](https://github.com/user-attachments/assets/6e367520-b8d7-4001-af79-59a03db1f006)


![Screenshot 2025-01-14 000314](https://github.com/user-attachments/assets/8e0008da-87d4-4556-9189-6e89ad27b1ef)


![Screenshot 2025-01-14 000344](https://github.com/user-attachments/assets/72df0df4-75e3-46da-88d0-6e2d4b3be45f)


![Screenshot 2025-01-14 000523](https://github.com/user-attachments/assets/c92dd32c-1f2a-42c4-a441-52f5a870473e)


# Future Improvements

Add support for additional CDP platforms.
Enhance the UI with advanced features like file uploads or context persistence.
Implement a feedback loop to improve response accuracy.
Optimize embeddings and vector store indexing for better performance.


# License
This project is licensed under the MIT License. See the LICENSE file for details.










   
