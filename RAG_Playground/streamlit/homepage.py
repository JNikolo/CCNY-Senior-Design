import streamlit as st

# Home page 
#st.set_page_config(page_title="Text Summarization App", page_icon="📝", layout="wide")

# This is the sidebar --> Here add places where we want to navigate so for example the other pages.
# about = st.Page("about.py", title="About Page", icon="ℹ️")
# summarization = st.Page("summarization.py", title="Summarization Dashboard")
# #rag = st.Page("rag.py", title="RAG Playground", description="This page allows you to experiment with the RAG model.")
# st.sidebar.title("Navigation")
# pg = st.navigation([about, summarization])
# pg.run()

# This is the sidebar --> Here add places where we want to navigate so for example the other pages. 
# st.sidebar.write("---")
# st.sidebar.header("Quick Links")
# st.sidebar.markdown("""
# - [GitHub Repository](https://github.com/JNikolo/CCNY-Senior-Design)
# - [Documentation](https://github.com/JNikolo/CCNY-Senior-Design/tree/main/api)
# - [Contact Us](https://github.com/JNikolo/CCNY-Senior-Design)
# """) 

# This is for the welcome section
st.title("Welcome to the **Text Summarization App**! 📝")
st.write("### A Smarter Way to Summarize and Evaluate Text.")
st.write("""
This app uses advanced machine learning models to make text summarization and evaluation easy. 
Whether you want to summarize long text, check how accurate the summaries are, or compare results 
from different models, this app can help.
""")

# The features section show a little what it can do. 
st.write("---")  # Dividers
st.header("What Can This App Do?")
st.write("Explore the main features of this application below:")

# This will create the subpoint block
col1, col2 = st.columns(2)

# Give some context about the app. 
with col1:
    st.subheader("🔍 **Generate Summaries**")
    st.write("""
    - Use ML models to summarize long pieces of text.
    - Add custom context documents to improve the quality of the summary.
    - Choose summarization parameters like max length and sampling directly from the app.
    """)

with col2:
    st.subheader("📊 **Evaluate Summaries**")
    st.write("""
    - Evaluate the accuracy and quality of generated summaries.
    - Use popular metrics like ROUGE-1 and ROUGE-L to assess performance.
    - Easily visualize the precision, recall, and F1-score of the summaries.
    """)

# Additional features about our section
st.write("---")  
st.header("Why Use This App?")
st.write("""
- **Interactive Dashboard**: Easily configure model settings and evaluate results in real-time.
- **Flexible Inputs**: Incorporate your own custom documents to generate highly accurate summaries.
- **Performance Metrics**: Get detailed insights into how well the summaries perform.
""")

# This is for navigated thourgh the app details
st.write("---")  
st.header("Navigate Through the App")
st.write("Here’s how you can get started:")
col3, col4 = st.columns(2)

with col3:
    st.subheader("🖥️ Summarization Dashboard")
    st.write("""
    - Enter text to summarize.
    - Provide additional documents for better summarization using RAG techniques.
    - Adjust model parameters like length and sampling.
    """)
with col4:
    st.subheader("📖 About Page")
    st.write("""
    - Learn more about the project and its purpose.
    - Access links to the GitHub repository and documentation.
    - Understand the technical implementation of the models.
    """)

# Little expllanation on how to do 
st.write("---")  # Divider
st.write("### To Get Started")
st.write("""
Explore the Summarization Dashboard or learn more about the project through the About Page. 
""")


st.write("---")
st.write("💡 Developed as part of a senior design project using NLP and ML techniques.")
