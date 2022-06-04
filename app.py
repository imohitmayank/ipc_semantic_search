# import
import pandas as pd
import streamlit as st
from txtai.embeddings import Embeddings

# set config
st.set_page_config(layout="wide", page_title="IPC Semantic Search")

# load the summarization model (cache for faster loading)
@st.cache(allow_output_mutation=True)
def load_model_embeddings_data():
    model = Embeddings({"path": "sentence-transformers/nli-mpnet-base-v2"})
    embeddings = model.load("embedding")
    df = pd.read_csv("devganscrap/sections_desc.csv")
    return model, embeddings, df

# loading the model
model, embeddings, df = load_model_embeddings_data()

# APP
# set title and subtitle
st.title("IPC Semantic Search")
st.markdown("Search the Indian Penal Code Sections with simple english")
# create the input text box
query = st.text_area("Input your search phrase here!", "animal cruelty")
button = st.button("Find sections..")

# if button is clicked
with st.spinner("Finding the most similar sections...."):
    if button:
        # find the section
        for id, score in embeddings.search(query, limit=5):
            print(f"Section: {df.loc[id, 'section']}\nDescription: {df.loc[id, 'description']}\n----------\n")