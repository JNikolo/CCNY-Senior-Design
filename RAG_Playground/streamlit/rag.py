import streamlit as st
import requests

# This will be for the api endpoints
API_URL_INJECT = "http://127.0.0.1:5000/inject"
API_URL_QUERY = "http://127.0.0.1:5000/search"
API_URL_CLEAN = "http://127.0.0.1:5000/clean_db"

st.title("Retrieval-Augmented Generation Playground")
st.write("Enter the URL of the walmart product you want to generate a summary for. It should be the reviews page of the product.")

# Input
url = st.text_input("Product Reviews URL", placeholder="https://www.walmart.com/reviews/product/10450114")
max_pages = st.number_input("Number of Pages", min_value=1, max_value=10, value=2)

if st.button("Get Reviews"):
    if not url.strip():
        st.error("Please provide a valid URL to generate summaries.")
    else:
        data = {"url": url, "max_pages": max_pages}
        with st.spinner("Fetching reviews..."):
            response = requests.post(API_URL_INJECT, json=data)
            response.raise_for_status()

            message = response.json().get("message", "No reviews found.")

            st.write(message)
if st.button("Clear"):
    try:
        response = requests.post(API_URL_CLEAN)
        response.raise_for_status()
        st.success("Database cleaned successfully.")
    except Exception as e:
        st.error(f"Error cleaning database: {e}")
# Query
query = st.text_input("Query", placeholder="What is the product about?")
top_k = st.number_input("Top K", min_value=1, max_value=10, value=5)

if st.button("Search Reviews"):
    if not query.strip():
        st.error("Please provide a valid query to search review.")
    else:
        data = {"query": query, "top_k": top_k}
        with st.spinner("Searching reviews..."):
            response = requests.post(API_URL_QUERY, json=data)
            response.raise_for_status()

            reviews = response.json().get("reviews", [])
            results = response.json().get("results", [])
            llm_summary = response.json().get("llm_summary", "No summary generated.")
            st.write("### Reviews:")
            st.write(reviews)
            st.write("### Reviews summarized:")
            st.write(results)
            st.write("### LLM Summary:")
            st.write(llm_summary)
