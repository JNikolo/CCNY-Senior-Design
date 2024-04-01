# CCNY-Senior-Design
This repository is for the Senior Design class Project. 

# Net Design 

## Project Idea
### RAG Playground
This project aims to create an interactive platform designed for hands-on exploration of Retrieval-Augmented Generation (RAG) models. It offers users a user-friendly interface to experiment with RAG in real-time, allowing for parameter customization, enhanced visualization, integration with external APIs, performance metrics, and accessibility features.  
![image](https://github.com/JNikolo/CCNY-Senior-Design/assets/125705821/78912715-a637-4ccb-bc38-63d021181509)


**Key Features:**
1. Enhanced Visualization: Incorporate advanced visualization tools to provide users with an intuitive understanding of how RAG models performed. Visualize answer correctness histogram, document embedding similarity map.

2. Integration with External Data: Allow integration with external datasets to expand the capabilities of the application. Users can access specialized databases or domain-specific knowledge sources to enhance the retrieval process and generate more accurate responses.

3. Customization Options: Provide users with the ability to customize various parameters of the RAG models, such as the retrieval strategy, generation settings, and input data sources. This flexibility enables users to tailor the platform to their specific use cases and preferences.

4. Performance Metrics: Include performance metrics and analytics to evaluate the effectiveness of the RAG models. Measure response times, accuracy, and relevance of the generated responses to provide users with valuable insights into the model's performance and capabilities.

5. Improving RAG: Helps users with recommendations based on the performance metrics results using a fine-tuned LLM. The user tries again and the previous results are shown with the current ones.
     
---
<!--
#### RAG Literacy

- [**Knowledge Retrieval Via The OpenAI Playground**](https://cobusgreyling.medium.com/knowledge-retrieval-via-the-openai-playground-8b04682ebe37)  
The article discusses the introduction of a Retrieval Augmentation tool in the new OpenAI playground under Assistants Mode. It examines the significance of this tool in the context of Retrieval-Augmented Generation (RAG) and its impact on the accessibility and functionality of the OpenAI Playground. The feature allows users to upload documents, which are automatically processed and referenced by the assistant when needed, aiming to augment the assistant's knowledge beyond pre-trained models. The article explores the workings of the Retrieval feature, including its processing steps and techniques for content retrieval. It highlights the potential benefits and challenges of the tool, emphasizing the need for flexibility, control over document handling, and insight into the retrieval process for effective application management. 

---

- [**How to improve RAG(Retrieval Augmented Generation) performance**](https://medium.com/@sthanikamsanthosh1994/how-to-improve-rag-retrieval-augmented-generation-performance-2a42303117f8#:~:text=Clean%20the%20Data%3A&text=The%20success%20of%20your%20RAG,interventions%20to%20more%20advanced%20techniques.)  
The article provides an in-depth exploration of the Retrieval Augmentation Generation (RAG) framework, which enhances Language Models (LLMs) by incorporating real-time information retrieval and generation processes to respond accurately to user queries. It outlines the two main phases of RAG: retrieval and generation, and discusses various strategies to refine each phase for optimal performance. These strategies include data cleaning, chunking techniques, custom embedding models, reranking, query transformation, and prompt tuning. The article emphasizes the importance of refining RAG processes to handle complex scenarios and specific domains effectively.

---

- [**Enhancing Large Language Model Performance To Answer Questions and Extract Information More Accurately**](https://arxiv.org/pdf/2402.01722.pdf)  
The paper explores the challenges faced by Large Language Models (LLMs) in generating accurate responses to questions and proposes a fine-tuning approach to address these issues. It discusses the utilization of feedback and examples to refine models continuously, employing metrics such as cosine similarity, LLM evaluation, and Rouge-L scores for evaluation. Benchmarking on financial datasets like FinanceBench and RAG Instruct Benchmark Tester Dataset, the study demonstrates the effectiveness of fine-tuned models compared to zero-shot LLMs, particularly in question and answering tasks. Additionally, the paper highlights the combination of fine-tuning with Retrieval Augmented Generation (RAG) as a promising approach to enhancing response accuracy further.

---

- [**Retrieval-Augmented Generation for Large Language Models: A Survey**](https://arxiv.org/pdf/2312.10997.pdf)  
The paper delves into the challenges faced by Large Language Models (LLMs), such as hallucination and outdated knowledge, and highlights Retrieval-Augmented Generation (RAG) as a promising solution. RAG integrates knowledge from external databases, enhancing model accuracy and credibility, particularly for knowledge-intensive tasks. It provides continuous updates and integration of domain-specific information. The paper reviews the progression of RAG paradigms, from Naive to Advanced and Modular RAG, examining the retrieval, generation, and augmentation techniques. It discusses state-of-the-art technologies in each component, along with metrics and benchmarks for evaluating RAG models. The paper concludes by outlining future research directions, including addressing challenges, expanding multi-modalities, and advancing the RAG infrastructure and ecosystem.

---

- [**Personalized RAG Engine for Low- Latency & High-Performance**](https://medium.com/@bijit211987/personalized-rag-engine-for-low-latency-high-performance-bb07b827a5f7)  
The article explores the construction of a Retrieval-Augmented Generation (RAG) system tailored to personalized data, which combines neural retrieval with text generation models for low latency access to vast personal datasets. It provides a comprehensive guide covering architecture, data ingestion, neural search index optimization, encoding strategies, retrieval model training, re-ranking, text generation model pre-training, query parsing, RAG model integration, user personalization, scalability, and testing & validation. The RAG pipeline enables natural language querying across personal data, resulting in accurate and responsive responses, with significant gains in performance metrics. The article emphasizes the importance of personalization in improving alignment with user language patterns and mental models. Additionally, it discusses scalability considerations and testing methodologies, concluding that RAG systems offer transformative access to personal information and anticipate further advancements in the field.
-->
## Ideas collection (Background)

| Ideas | Summary |
|-------|---------|
| [fastRAG](https://github.com/IntelLabs/fastRAG) | <details><summary>**Overview**</summary>FastRAG is a research framework developed by Intel Labs, designed for creating efficient and optimized retrieval-augmented generative (RAG) pipelines. It includes LLM backends like Intel Gaudi Accelerators, ONNX Runtime, and Llama-CPP for running RAG pipelines efficiently, along with RAG-efficient components like Colbert for token-based late interaction, Fusion-in-Decoder (FiD) for generative multi-document encoding and decoding, and REPLUG for improved multi-document decoding.</details> <details><summary>**Components/Techniques**</summary><ul> <li><details><summary><b>REPLUG (Retrieve and Plug):</b></summary><ul><li>Retrieval-augmented LM method.</li><li>Documents are retrieved and plugged into the input using ensembling.</li><li>Works with any LM without fine-tuning.</li><li>Enables processing a larger number of retrieved documents without limiting to the LM context window.</li></ul> </details></li><li><details><summary><b>ColBERT v2 with PLAID Engine:</b></summary><ul><li>Dense retriever encoding documents into representative vectors.</li><li>ColBERT v2 reduces index size using vector quantization.</li><li>PLAID Engine improves latency times for ColBERT-based indexes.</li></ul></details></li><li><details><summary><b>PLAID Requirements:</b></summary><ul><li>Specifies GPU requirements for PLAID Engine usage.</li></ul></details></li><li><details><summary><b>fastRAG running LLMs with Habana Gaudi (DL1) and Gaudi 2:</b></summary><ul><li>Support for running LLMs on Intel Habana Gaudi accelerators.</li><li>Instructions for configuring the invocation layer of PromptModel for Gaudi backend.</li></ul></details></li><li><details><summary><b>fastRAG running LLMs with ONNX-runtime:</b></summary><ul><li>Method for running quantized LLMs efficiently on CPUs using ONNX-runtime.</li><li>Includes instructions for quantizing the model and loading the quantized model.</li></ul></details></li><li><details><summary><b>fastRAG Running RAG Pipelines with LLMs on a Llama CPP backend:</b></summary><ul><li>Method for running LLMs effectively on CPUs using llama-cpp.</li><li>Installation instructions and loading the model using LlamaCPPInvocationLayer.</li></ul></li><li><details><summary><b>Optimized Embedding Models:</b></summary><ul><li>Introduces quantized int8 models for bi-encoder rankers and retrievers.</li><li>Emphasizes low latency and high throughput.</li><li>Instructions for optimization and usage with the optimum-intel framework.</li></ul></details></li><li><details><summary><b>Fusion-In-Decoder (FiD):</b></summary><ul><li>Transformer-based generative model based on the T5 architecture.</li><li>Used for answering questions given relevant information.</li><li>Provides implementation as an invocation layer for LLMs and a training script for fine-tuning FiD models.</li></ul></li></ul></details> <details><summary>**Tools/Technologies/Libraries**</summary><ul><li>farm-haystack</li><li>transformers</li><li>datasets</li><li>evaluate</li><li>pandas</li><li>nltk</li><li>tqdm</li><li>numba</li><li>openpyxl</li><li>numpy</li><li>protobuf</li><li>ujson</li><li>accelerate</li><li>fastapi</li><li>uvicorn</li><li>Pillow</li><li>beir</li><li>kilt</li><li>streamlit</li><li>st-annotated-text</li><li>matplotlib</li><li>streamlit_chat</li><li>colbert-ai</li><li>faiss-gpu</li><li>faiss-cpu</li><li>qdrant-haystack</li><li>spacy</li><li>pyvis</li><li>networkx</li><li>opencv-python-headless</li><li>intel-extension-for-transformers</li><li>neural_compressor</li><li>pytrec_eval</li><li>torch</li><li>onnx</li><li>onnxruntime</li><li>onnxruntime-extensions</li><li>sentence-transformers</li><li>intel-extension-for-pytorch</li><li>optimum</li><li>llama-cpp-python</li><li>flake8</li></ul></details> |
| [Haystack](https://github.com/deepset-ai/haystack) | <details><summary>**Overview**</summary>The goal of the LLM orchestration framework Haystack by deepset.ai is to create LLM applications that are adaptable and ready for production. It facilitates the creation of pipelines for data interaction by joining different parts, such as file converters, vector databases, and models. It leverages textual data, including structured and unstructured documents, for retrieval and processing, making it perfect for RAG, question answering, semantic search, and chatbots. Although providing flexibility and extensive NLP capabilities, system complexity, data quality reliance, and the requirement for integration with current technologies may present implementation issues.</details> <details><summary>**Components/Techniques**</summary><ul><li><details><summary>**Components**</summary><ul><li><b>Generators:</b> Responsible for generating text responses, divided into chat and non-chat types based on conversational contexts.</li><li><b>Retrievers:</b> Select documents matching user queries from Document Stores.</li></ul></details></li><li> <details><summary>**Document Stores**</summary>An object storing documents in Haystack, serving as an interface to a storage database. Various components can interact with it to read or write documents.</details></li><li> <details><summary>**Data Classes**</summary><ul><li><b>Document class:</b> Contains information carried through the pipeline, such as text, metadata, tables, or binary data.</li><li><b>Answer class:</b> Holds generated answers, originating queries, and metadata.</li></ul></details></li><li> <details><summary>**Pipelines**</summary>Customizable systems created by combining components, document stores, and integrations. Highly flexible, allowing various flows, standalone components, loops, and connections. Pipelines can be saved in convenient formats for reuse or sharing.</details></li><li> <details><summary>**Optimization**</summary> <ul><li><details><summary><strong>What is Model-Based Evaluation</strong></summary><p>Model-based evaluation in Haystack utilizes a language model to assess the results of a Pipeline, typically without requiring labels for outputs. It's commonly used with Retrieval-Augmented Generative (RAG) Pipelines but can be applied to any Pipeline. Haystack currently supports end-to-end model-based evaluation of complete RAG Pipelines.</p></details></li><li> <details><summary><strong>Using LLMs for Evaluation</strong></summary><p>A common strategy involves using Language Models (LLMs) like OpenAI's GPT models as evaluator models, often referred to as golden models. GPT-4 is frequently used for this purpose. This method offers flexibility in defining evaluation metrics, such as faithfulness and context relevance, through well-crafted prompts.</p></details> </li><li><details><summary><strong>Using Small Cross-Encoder Models</strong></summary><p>In addition to LLMs, small cross-encoder models can be used for evaluation, calculating semantic answer similarity, for example. These models are faster and cheaper but less flexible in terms of evaluation aspects compared to LLMs.</p></details></li><li> <details><summary><strong>Model-Based Evaluation Pipelines</strong></summary><p>Model-based evaluation in Haystack can be performed independently by creating and running an evaluation Pipeline, or by adding an evaluator component to the end of a RAG Pipeline. The latter approach allows both RAG Pipeline execution and evaluation in a single pipeline.run() call.</p></details></li><li> <details><summary><strong>Evaluation Framework Integrations</strong></summary><p>Haystack integrates with evaluation frameworks like DeepEval, UpTrain, and Ragas, providing Evaluator components for each framework: RagasEvaluator, DeepEvalEvaluator, and UpTrainEvaluator.</p></details></li></ul></details></ul> </details> <details><summary>**Tools/Technologies/Libraries**</summary> <ul><li>Hatchling (build system)</li><li>Pandas</li><li>Haystack-bm25</li><li>Tqdm</li><li>Tenacity</li><li>Lazy-imports</li><li>Openai</li><li>Jinja2</li><li>Posthog</li><li>Pyyaml</li><li>More-itertools</li><li>Networkx</li><li>Typing_extensions</li><li>Boilerpy3</li><li>Requests</li><li>Numpy</li><li>Python-dateutil</li><li>Pre-commit</li><li>Mypy</li><li>Pytest</li><li>Pytest-cov</li><li>Pytest-custom_exit_code</li><li>Pytest-asyncio</li><li>Pytest-rerunfailures</li><li>Responses</li><li>Tox</li><li>Coverage</li><li>Python-multipart</li><li>Psutil</li><li>Pylint</li><li>Ruff</li><li>Toml</li><li>Reno</li><li>Dulwich</li><li>Black</li><li>Transformers</li><li>Huggingface_hub</li><li>Spacy</li><li>Spacy-curated-transformers</li><li>En-core-web-trf</li><li>Pypdf</li><li>Markdown-it-py</li><li>Mdit_plain</li><li>Tika</li><li>Azure-ai-formrecognizer</li><li>Langdetect</li><li>Sentence-transformers</li><li>Openai-whisper</li><li>Chroma-haystack</li><li>Jsonref</li><li>Openapi3</li><li>Jsonschema</li><li>Opentelemetry-sdk</li><li>Ddtrace</li><li>Structlog</li><li>Isort</li><li>Pyproject-parser</li><li>Haystack-pydoc-tools</li></ul></details>|
| [RAGs](https://github.com/run-llama/rags) | <details><summary>**Overview**</summary>RAGs is a Streamlit app inspired by OpenAI's GPTs, allowing users to create a RAG pipeline using natural language. Users can describe their task and specify parameters such as the number of documents to retrieve. The app provides a config view where users can adjust parameters like top-k and summarization. Finally, users can query the RAG agent with their questions over the specified data source.</details> <details><summary>**Components/Techniques**</summary> <ul><li><details><summary>Home Page</summary>This is the section where you build a RAG pipeline by instructing the "builder agent". Typically to setup a RAG pipeline you need the following components:<ul><li>Describe the dataset. Currently they support either a single local file or a web page</li><li>Describe the task. Concretely this description will be used to initialize the "system prompt" of the LLM powering the RAG pipeline.</li><li>Define the typical parameters for a RAG setup. See the below section for the list of parameters.</li></ul></details></li><li><details><summary>RAG Config</summary><ul><li>This section contains the RAG parameters, generated by the "builder agent" in the previous section. In this section, you have a UI showcasing the generated parameters and have full freedom to manually edit/change them as necessary.</li><li>Currently the set of parameters is as follows:</li><ul><li>System Prompt</li><li>Include Summarization: whether to also add a summarization tool (instead of only doing top-k retrieval.)</li><li>Top-K</li><li>Chunk Size</li><li>Embed Model</li><li>LLM</li></ul><li>If you manually change parameters, you can press the "Update Agent" button in order to update the agent.</li><li>If you don't see the `Update Agent` button, that's because you haven't created the agent yet. Please go to the previous "Home" page and complete the setup process.</li><li>We can always add more parameters to make this more "advanced" 🛠️, but thought this would be a good place to start.</li></ul></details></li><li><details><summary>Generated RAG Agent</summary><ul><li>Once your RAG agent is created, you have access to this page.</li><li>This is a standard chatbot interface where you can query the RAG agent and it will answer questions over your data.</li><li>It will be able to pick the right RAG tools (either top-k vector search or optionally summarization) in order to fulfill the query.</li></ul></details></li><li><details><summary>Supported LLMs and Embeddings</summary><ul><li><details><summary>Builder Agent</summary><ul><li>By default, the builder agent uses OpenAI, specified in the <code>core/builder_config.py</code> file.</li><li>Customization to any desired LLM is possible, with an example provided for Anthropic.</li><li>Note: GPT-4 variants are recommended for reliable results in agent construction.</li></ul></details></li><li><details><summary>Generated RAG Agent</summary><ul><li>Configuration can be set through natural language or manually for both the embedding model and LLM.</li><li>LLMs supported:<ul><li>OpenAI: ID format is "openai:<model_name>", e.g., "openai:gpt-4-1106-preview".</li><li>Anthropic: ID format is "anthropic:<model_name>", e.g., "anthropic:claude-2".</li><li>Replicate: ID format is "replicate:<model_name>".</li><li>HuggingFace: ID format is "local:<model_name>", e.g., "local:BAAI/bge-small-en".</li></ul></li><li>Embeddings: Supports text-embedding-ada-002 by default, also supports Hugging Face models. Hugging Face models can be used by prefixing "local", e.g., "local:BAAI/bge-small-en".</li></ul></li></ul></details></li></ul></details><details><summary>**Tools/Technologies/Libraries**</summary><ul><li>streamlit</li><li>streamlit-pills</li><li>llama-index</li><li>llama-hub</li><li>langchain</li><li>pypdf</li><li>clip</li><li>typing-inspect</li><li>typing_extensions</li><li>types-requests</li><li>black</li><li>isort</li><li>pytest-asyncio</li><li>ruff</li><li>mypy</li><li>referencing</li><li>jsonschema-specifications</li><li>poetry</li><li>poetry-core</li></ul> |
| [RAGArch](https://github.com/AI-ANK/RAGArch) | <details><summary>**Overview**</summary>RAGArch is a streamlit application that allows users to test and compare RAG pipelines by giving them the option to choose different parameters such as the LLM, embeddings, and vector store</details> <details><summary>**Components/Techniques**</summary>The application not only allows users to play with different settings with their own documents in real time, but also provides the option to export the Python code that corresponds to the pipeline the users configures so that they can put it into another project. The demo utilizes streamlit and LlamaindexThe LLM's that are included in this demo are Gemini Pro, Cohere, GPT 3.5, and GPT 4. The embeddings included are: <ul><li>"BAAI/bge-small-en-v1.5"</li><li>"WhereIsAI/UAE-Large-V1"</li><li>"BAAI/bge-large-en-v1.5"</li><li>"khoa-klaytn/bge-small-en-v1.5-angle"</li><li>"BAAI/bge-base-en-v1.5"</li><li>"llmrails/ember-v1"</li><li>"jamesgpt1/sf_model_e5"</li><li>"thenlper/gte-large"</li><li>"infgrad/stella-base-en-v2"</li><li>"thenlper/gte-base"</li></lu> Finally for Vectors Stores there is Simple, Pinecone, and Qdrant</details> |

## Datasets

| Datasets | Summary |
|-----------------|-----------------|
| [RAG Dataset 12000](https://huggingface.co/datasets/neural-bridge/rag-dataset-12000) |  |
| [Dataset Card for RAG-Instruct-Benchmark-Tester](https://huggingface.co/datasets/llmware/rag_instruct_benchmark_tester) | |
| [RAGas Evaluation](https://huggingface.co/datasets/shayorshay/ragas-eval) | |
| [Amnesty QA](https://huggingface.co/datasets/explodinggradients/amnesty_qa) | |
| []() | |
| []() | |

<!--
**Dataset Summary:**
The RAG-Instruct-Benchmark-Tester dataset is a benchmarking test dataset specifically designed for retrieval augmented generation (RAG) use cases in enterprise settings, particularly in financial services and legal domains. It consists of 200 questions with context passages sourced from various retrieval scenarios such as financial news, earnings releases, contracts, invoices, technical articles, general news, and short texts. The dataset is segmented into different categories for benchmarking evaluation, including core Q&A, not found classification, boolean (yes/no), basic math, complex Q&A, and summary questions.

**Representative Questions:**
The dataset includes a variety of representative questions covering topics such as payment terms, financial performance, legal agreements, economic forecasts, stock market data, and mathematical calculations. These questions aim to assess different skills and capabilities of models in understanding and responding to diverse query types.

**Languages:**
The dataset is in English.

**Dataset Structure:**
It comprises 200 JSONL samples with six keys: "query", "context", "answer", "category", "tokens", and "sample_number". Each sample includes information about the question, context passage, answer, category of question, tokenized text, and sample number.

**Personal and Sensitive Information:**
The dataset samples were custom-written for the benchmarking objective, derived from publicly-available sources or originally-created samples. Therefore, they do not contain personal or sensitive information.

**Dataset Card Contact:**
For further information about the dataset project, interested parties can contact Darren Oberst and the llmware team. They are available to provide additional details about the project upon request.




dataset 12000
**Dataset Summary:**
The Retrieval-Augmented Generation (RAG) Dataset 12000 is designed for RAG-optimized models, offering English data built by Neural Bridge AI and released under the Apache license 2.0. It enhances large language models (LLMs) by allowing them to consult external authoritative knowledge bases before generating responses. This approach significantly improves the models' ability to produce relevant, accurate, and context-specific output by extending their capabilities to specialized domains or internal data without retraining.

**Importance of RAG:**
RAG addresses inherent challenges of LLMs such as unpredictability in responses and reliance on potentially outdated training data. By guiding LLMs towards authoritative sources, RAG enhances user trust in AI-powered applications. Benefits include cost-effective implementation, access to current information, improved user trust, and greater control for developers over information retrieval processes.

**Dataset Details:**
The dataset consists of triple-feature entries: "context," "question," and "answer" fields, with 12000 entries. Each data point includes a context obtained from Falcon RefinedWeb, a question related to the context, and an answer generated by GPT-4.

**Languages:**
The dataset text is in English, with the BCP-47 code "en."

**Dataset Structure:**
Data instances contain context, question, and answer fields. An example data point is structured as follows:
```json
{
  "context": "...",
  "question": "...",
  "answer": "..."
}
```

**Data Splits:**
The dataset is split into training and test sets, with 9600 instances for training and 2400 instances for testing.






- [**An Overview on RAG Evaluation**](https://weaviate.io/blog/rag-evaluation)  
The article delves into the evaluation and optimization of Retrieval Augmented Generation (RAG) systems, which enhance Large Language Models (LLMs) with context retrieved from vector databases like Weaviate. Inspired by advancements in using LLMs for evaluation, the authors explore new trends, metrics, and tuning approaches for RAG systems. They discuss the distinctions between RAG and Agent systems and propose methods for managing experimental configurations. The article aims to provide insights into enhancing the performance and effectiveness of RAG applications, particularly in chatbots and question-answering systems.
 
- [**How to Measure the Success of Your RAG-based LLM System**](https://towardsdatascience.com/how-to-measure-the-success-of-your-rag-based-llm-system-874a232b27eb)  
The article explores the significance of Research Augmented Generation (RAG) as a prevalent application of Large Language Models (LLMs) and its increasing adoption by businesses. While individual users often focus on text summarization and generation, businesses recognize the potential of leveraging their data with this technology. The author reflects on personal experiences with LLMs, highlighting text generation as a primary use case. The article aims to delve into the evaluation of RAG systems, rather than offering a guide on building them, by discussing various aspects of assessing their performance and effectiveness.

---

- [**Top Evaluation Metrics for RAG Failures**](https://towardsdatascience.com/top-evaluation-metrics-for-rag-failures-acb27d2a5485)  
The article discusses comprehensive evaluation metrics and approaches for assessing the performance of Large Language Model (LLM) Retrieval Augmented Generation (RAG) systems. It emphasizes the importance of continually evaluating these systems against established metrics to enhance their accuracy, relevance, and timeliness in providing information. Additionally, the article suggests advanced methods for improving RAG, such as re-ranking, metadata attachments, experimentation with embedding models and indexing methods, and implementing techniques like HyDE and Cohere document mode. While these advanced methods may enhance contextual coherence, they require more resources. Utilizing RAG alongside these methods can lead to performance improvements, provided that retrieval and response metrics are monitored and maintained effectively.

---

- [**Evaluating RAG Applications with RAGAs**](https://towardsdatascience.com/evaluating-rag-applications-with-ragas-81d67b0ee31a)  
The article discusses the challenges involved in evaluating Retrieval-Augmented Generation (RAG) pipelines, emphasizing the need to assess both the retriever and generator components separately and together for comprehensive evaluation. It highlights the importance of quantitative evaluation using appropriate metrics and datasets. With the emergence of various approaches for RAG evaluation frameworks, including RAGAs, the article aims to explore how RAG pipelines can be evaluated effectively using these frameworks.

---

- [**Evaluate and Optimize RAG with TruLens (full tutorial)**](https://www.youtube.com/watch?v=ul5huLywzZk&t=13s&ab_channel=JohannesJolkkonen%7CFunktioAI)
The video shows how to get started using TruLens, an evaluation framework for Systematic evaluation, which is the key piece in taking your RAG-systems from just a cool demo into something that's actually useful for real people and businesses. TruLens has been developed by TruEra, a well-established ML-monitoring company.
---

- [**Visualize your RAG Data — Evaluate your Retrieval-Augmented Generation System with Ragas**](https://towardsdatascience.com/visualize-your-rag-data-evaluate-your-retrieval-augmented-generation-system-with-ragas-fc2486308557)  
The article introduces a methodology for evaluating Retrieval-Augmented Generation (RAG) systems using interactive visualization techniques. It outlines steps for building a RAG system, generating evaluation questions, and assessing system performance. The evaluation involves metrics such as answer correctness, which is analyzed in conjunction with question and document embeddings using UMAP-based visualizations. The article demonstrates how to use Renumics Spotlight to visualize and interpret the results, identifying patterns and clusters within the data to gain deeper insights into system behavior. Overall, the approach offers a comprehensive method for evaluating and understanding RAG systems, facilitating informed decision-making in software development.

#### Ideas for actual app

- [**LLM Playground Hands-On Learning | Build and Compare RAG-based Chatbot Responses Side-by-Side**](https://www.youtube.com/watch?v=xIc4IR79ksA&t=406s&ab_channel=DataRobot)  
The video introduces the DataRobot LLM Playground for first-time users. It guides viewers through downloading accompanying zip files to build vector databases and LLM blueprints. Different components like vector databases, system prompts, and LLM models are showcased through side-by-side comparisons of generative outputs. Users are encouraged to experiment with prompts using movie plot summary data, with the platform offering rapid prototyping and project management tools for building Gen AI applications efficiently.

---

- [**How to build your AI ChatBot with NLP in Python**](https://www.analyticsvidhya.com/blog/2021/10/complete-guide-to-build-your-ai-chatbot-with-nlp-in-python/)  
The article introduces readers to the creation of an AI chatbot using Natural Language Processing (NLP) in Python. It outlines the steps involved, from understanding NLP to building a chatbot capable of engaging in real conversations with users. The guide offers hands-on instructions, providing code samples that can be customized to suit individual needs. In the conclusion, it emphasizes the versatility of the provided code samples as building blocks for similar projects and suggests enrolling in an AI and ML Blackbelt Plus Program to further enhance skills. The article highlights the use of speech recognition tools and pre-trained Transformers language models to make the chatbot intelligent.
---
- [**Building Production-Ready RAG Applications: Jerry Liu**](https://www.youtube.com/watch?v=TRjq7t2Ms5I&ab_channel=AIEngineer)  
The video is a recorded talk by Jerry Liu, CEO of LlamaIndex, from the AI Engineer Summit 2023 in San Francisco. Liu discusses how Large Language Models (LLMs) are revolutionizing search, interaction, and content generation, particularly through Retrieval Augmented Generation (RAG) stacks. He emphasizes the challenges of productionizing RAG stacks effectively and highlights core techniques for improving retrieval systems. These techniques include data preparation, vectorization, retrieval strategies, evaluation metrics, fine-tuning, scalability, efficiency, and ethical considerations. Liu shares insights from his experience in ML engineering and AI research, concluding with an invitation to the AI Engineer World's Fair in 2024.

---
- [**Meet RAGxplorer: An interactive AI Tool to Support the Building of Retrieval Augmented Generation (RAG) Applications by Visualizing Document Chunks and the Queries in the Embedding Space**](https://www.marktechpost.com/2024/01/25/meet-ragxplorer-an-interactive-ai-tool-to-support-the-building-of-retrieval-augmented-generation-rag-applications-by-visualizing-document-chunks-and-the-queries-in-the-embedding-space/)  
The article introduces RAGxplorer, an interactive AI tool designed to support the development of Retrieval Augmented Generation (RAG) applications by visualizing document chunks and queries in an embedding space. RAGxplorer breaks documents into smaller, overlapping chunks and converts them into mathematical representations called embeddings. These embeddings are then visualized in a 2D or 3D space, allowing users to assess how well RAG models understand the document. The tool's flexibility in handling various document formats and query expansion techniques enhances its effectiveness in revealing semantic relationships within documents, helping users identify biases, knowledge gaps, and overall model performance. RAGxplorer addresses the challenges of visualizing complex language models, making it a valuable resource for researchers, developers, and practitioners seeking deeper insights into these advanced systems.
-->
## Team Members
- [Jair Ruiz](https://github.com/JNikolo) - Leader
- [Usman Abbas](https://github.com/uscod) - Systems Savvy
- [Evan Perez](https://github.com/evanperez444) - TechSmith

## More About Us
[Know about our team](https://docs.google.com/presentation/d/1SBlGVdz81NUZDpsXQ5xZXaC7oOi-OAkKURFXmy4CcT8/edit?usp=sharing)
