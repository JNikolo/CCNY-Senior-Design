import streamlit as st
import requests

API_URL_SUMMARIZE = "http://127.0.0.1:5000/dual_summarize"
API_URL_SUMMARIES = "http://127.0.0.1:5000/summarize_batch"


st.title("Text Summarizer")
st.write("Enter text to generate summaries using the TextSummarizer and GeminiSummarizer models.")

#input
user_input = st.text_area("Input Text", placeholder="Type or paste your text here...")
if st.button("Generate Summaries"):
    if not user_input.strip():
        st.error("Please provide text input to generate summaries.")
    else:
        #use api functions (streamlit_app.py)
        data = {"text": user_input}

        with st.spinner("Generating summaries..."):
            try:
                #request for LSTM summarizer
                response_text = requests.post(API_URL_SUMMARIZE, json=data)
                response_text.raise_for_status()  # Check for HTTP errors
                text_summary = response_text.json().get("text_summary", "No summary generated.")

                gemini_summary = response_text.json().get("gemini_summary", "No summary generated.")

                #display results
                st.subheader("Summaries:")
                st.write("### TextSummarizer Output:")
                st.write(text_summary)

                st.write("### GeminiSummarizer Output:")
                st.write(gemini_summary)

            except requests.exceptions.RequestException as e:
                st.error(f"Error contacting the API: {e}")

#Add a new page for Reviews Summarization
st.title("Reviews Summarizer")
st.write("Enter multiple reviews to get concise summaries.")

#Input: multiple reviews
reviews_input = st.text_area(
    "Paste your reviews here (one per line):",
    placeholder="Example:\nReview 1\nReview 2\nReview 3",
    height=200,
)
if st.button("Summarize Reviews"):
    if not reviews_input.strip():
        st.error("Please enter at least one review.")
    else:
        #Split the reviews into a list
        reviews = [review.strip() for review in reviews_input.split("\n") if review.strip()]
        st.write(f"**Number of Reviews:** {len(reviews)}")

        #Prepare API request
        data = {"texts": reviews}  # Adjust payload to match the API requirements

        with st.spinner("Summarizing reviews..."):
            try:
                # Send reviews to the API
                response = requests.post(API_URL_SUMMARIES, json=data)
                response.raise_for_status()  # Check for HTTP errors
                summaries = response.json().get("summaries", ["No summary generated."] * len(reviews))

                st.success("Summarization complete!")
                st.markdown("### Summaries:")
                for i, summary in enumerate(summaries, start=1):
                    st.markdown(f"**Review {i}:** {summary}")

            except requests.exceptions.RequestException as e:
                st.error(f"Error contacting the API: {e}")



# # This will be for the api endpoints 
# API_URL_SUMMARIZE = ""
# import streamlit as st
# import requests
# import pandas as pd

# # This will be for the api endpoints 
# API_URL_SUMMARIZE = ""
# API_URL_EVALUATE = ""
# API_KEY = "" # The API key would be here 

# # This will be the title for dashboard
# st.title("Text Summarization Dashboard")
# st.sidebar.header("Model Configuration")

# # This is the Prediction Section
# st.write("## Prediction")
# with st.container():
#     # THis here will iput our reviw
#     st.write("### Input Review")
#     query = st.text_area("Enter text to summarize:")

#     # This will be a checkbox for any custom documents
#     use_custom_documents = st.checkbox("Use custom documents for RAG")
#     if use_custom_documents:
#         st.write("### Additional Context Documents")
#         documents_input = st.text_area("Enter documents (one per line):")
#     else:
#         documents_input = None
#     if st.button("Summarize"):
#         documents = documents_input.strip().split("\n") if use_custom_documents and documents_input else []
#         if query:
#             payload = {
#                 "query": query,
#                 "documents": documents,
#             }
#             headers = {"X-API-Key": API_KEY}
#             with st.spinner("Generating summary..."):
#                 try:
#                     response = requests.post(API_URL_SUMMARIZE, json=payload, headers=headers)
#                     if response.status_code == 200:
#                         summary = response.json().get("summary", "No summary generated.")
#                         st.write("### Generated Summary")
#                         st.text_area("Summary:", value=summary, height=150)
#                     else:
#                         st.error(f"Error {response.status_code}: {response.text}")
#                 except requests.exceptions.RequestException as e:
#                     st.error(f"API Connection Error: {e}")
#         else:
#             st.warning("Please enter text to summarize.")

# # This will evalute our model 
# st.write("## Evaluate Our Model")
# with st.container():
#     st.write("### Input Review")
#     review_input = st.text_area("Enter the generated summary for evaluation:")
#     st.write("### Reference Summary")
#     reference_summary = st.text_area("Enter the reference summary:")

#     # This will evalute our summary 
#     if st.button("Evaluate Summary"):
#         if review_input and reference_summary:
#             payload = {
#                 "input_review": review_input,
#                 "reference_summary": reference_summary,
#                 "metrics": ["rouge-1", "rouge-l"],  # metrics would go here. 
#             }
#             headers = {"X-API-Key": API_KEY}


#             # THis is for evaltuing the f1 scores. Will handle errors accrodingly. 
#             with st.spinner("Evaluating metrics..."):
#                 try:
#                     response = requests.post(API_URL_EVALUATE, json=payload, headers=headers)
#                     if response.status_code == 200:
#                         metrics = response.json()
#                         st.write("### Output Metrics")
#                         for metric, scores in metrics.items():
#                             st.write(f"**{metric.upper()}**")
#                             st.write(f"- Precision: {scores['precision']:.2f}")
#                             st.write(f"- Recall: {scores['recall']:.2f}")
#                             st.write(f"- F1-Score: {scores['f1-score']:.2f}")
#                     else:
#                         st.error(f"Error {response.status_code}: {response.text}")
#                 except requests.exceptions.RequestException as e:
#                     st.error(f"API Connection Error: {e}")
#         else:
#             st.warning("Please provide both input review and reference summary.")

# # THis is for the side bar.
# # Note: can change the lengh like max or minimum. 
# st.sidebar.write("### Summarization Parameters")
# max_length = st.sidebar.slider("Maximum Summary Length", 30, 300, 130)
# min_length = st.sidebar.slider("Minimum Summary Length", 10, 100, 30)
# do_sample = st.sidebar.checkbox("Enable Sampling", value=False)


# # An example --> Can be removed later
# st.write("## News Dataset Comparison")
# @st.cache_data
# def load_news_dataset():
#     data = {
#         "Title": ["Example News 1", "Example News 2"],
#         "Content": ["This is the content of news 1.", "This is the content of news 2."]
#     }
#     return pd.DataFrame(data)


# news_dataset = load_news_dataset()
# st.write(news_dataset)


# # We can try adding a home page later 


