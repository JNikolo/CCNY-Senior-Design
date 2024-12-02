import streamlit as st

# The about page info
#st.set_page_config(page_title="About | Text Summarization App", )
st.title("About the **Text Summarization App** ℹ️")
st.write("### Discover the Purpose and Features of This App")

# Conclusion/Intro 
st.write("""
This app is part of a senior design project. It uses machine learning to make text summarization and evaluation easier.
Our goal is to help users quickly summarize text and measure the quality of the summaries.
""")
# Quick Description change if anything 
st.write("---") 
st.header("📌 Why We Built This App")
st.write("""
This app was created to:
- Make summarizing text simple and fast.
- Help users evaluate summaries with metrics like ROUGE.
- Provide an easy-to-use interface for generating and evaluating text summaries.
""")
         
# About the Team And Github 
st.write("---")
st.header("👨‍💻 About the Team")
st.write("""
This app was built by a senior design team with a passion for machine learning and natural language processing.
""")
st.subheader("🔗 Useful Links")
st.write("""
- [GitHub Repository](https://github.com/JNikolo/CCNY-Senior-Design)
- [Documentation](https://github.com/JNikolo/CCNY-Senior-Design/tree/main/api)
""")
st.write("---")
st.write("""
Thank You! Check the **Summarization Dashboard** to start summarizing and evaluating text.
""")
