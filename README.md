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
| [fastRAG](https://github.com/IntelLabs/fastRAG) | <details><summary>**Overview**</summary>FastRAG is a research framework developed by Intel Labs, designed for creating efficient and optimized retrieval-augmented generative (RAG) pipelines. It includes LLM backends like Intel Gaudi Accelerators, ONNX Runtime, and Llama-CPP for running RAG pipelines efficiently, along with RAG-efficient components like Colbert for token-based late interaction, Fusion-in-Decoder (FiD) for generative multi-document encoding and decoding, and REPLUG for improved multi-document decoding.</details> <details><summary>**Components/Techniques**</summary><ul> <li><details><summary><b>REPLUG (Retrieve and Plug):</b></summary><ul><li>Retrieval-augmented LM method.</li><li>Documents are retrieved and plugged into the input using ensembling.</li><li>Works with any LM without fine-tuning.</li><li>Enables processing a larger number of retrieved documents without limiting to the LM context window.</li></ul> </details></li><li><details><summary><b>ColBERT v2 with PLAID Engine:</b></summary><ul><li>Dense retriever encoding documents into representative vectors.</li><li>ColBERT v2 reduces index size using vector quantization.</li><li>PLAID Engine improves latency times for ColBERT-based indexes.</li></ul></details></li><li><details><summary><b>PLAID Requirements:</b></summary><ul><li>Specifies GPU requirements for PLAID Engine usage.</li></ul></details></li><li><details><summary><b>fastRAG running LLMs with Habana Gaudi (DL1) and Gaudi 2:</b></summary><ul><li>Support for running LLMs on Intel Habana Gaudi accelerators.</li><li>Instructions for configuring the invocation layer of PromptModel for Gaudi backend.</li></ul></details></li><li><details><summary><b>fastRAG running LLMs with ONNX-runtime:</b></summary><ul><li>Method for running quantized LLMs efficiently on CPUs using ONNX-runtime.</li><li>Includes instructions for quantizing the model and loading the quantized model.</li></ul></details></li><li><details><summary><b>fastRAG Running RAG Pipelines with LLMs on a Llama CPP backend:</b></summary><ul><li>Method for running LLMs effectively on CPUs using llama-cpp.</li><li>Installation instructions and loading the model using LlamaCPPInvocationLayer.</li></ul></li><li><details><summary><b>Optimized Embedding Models:</b></summary><ul><li>Introduces quantized int8 models for bi-encoder rankers and retrievers.</li><li>Emphasizes low latency and high throughput.</li><li>Instructions for optimization and usage with the optimum-intel framework.</li></ul></details></li><li><details><summary><b>Fusion-In-Decoder (FiD):</b></summary><ul><li>Transformer-based generative model based on the T5 architecture.</li><li>Used for answering questions given relevant information.</li><li>Provides implementation as an invocation layer for LLMs and a training script for fine-tuning FiD models.</li></ul></li></ul></details> <details><summary>**Limitations**</summary>One limitation of FastRAG is the dependency on the quality and structure of the underlying data for performance enhancements. Poorly structured or low-quality data sources may limit the performance enhancements offered by FastRAG. </details> |
| [Haystack](https://github.com/deepset-ai/haystack) | <details><summary>**Overview**</summary>The goal of the LLM orchestration framework Haystack by deepset.ai is to create LLM applications that are adaptable and ready for production. It facilitates the creation of pipelines for data interaction by joining different parts, such as file converters, vector databases, and models. It leverages textual data, including structured and unstructured documents, for retrieval and processing, making it perfect for RAG, question answering, semantic search, and chatbots. Although providing flexibility and extensive NLP capabilities, system complexity, data quality reliance, and the requirement for integration with current technologies may present implementation issues.</details> <details><summary>**Components/Techniques**</summary> <details><summary>**Components**</summary><ul><li><b>Generators:</b> Responsible for generating text responses, divided into chat and non-chat types based on conversational contexts.</li><li><b>Retrievers:</b> Select documents matching user queries from Document Stores.</li></ul></details> <details><summary>**Document Stores**</summary>An object storing documents in Haystack, serving as an interface to a storage database. Various components can interact with it to read or write documents.</details> <details><summary>**Data Classes**</summary><ul><li><b>Document class:</b> Contains information carried through the pipeline, such as text, metadata, tables, or binary data.</li><li><b>Answer class:</b> Holds generated answers, originating queries, and metadata.</li></ul></details> <details><summary>**Pipelines**</summary>Customizable systems created by combining components, document stores, and integrations. Highly flexible, allowing various flows, standalone components, loops, and connections. Pipelines can be saved in convenient formats for reuse or sharing.</details> </details> <details><summary>**Limitations**</summary> </details> |
| [RAGs](https://github.com/run-llama/rags) | <details><summary>**Overview**</summary>Details for RAGs...</details> <details><summary>**Components/Techniques**</summary></details> <details><summary>**Limitations**</summary> </details>  |
| [RAGArch](https://github.com/AI-ANK/RAGArch) | <details><summary>**Overview**</summary>Details for RAGArch...</details> <details><summary>**Components/Techniques**</summary></details> <details><summary>**Limitations**</summary> </details> |

## Datasets

| Datasets | Summary |
|-----------------|-----------------|
| | |
| | |
<!--
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
