import os
import streamlit as st
from langchain_groq import ChatGroq
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains import create_retrieval_chain
from langchain_community.vectorstores import FAISS # vectrt store db
from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain_google_genai import GoogleGenerativeAIEmbeddings # vector emdeb

from dotenv import load_dotenv
from pathlib import Path

load_dotenv()

## load the GROQ and google generative AI embeddings

groq_api_key = os.getenv("GROQ_API_KEY")
os.environ['GOOGLE_API_KEY'] = os.getenv("GOOGLE_API_KEY")

google_api_key = os.getenv("GOOGLE_API_KEY")
if google_api_key is None:
    raise ValueError("Google API Key is not set. Please check your environment variables.")

st.title("Gemma Model Doc Q&A")

llm = ChatGroq(groq_api_key=groq_api_key, model="Gemma-7b-It")

prompt = ChatPromptTemplate.from_template(
    """
    Answer the question based on the provided context. If the question can't be answered based on the context, say "Sorry, I don't know".
    Please provide the most accurate responce based on the question.
    <context>
    {context}
    <context>
    QUESTION: {input}
    ANSWER:

    """
)

def vector_embedding():

    if "vectors" not in st.session_state:
        try:
            st.session_state.embeddings=GoogleGenerativeAIEmbeddings(model = "models/embedding-001")
            st.session_state.loader=PyPDFDirectoryLoader("./data") ## Data Ingestion
            st.session_state.docs=st.session_state.loader.load() ## Document Loading
            st.session_state.text_splitter=RecursiveCharacterTextSplitter(chunk_size=1000,chunk_overlap=200) ## Chunk Creation
            st.session_state.final_documents=st.session_state.text_splitter.split_documents(st.session_state.docs[:20]) #splitting
            st.session_state.vectors=FAISS.from_documents(st.session_state.final_documents,st.session_state.embeddings) #vector OpenAI embeddings
            st.write("Vector Store DB Is Ready")
        except Exception as e:
            st.error(f"Error embedding documents: {e}")
            print(f"Error embedding documents: {e}")


# taking user input
prompt1=st.text_input("Enter Your Question From Doduments")


if st.button("Documents Embedding"):
    vector_embedding()

import time


if prompt1:
    document_chain=create_stuff_documents_chain(llm,prompt)
    retriever=st.session_state.vectors.as_retriever()
    retrieval_chain=create_retrieval_chain(retriever,document_chain)
    
    start=time.process_time()
    
    try:
        response=retrieval_chain.invoke({'input':prompt1})
        print("Response time :",time.process_time()-start)
        st.write(response['answer'])

        # With a streamlit expander
        with st.expander("Document Similarity Search"):
            # Find the relevant chunks
            for i, doc in enumerate(response["context"]):
                st.write(doc.page_content)
                st.write("--------------------------------")

    except Exception as e:
        st.error(f"Error processing query: {e}")