# import
import pandas as pd
import streamlit as st
from txtai.embeddings import Embeddings

# set config
st.set_page_config(layout="wide", page_title="⚖️ Law Finder - IPC")

# load the summarization model (cache for faster loading)
@st.cache(allow_output_mutation=True)
def load_model_embeddings_data():
    embeddings = Embeddings({"path": "sentence-transformers/nli-mpnet-base-v2"})
    embeddings.load("embedding")
    df = pd.read_csv("devganscrap/sections_desc.csv")
    return embeddings, df

# loading the model
embeddings, df = load_model_embeddings_data()

# APP
# set title and subtitle
st.title("⚖️ Law Finder - IPC")
st.markdown("Search the [Indian Penal Code](https://en.wikipedia.org/wiki/Indian_Penal_Code) Sections with simple english.")
st.markdown("The data scraping procedure is explained in detail on [my website](http://mohitmayank.com/a_lazy_data_science_guide/python/scraping_websites/)")
st.markdown("The complete code is on [Github](https://github.com/imohitmayank/ipc_semantic_search)")

# create the input text box
query = st.text_area("Input your search phrase here!", "animal cruelty")
button = st.button("Find sections...")

# if button is clicked
with st.spinner("Finding the most similar sections...."):
    if button:
        # find and display the sections
        st.markdown("**Sections:**")
        results = []
        for id, score in embeddings.search(query, limit=5):
            st.write({
                'section': df.loc[id, 'section'],
                'description': df.loc[id, 'description']
            })