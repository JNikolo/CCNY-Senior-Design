import streamlit as st

# Home page 
st.set_page_config(page_title="Text Summarization App", page_icon="📝", layout="wide")

# This is the sidebar --> Here add places where we want to navigate so for example the other pages.
homepage = st.Page("homepage.py", title="Home Page", icon="🏠")
about = st.Page("about.py", title="About Page", icon="ℹ️")
summarization = st.Page("summarization.py", title="Summarization Dashboard", icon="📊")
rag = st.Page("rag.py", title="RAG Playground", icon="🧪")

# This is the sidebar --> Here add places where we want to navigate so for example the other pages. 
st.sidebar.header("Quick Links")
st.sidebar.markdown("""
- [GitHub Repository](https://github.com/JNikolo/CCNY-Senior-Design)
- [Documentation](https://github.com/JNikolo/CCNY-Senior-Design/tree/main/api)
- [Contact Us](https://github.com/JNikolo/CCNY-Senior-Design)
""") 

pg = st.navigation([homepage, about, summarization, rag])
pg.run()