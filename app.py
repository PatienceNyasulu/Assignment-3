import streamlit as st
import pandas as pd
import pickle

from preprocessing_utils import *

st.write("""
    # Newspaper Article Clustering
""")
st.markdown('[Link to GitHub code](https://github.com/PatienceNyasulu/Web_content-mining)')


articles = pd.read_csv('clustered_articles.csv')

# Get selected category
selected_category = st.selectbox("Select a category:", ['politics', 'business', 'culture', 'sport'])

#st.write('Selected Category:', selected_category)

k_means = pickle.load(open('kmeans_model.pkl', 'rb'))

# Filter articles by selected category
clustered_articles = articles[articles['category'] == selected_category]

# Get unique clusters for the selected category
clusters = clustered_articles['clusters'].unique()

# Get selected cluster from the user
selected_cluster = st.selectbox("Select a cluster:", clusters)

st.write('Selected Cluster:', selected_cluster)

# Filter articles by selected cluster
selected_cluster_articles = clustered_articles[clustered_articles['clusters'] == selected_cluster]

# Display URLs of articles in the selected cluster
st.write('Related Articles:')
st.write(selected_cluster_articles['url'])
