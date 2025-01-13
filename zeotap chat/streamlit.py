import streamlit as st
import requests


API_URL = "http://localhost:8000/ask"  


st.title("Zeotap Documentation Chatbot")


user_question = st.text_input("Ask a question about the documentation:")


if st.button("Ask"):
    if user_question:
       
        response = requests.post(API_URL, json={"question": user_question})

        
        if response.status_code == 200:
           
            response_data = response.json()
            content = response_data.get("response", {}).get("content", "No content available.")
            
            
            st.write("**Response:**")
            st.write(content)
        else:
            
            st.error(f"Error: {response.status_code} - {response.text}")
    else:
        st.warning("Please enter a question.")
