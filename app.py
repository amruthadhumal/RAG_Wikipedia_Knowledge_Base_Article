# =====================================================
# Simple RAG Streamlit App
# Wikipedia Knowledge Base + FAISS + Mistral
# =====================================================

import streamlit as st

from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from transformers import pipeline

# -----------------------------------------------------
# Page Configuration
# -----------------------------------------------------

st.set_page_config(
    page_title="Wikipedia RAG Assistant",
    page_icon="📚",
    layout="wide"
)

st.title("📚 Wikipedia RAG Assistant")
st.write("Ask questions from the Wikipedia Knowledge Base")

# -----------------------------------------------------
# Load Embeddings
# -----------------------------------------------------

@st.cache_resource
def load_embeddings():
    return HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

# -----------------------------------------------------
# Load FAISS Database
# -----------------------------------------------------

@st.cache_resource
def load_vectorstore():

    embeddings = load_embeddings()

    vectorstore = FAISS.load_local(
        "wiki_faiss_db",
        embeddings,
        allow_dangerous_deserialization=True
    )

    return vectorstore

# -----------------------------------------------------
# Load LLM
# -----------------------------------------------------

@st.cache_resource
def load_llm():

    llm = pipeline(
        "text-generation",
        model="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
        device_map="auto"
    )

    return llm

# -----------------------------------------------------
# RAG Function
# -----------------------------------------------------

def ask_rag(question):

    vectorstore = load_vectorstore()
    llm = load_llm()

    docs = vectorstore.similarity_search(
        question,
        k=3
    )

    context = "\n".join(
        [doc.page_content for doc in docs]
    )

    prompt = f"""
    Context:
    {context}

    Question:
    {question}

    Answer:
    """

    result = llm(
        prompt,
        max_new_tokens=200,
        do_sample=False
    )

    answer = result[0]["generated_text"]

    return answer, docs

# -----------------------------------------------------
# User Input
# -----------------------------------------------------

question = st.text_input(
    "Enter your question"
)

if st.button("Get Answer"):

    if question:

        with st.spinner("Searching knowledge base..."):

            answer, docs = ask_rag(question)

        st.subheader("Answer")
        st.write(answer)

        st.subheader("Retrieved Context")

        for i, doc in enumerate(docs):
            with st.expander(f"Document {i+1}"):
                st.write(doc.page_content)

    else:
        st.warning("Please enter a question.")