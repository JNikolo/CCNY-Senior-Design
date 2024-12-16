<!-- Back to top link -->
<a name="readme-top"></a>


<!-- PROJECT LOGO -->
<div align="center">
<h1 align="center">Net Design - RAG Playground</h1>

  <p align="center">
    An interactive platform for exploring Retrieval-Augmented Generation (RAG) systems and abstractive text summarization
  </p>
</div>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li><a href="#team-members">Team Members</a></li>
    <li><a href="#quick-links">Quick Links</a></li>
    <li>
      <a href="#rag-playground">RAG Playground</a>
      <ul>
        <li><a href="#key-features">Key Features</a></li>
      </ul>
    </li>
    <li><a href="#project-presentations">Project Presentations</a></li>
    <li><a href="#dataset">Dataset</a></li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#project-development-research">Project Development Research</a></li>
    <li><a href="#about-us">About Us</a></li>
  </ol>
</details>

## Team Members
- [Jair Ruiz](https://github.com/JNikolo)  
  [![LinkedIn](https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555)](https://linkedin.com/in/jair-ruiz)

- [Usman Abbas](https://github.com/uscod)  
  [![LinkedIn](https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555)](https://www.linkedin.com/in/usman-abbas-4b7770317/)

- [Evan Perez](https://github.com/evanperez444)  
  [![LinkedIn](https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555)](https://www.linkedin.com/in/perezevan/)

## Quick Links
- [Notebooks for training model, data mining, and evaluation](Notebooks/)
- [Code for the full-stack application](RAG_Playground/)
- [Code to train the Deep Learning Model easily](api/)
- ⌞‼⌝ [Project Final Report Document](https://docs.google.com/document/d/1ULCsQyWiKkRIXwG25bPKsxRUIvLo9e4pVbrY7XOFeO4/edit?usp=sharing) ⌞‼⌝

## RAG Playground
![WhatsApp Image 2024-12-02 at 13 22 23_0b15d46c](https://github.com/user-attachments/assets/37cec930-a51e-44bd-bb29-dea78678f907)

This project focuses on building/finetuning a deep learning model to perform abstractive text summarization. Additionally, the project aims to create an interactive platform for hands-on exploration of Retrieval-Augmented Generation (RAG) systems. Users will be able to compare the performance of the standalone model with that of the RAG system in summarization tasks.

![RAG Playground Screenshot](https://github.com/JNikolo/CCNY-Senior-Design/assets/125705821/6c4abf42-2fba-4084-a32c-974465161a3d)

### Key Features
1. **Abstractive Summarization:** Training a deep learning model to perform abstractive summarization of texts.

2. **Customization Options:** Provide users with the ability to customize various parameters of the RAG models, such as the retrieval strategy, generation settings, and input data sources.

3. **Performance Comparison:** Allowing users to compare the summarization performance of our model against the AI system.

### Built With

* [![Python][Python.org]][Python-url]
* [![TensorFlow][TensorFlow.org]][TensorFlow-url]
* [![Streamlit][Streamlit.app]][Streamlit-url]
* [![Flask][Flask.com]][Flask-url]

## Getting started
### Prerequisites

Before you begin, ensure you have the following installed:
* Python 3.8 or higher
  ```sh
  python --version  # Check your Python version
  ```

* pip (Python package manager)
  ```sh
  pip --version  # Check pip version
  ```

### Installation

1. Clone the repository
   ```sh
   git clone https://github.com/JNikolo/CCNY-Senior-Design.git
   cd CCNY-Senior-Design
   ```

2. Create and activate a virtual environment (recommended)
   ```sh
   # Windows
   python -m venv venv
   .\venv\Scripts\activate

   # macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```
#### Training the model
   1. Install all dependencies
      ```sh
      cd api
      pip install -r requirements.txt
      ```
   2. Follow instructions in [`README.md`](/api/README.md) to train your model or use [`example.py`](/api/example.py) to start

#### Running the application
   1. Install all dependencies
      ```sh
         cd api
         pip install -r requirements.txt
      ```
   2. Create a .env file, see [`.env.sample`](/RAG_Playground/api/.env.sample) as an example, and start the server
      ```sh
      # Navigate to backend directory
      cd rag_playground/api
      touch .env
      python app.py
      ```

   3. In a new terminal, start the Streamlit frontend
      ```sh
      # Navigate to frontend directory
      cd rag_playground/streamlit
      streamlit run main.py
      ```

The application should now be running at:
- Frontend: http://localhost:8501
- Backend API: http://127.0.0.1:5000

## Project Presentations
- [Project Proposal](https://docs.google.com/presentation/d/1FeWjZ08U_bxXY8HETvEQ2Stk9Us1oO6mexBh0WYTLHo/edit?usp=sharing)
- [First Update](https://docs.google.com/presentation/d/1zdITAq-Jup3Cn-_ZQrCusIorHMXZGKbc2iP00UaLSrc/edit?usp=sharing)
- [Second Update](https://docs.google.com/presentation/d/1NVGF9PX7dp-oi380DOlgTdgCqsds3E0KZhDJIq4OuNU/edit?usp=sharing)
- [Third Update](https://docs.google.com/presentation/d/1DOyjDkYukcNkbUq47O0cVic0O2sxrRK_Cjq6lpjPpFQ/edit?usp=sharing)
- [Midterm Presentation](https://docs.google.com/presentation/d/1ieUe0iN5Ay0Ja77RSPIDyiXBMAPUYFfZ0d9_BM9R40k/edit?usp=sharing)
- [Code Organization](https://docs.google.com/presentation/d/1SSujFJub1Fq22ds0xiPLN-ORdPxhlYHpzAVCumiEA20/edit?usp=sharing)
- [Project Poster](https://docs.google.com/presentation/d/1rAOGZ5JD9jo_wqC32g5U0crWHvT0b_cgT7wWeayUvbc/edit?usp=sharing)
- [Final Project Presentation](https://docs.google.com/presentation/d/1Bt1WlfJEjnX0RuZc9flhsH_Rc4YFNu_zAqJ24SBATzk/edit?usp=sharing)


## Dataset
This project uses the [Amazon Fine Food Reviews dataset](https://www.kaggle.com/datasets/snap/amazon-fine-food-reviews), which includes:
- ~500,000 reviews spanning over 10 years
- Food Reviews Summaries in ~10 words or less
- Data splits:
  - Train: 314,573
  - Validation: 78,644

Example entry:
```json
{
  "id": 456,
  "Text": "These cookies are absolutely delicious! They are crispy, not too sweet, and have a nice buttery flavor. I can't stop eating them. Will definitely buy again!",
  "summary": "Best cookies ever!",
  "asin": "B01N6P0FHH"
}
```
## Project Development Research
### Ideas collection
<details>
<summary>The following is a collection of previous work that relates to our project idea.</summary>

| Ideas | Overview | Components/Techniques | Technology/Libraries/Tools | Notes |
|-------|---------|-------|---------|---------|
| [fastRAG](https://github.com/IntelLabs/fastRAG) | FastRAG is a research framework developed by Intel Labs, designed for creating efficient and optimized retrieval-augmented generative (RAG) pipelines. <details><summary>**Read more**</summary>It includes LLM backends like Intel Gaudi Accelerators, ONNX Runtime, and Llama-CPP for running RAG pipelines efficiently, along with RAG-efficient components like Colbert for token-based late interaction, Fusion-in-Decoder (FiD) for generative multi-document encoding and decoding, and REPLUG for improved multi-document decoding.</details> | <details><summary>**Explore the components**</summary> <ul> <li><details><summary><b>REPLUG (Retrieve and Plug):</b></summary><ul><li>Retrieval-augmented LM method.</li><li>Documents are retrieved and plugged into the input using ensembling.</li><li>Works with any LM without fine-tuning.</li><li>Enables processing a larger number of retrieved documents without limiting to the LM context window.</li></ul> </details></li> ... | <details> <summary>**Explore key libraries**</summary><ul><li>farm-haystack</li><li>transformers</li><li>datasets</li>...</ul></details> | Useful project to have an idea how to build different types of RAG pipelines. Most likely not to be too much referenced, since it does not align too much with our idea.
| [Haystack](https://github.com/deepset-ai/haystack) | The goal of the LLM orchestration framework Haystack by deepset.ai is to create LLM applications that are adaptable and ready for production. <details><summary>**Read more**</summary>It facilitates the creation of pipelines for data interaction by joining different parts, such as file converters, vector databases, and models...</details> | <details><summary>**Explore the components**</summary><ul><li><details><summary>**Components**</summary><ul><li><b>Generators:</b> Responsible for generating text responses...</li><li><b>Retrievers:</b> Select documents matching user queries...</li></ul></details></li>... | <details><summary>**Explore key libraries**</summary> <ul><li>Hatchling (build system)</li><li>Pandas</li>...</ul></details>| This project is interesting to look at because it expands in the creation of AI tools. This will give us an idea on how we can create a powerful interface for users to create their RAG pipelines since Haystack is a fully functional framework. |
| [RAGs](https://github.com/run-llama/rags) | RAGs is a Streamlit app inspired by OpenAI's GPTs, allowing users to create a RAG pipeline using natural language. <details><summary>**Read more**</summary>Users can describe their task and specify parameters such as the number of documents to retrieve...</details> | <details><summary>**Explore the components**</summary> <ul><li><details><summary>Home Page</summary>This is the section where you build a RAG pipeline...</details></li>...</ul></details> | ... | ...
</details>

### Datasets
<details><summary>Datasets for Summarization Tasks</summary>

| **Datasets** | **Overview** | **Size** | **Structure** | **Domain** | **To be used** | **Notes** | 
|--------------|--------------|----------|---------------|------------|----------------|-----------|
| [WikiHow-Dataset](https://github.com/mahnazkoupaee/WikiHow-Dataset/tree/master) | This is a large-scale summarization dataset consisting of diverse articles from the WikiHow knowledge base. | +200K pairs of articles and summaries | The dataset is presented in a .csv file format and the columns are Title, Headline, and Text. <details><summary>**Read more**</summary><ul><li><b>Title:</b> The title of the article as it appears on the WikiHow knowledge base.</li><li><b>Headline:</b> The concatenation of all the bold lines (the summary sentences) of all the paragraphs to serve as the reference summary.</li><li><b>Text:</b> The concatenation of all paragraphs (except the bold lines) to generate the article to be summarized.</li></ul></details> | Knowledge Base | ✅ | The dataset needs to be processed using the script provided in the source repo. It will download all the summaries and articles for each of the titles. |
| [Scientific Papers Dataset](https://huggingface.co/datasets/armanc/scientific_papers)  | This large dataset contains two sets of long and structured documents. The datasets are obtained from ArXiv and PubMed OpenAccess repositories. | The ArXiv and PubMed datasets have +200K and +100k rows respectively. <details><summary>**Read more**</summary><ul><li><b>arXiv:</b><ul><li><b>Train:</b> 203,037</li><li><b>Validation:</b> 6,436</li><li><b>Test:</b> 6,440</li></ul></li><li><b>PubMed:</b><ul><li><b>Train:</b> 119,924</li><li><b>Validation:</b> 6,633</li><li><b>Test:</b> 6,658</li></ul></li></ul> | Both datasets have the columns: article, abstract, section_names; all the features are string.<details><summary>**Read more**</summary><ul><li><b>Article:</b> The body of the document, paragraphs separated by "/n".</li><li><b>Abstract:</b> The abstract of the document, paragraphs separated by "/n".</li><li><b>Section Names:</b> Titles of sections, separated by "/n".</li></ul></details> | Academic Paper | ✅ | In these datasets, the abstract is used as the summary. |
| [CNN/Daily Mail Dataset](https://www.kaggle.com/datasets/gowrishankarp/newspaper-text-summarization-cnn-dailymail) | The CNN / DailyMail Dataset is an English-language dataset containing just over 300k unique news articles as written by journalists at CNN and the Daily Mail. | This dataset contains +300k rows. <details><summary>**Read more**</summary><ul><li><b>Dataset Split:</b><ul><li><b>Train:</b> 287,113 instances</li><li><b>Validation:</b> 13,368 instances</li><li><b>Test:</b> 11,490 instances</li></ul></li></ul></details> | The dataset contains the columns: id, article and highlights. All of them are strings.<details><summary>**Read more**</summary><ul><li><b>ID:</b> A string containing the hexadecimal formatted SHA1 hash of the URL where the story was retrieved from</li><li><b>Article:</b> A string containing the body of the news article</li><li><b>Highlights:</b> A string containing the highlight of the article as written by the article author</li></ul></details> | News | ✅ | In the dataset, the highlights field is used as the summary of the text to perform evaluation. |

</details>


### Techniques and methods
The following is a collection of techniques for text summarization and to create the RAG systems.

<details>
  <summary>Text Summarization Techniques</summary>
  <table border="1">
    <thead>
      <tr>
        <th>Technique</th>
        <th>Overview</th>
        <th>Key Features</th>
        <th>Pros/Cons</th>
        <th>Use-cases</th>
        <th>When is needed?</th>
        <th>Notes</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><a href="https://aclanthology.org/2021.naacl-main.380.pdf">Graph-enhanced Multi-Document Summarization (MDS)</a></td>
        <td>An efficient graph-enhanced approach to multi-document summarization using an encoder-decoder Transformer model.</td>
        <td>
          <details>
            <summary>**Explore key features**</summary>
            <ul>
              <li>Incorporates an efficient encoding mechanism that avoids quadratic memory growth.</li>
              <li>Utilizes graph representations derived from multi-document clusters.</li>
              <li>Pre-trained on very large text data.</li>
            </ul>
          </details>
        </td>
        <td>
          <details>
            <summary>**Explore pros/cons**</summary>
            <p>Pros: Scales to large input documents, improves summary abstraction, and is more informative and factually consistent. Cons: Requires additional processing for graph representations.</p>
          </details>
        </td>
        <td>
          <details>
            <summary>**Explore use**</summary>
            <ul>
              <li>Summarizing news clusters.</li>
              <li>Any task involving summarization of large multi-document datasets.</li>
            </ul>
          </details>
        </td>
        <td>When dealing with large multi-document clusters and when factual consistency and informativeness are critical.</td>
        <td>The approach leads to significant improvements on the Multi-News dataset and shows transfer improvements on the DUC-2004 dataset. Provides a 1.8 ROUGE score improvement over previous work.</td>
      </tr>
      <tr>
        <td><a href="https://direct.mit.edu/coli/article/48/2/279/109901/Domain-Adaptation-with-Pre-trained-Transformers">Query-Focused Text Summarization (QFTS)</a></td>
        <td>Generates summaries of text documents based on a given query using transformer models.</td>
        <td>
          <details>
            <summary>**Explore key features**</summary>
            <ul>
              <li>Utilizes pre-trained transformer models.</li>
              <li>Applies domain adaptation techniques including transfer learning, weakly supervised learning, and distant supervision.</li>
            </ul>
          </details>
        </td>
        <td>
          <details>
            <summary>**Explore pros/cons**</summary>
            <p>Pros: Effective in generating abstractive summaries, sets new state-of-the-art results, versatile across single and multi-document scenarios. Cons: Lack of large labeled data for training, complexity in implementing domain adaptation techniques.</p>
          </details>
        </td>
        <td>
          <details>
            <summary>**Explore use**</summary>
            <ul>
              <li>Query-focused summarization for both single and multi-document scenarios.</li>
              <li>Tasks requiring summaries tailored to specific queries.</li>
            </ul>
          </details>
        </td>
        <td>When the goal is to generate summaries relevant to specific queries, especially in domains with limited labeled data.</td>
        <td>Extensive experiments on six datasets demonstrate the effectiveness of the approach, achieving new state-of-the-art results across various evaluation metrics.</td>
      </tr>
      <tr>
        <td><a href="https://aclanthology.org/2021.eacl-main.154.pdf">Hierarchical Propagation Layer for Transformer Models</a></td>
        <td>A novel layer designed to enhance transformer-based architectures for reasoning with long documents.</td>
        <td>
          <details>
            <summary>**Explore key features**</summary>
            <ul>
              <li>Divides input into multiple blocks.</li>
              <li>Independently processes each block with scaled dot-attentions.</li>
              <li>Combines information between successive layers.</li>
            </ul>
          </details>
        </td>
        <td>
          <details>
            <summary>**Explore pros/cons**</summary>
            <p>Pros: Effective for long document summarization, achieves state-of-the-art results. Cons: Complexity in implementation, potentially higher computational resources needed.</p>
          </details>
        </td>
        <td>
          <details>
            <summary>**Explore use**</summary>
            <ul>
              <li>Extractive summarization of long scientific papers.</li>
              <li>Extractive summarization of long news articles.</li>
            </ul>
          </details>
        </td>
        <td>When dealing with tasks that require understanding and summarizing long documents, especially in research and media domains.</td>
        <td>This technique provides a hierarchical approach that improves over standard transformers, particularly useful for tasks requiring processing of extensive text. Validated on three corpora, demonstrating superior performance for long documents and competitive results for shorter ones.</td>
      </tr>
      <!-- Add more rows here for other techniques -->
    </tbody>
  </table>
</details>


<details>
  <summary>RAG System Development</summary>
  <table>
    <thead>
      <tr>
        <th>Technique</th>
        <th>Overview</th>
        <th>Pros/Cons</th>
        <th>Use-cases</th>
        <th>Tools/Software</th>
        <th>To be used</th>
        <th>Notes</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><a href="https://www.linkedin.com/pulse/building-ai-chatbot-rag-langchain-streamlit-sachin-samuel-n9tef/">Building an AI Chatbot with RAG, Langchain, and Streamlit</a></td>
        <td>This technique presents a way to integrate a robust LLM framework like Langchain, and a friendly front-end framework like Streamlit to showcase RAG capabilities.</td>
        <td>
          <details>
            <summary>Explore pros/cons</summary>
            <b>Pros:</b>
            <ul>
              <li>Integration of Robust Framework: The technique integrates Langchain, a robust Large Language Model (LLM) framework, providing powerful language processing capabilities.</li>
              <li>User-Friendly Front-End: Streamlit, a friendly front-end framework, is used to create an intuitive and interactive interface for showcasing RAG capabilities.</li>
            </ul>
            <b>Cons:</b>
            <ul>
              <li>Technical Complexity: Implementing an AI chatbot with RAG, Langchain, and Streamlit may require a certain level of technical expertise, especially in setting up and configuring the components.</li>
              <li>Resource Intensive: Running an AI chatbot with these frameworks may be resource-intensive, requiring sufficient computational resources and infrastructure.</li>
            </ul>
          </details>
        </td>
        <td>
          <details>
            <summary>Explore use-cases</summary>
            <ul>
              <li>Customer Service: The AI chatbot can be deployed for customer service applications, providing automated responses to customer inquiries and support requests.</li>
              <li>Information Retrieval: Users can interact with the chatbot to retrieve information on various topics, leveraging the language processing capabilities of Langchain and the interactive interface of Streamlit.</li>
              <li>Educational Tools: The chatbot can serve as an educational tool, assisting users with learning and understanding concepts in natural language processing and AI.</li>
            </ul>
          </details>
        </td>
        <td>
          <ul>
            <li>Streamlit</li>
            <li>Langchain</li>
          </ul>
        </td>
        <td>✅</td>
        <td>Optimum technique to showcase our project to the world. Streamlit is easy to use, and Langchain is a very powerful framework.</td>
      </tr>
      <tr>
        <td><a href="https://ijisae.org/index.php/IJISAE/article/view/4500/3160">Abstractive Long Text Summarization using Large Language Models</a></td>
        <td>A novel approach for addressing the challenge of retaining context over extensive texts or multiple documents using Large Language Models (LLMs). The methodology focuses on improving summarization and question answering tasks by preventing LLM overload with unrelated, repetitive, or redundant data.</td>
        <td>
          <details>
            <summary>Explore pros/cons</summary>
            <b>Pros:</b>
            <ul>
              <li>Enhances summarization and question answering by retaining relevant context.</li>
              <li>Saves time and resources by avoiding processing of unrelated or redundant data.</li>
              <li>Improves overall performance and efficiency of LLMs.</li>
            </ul>
            <b>Cons:</b>
            <ul>
              <li>Implementation complexity may vary based on LLM architecture and task requirements.</li>
            </ul>
          </details>
        </td>
        <td>
          <details>
            <summary>Explore use-cases</summary>
            <ul>
              <li>Large-scale document summarization.</li>
              <li>Question answering systems for extensive texts or multiple documents.</li>
            </ul>
          </details>
        </td>
        <td>
          <ul>
            <li>Large Language Models (LLMs)</li>
            <li>Summarization and Question Answering frameworks</li>
          </ul>
        </td>
        <td>✅</td>
        <td>The proposed approach aims to optimize LLMs for better context retention, leading to more effective summaries and answers, thus enhancing overall system performance and efficiency.</td>
      </tr>
      <tr>
        <td><a href="https://arxiv.org/pdf/2403.15729">Retrieval Augmented Generation (RAG)-based Summarization AI for EIC</a></td>
        <td>A two-step approach involving a Retrieval Augmented Generation (RAG)-based Summarization AI for Electron Ion Collider (EIC) community. The AI-Agent condenses information and references relevant responses, offering substantial advantages for collaborators.</td>
        <td>
          <details>
            <summary>Explore pros/cons</summary>
            <b>Pros:</b>
            <ul>
              <li>Condenses vast and complex information into concise summaries.</li>
              <li>Effectively references relevant responses, enhancing collaboration.</li>
              <li>Utilizes RAG assessments (RAGAs) scoring mechanisms for evaluation.</li>
            </ul>
            <b>Cons:</b>
            <ul>
              <li>Complexity in development and integration.</li>
              <li>Potential challenges in ensuring accuracy and relevance of generated summaries.</li>
            </ul>
          </details>
        </td>
        <td>
          <details>
            <summary>Explore use-cases</summary>
            <ul>
              <li>Accessing and utilizing large-scale experiment information.</li>
              <li>Collaborative research in the Electron Ion Collider (EIC) community.</li>
            </ul>
          </details>
        </td>
        <td>
          <ul>
            <li>Large Language Models (LLMs)</li>
            <li>LangChain for workflow foundation</li>
            <li>Web application for demonstration</li>
          </ul>
        </td>
        <td>✅</td>
        <td>Integrates retrieval augmented generation techniques with Large Language Models (LLMs) to summarize and reference relevant responses, facilitating access to complex experiment information and promoting collaborative research.</td>
      </tr>
      <tr>
        <td><a href="https://arxiv.org/pdf/2404.16130">Graph RAG Approach for Question Answering</a></td>
        <td>A method combining retrieval-augmented generation (RAG) and query-focused summarization (QFS) for question answering over private text corpora. Utilizes large language models (LLMs) to build a graph-based text index and pre-generate community summaries for closely-related entities, leading to improved scalability and performance compared to traditional RAG and QFS methods.</td>
        <td>
          <details>
            <summary>Explore pros/cons</summary>
            <b>Pros:</b>
            <ul>
              <li>Scales with the generality of user questions and the quantity of source text.</li>
              <li>Improves comprehensiveness and diversity of generated answers.</li>
              <li>Provides a solution for global sensemaking questions over large datasets.</li>
            </ul>
            <b>Cons:</b>
            <ul>
              <li>Complexity in implementation and integration.</li>
              <li>Requires significant computational resources for large-scale text indexing.</li>
            </ul>
          </details>
        </td>
        <td>
          <details>
            <summary>Explore use-cases</summary>
            <ul>
              <li>Question answering over private text corpora.</li>
              <li>Sensemaking tasks over large datasets.</li>
            </ul>
          </details>
        </td>
        <td>
          <ul>
            <li>Large Language Models (LLMs)</li>
            <li>Python-based implementation forthcoming at <a href="https://github.com/GraphRAG">Graph RAG GitHub</a></li>
          </ul>
        </td>
        <td>✅</td>
        <td>Combines RAG and QFS methods to improve question answering over private text corpora. Provides scalability and performance improvements over traditional approaches, demonstrated through substantial improvements in answer comprehensiveness and diversity.</td>
      </tr>
    </tbody>
  </table>
</details>

## About Us
Learn more about our team [here](https://docs.google.com/presentation/d/1SBlGVdz81NUZDpsXQ5xZXaC7oOi-OAkKURFXmy4CcT8/edit?usp=sharing)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- MARKDOWN LINKS & IMAGES -->
[contributors-shield]: https://img.shields.io/github/contributors/JNikolo/CCNY-Senior-Design.svg?style=for-the-badge
[contributors-url]: https://github.com/JNikolo/CCNY-Senior-Design/graphs/contributors
[license-url]: https://github.com/JNikolo/CCNY-Senior-Design/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/linkedin_username
[Python.org]: https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white
[Python-url]: https://python.org/
[TensorFlow.org]: https://img.shields.io/badge/TensorFlow-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white
[TensorFlow-url]: https://tensorflow.org/
[Streamlit.app]: https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white
[Streamlit-url]: https://streamlit.io/
[Flask.com]: https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white
[Flask-url]: https://flask.palletsprojects.com/

