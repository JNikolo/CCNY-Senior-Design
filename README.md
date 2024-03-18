# CCNY-Senior-Design
This repository is for the Senior Design class Project. 

# Net Design 

## Project Idea
### RAG Playground
This project aims to create an interactive platform designed for hands-on exploration of Retrieval-Augmented Generation (RAG) models. It offers users a user-friendly interface to experiment with RAG in real-time, allowing for parameter customization, feedback mechanisms, educational resources, integration with external APIs, performance metrics, and accessibility features.  

**Key Features:**
1. Enhanced Visualization: Incorporate advanced visualization tools to provide users with an intuitive understanding of how RAG models work. Visualize the retrieval process, attention mechanisms, and response generation to enhance the learning experience.

2. Feedback Mechanism: Implement a feedback mechanism where users can provide input on the quality and relevance of the generated responses. This feedback will be used to fine-tune the RAG models and improve their performance over time.

3. Educational Resources: Include tutorials, documentation, and case studies to help users understand the underlying concepts of RAG models. Offer interactive lessons and walkthroughs to facilitate learning and experimentation.

4. Integration with External APIs: Allow integration with external APIs or datasets to expand the capabilities of RAG Explorer. Users can access specialized databases or domain-specific knowledge sources to enhance the retrieval process and generate more accurate responses.

5. Customization Options: Provide users with the ability to customize various parameters of the RAG models, such as the retrieval strategy, generation settings, and input data sources. This flexibility enables users to tailor the platform to their specific use cases and preferences.

6. Performance Metrics: Include performance metrics and analytics to evaluate the effectiveness of the RAG models. Measure response times, accuracy, and relevance of the generated responses to provide users with valuable insights into the model's performance and capabilities.

7. Community Engagement: Foster a community around RAG Explorer by hosting forums, discussion boards, and virtual events where users can share ideas, ask questions, and collaborate on projects together. Encourage knowledge sharing and collaboration among users.

8. Accessibility: Ensure that RAG Explorer is accessible to users with different levels of expertise and diverse backgrounds. Provide user-friendly interfaces, clear documentation, and support for multiple languages to make the platform inclusive and accessible to all users.

### Background
- [**How to build your AI ChatBot with NLP in Python**](https://www.analyticsvidhya.com/blog/2021/10/complete-guide-to-build-your-ai-chatbot-with-nlp-in-python/)  
The article introduces readers to the creation of an AI chatbot using Natural Language Processing (NLP) in Python. It outlines the steps involved, from understanding NLP to building a chatbot capable of engaging in real conversations with users. The guide offers hands-on instructions, providing code samples that can be customized to suit individual needs. In the conclusion, it emphasizes the versatility of the provided code samples as building blocks for similar projects and suggests enrolling in an AI and ML Blackbelt Plus Program to further enhance skills. The article highlights the use of speech recognition tools and pre-trained Transformers language models to make the chatbot intelligent.

---

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

---

- [**An Overview on RAG Evaluation**](https://weaviate.io/blog/rag-evaluation)  
The article delves into the evaluation and optimization of Retrieval Augmented Generation (RAG) systems, which enhance Large Language Models (LLMs) with context retrieved from vector databases like Weaviate. Inspired by advancements in using LLMs for evaluation, the authors explore new trends, metrics, and tuning approaches for RAG systems. They discuss the distinctions between RAG and Agent systems and propose methods for managing experimental configurations. The article aims to provide insights into enhancing the performance and effectiveness of RAG applications, particularly in chatbots and question-answering systems.

---

- [**How to Measure the Success of Your RAG-based LLM System**](https://towardsdatascience.com/how-to-measure-the-success-of-your-rag-based-llm-system-874a232b27eb)  
The article explores the significance of Research Augmented Generation (RAG) as a prevalent application of Large Language Models (LLMs) and its increasing adoption by businesses. While individual users often focus on text summarization and generation, businesses recognize the potential of leveraging their data with this technology. The author reflects on personal experiences with LLMs, highlighting text generation as a primary use case. The article aims to delve into the evaluation of RAG systems, rather than offering a guide on building them, by discussing various aspects of assessing their performance and effectiveness.

---

- [**Top Evaluation Metrics for RAG Failures**](https://towardsdatascience.com/top-evaluation-metrics-for-rag-failures-acb27d2a5485)  
The article discusses comprehensive evaluation metrics and approaches for assessing the performance of Large Language Model (LLM) Retrieval Augmented Generation (RAG) systems. It emphasizes the importance of continually evaluating these systems against established metrics to enhance their accuracy, relevance, and timeliness in providing information. Additionally, the article suggests advanced methods for improving RAG, such as re-ranking, metadata attachments, experimentation with embedding models and indexing methods, and implementing techniques like HyDE and Cohere document mode. While these advanced methods may enhance contextual coherence, they require more resources. Utilizing RAG alongside these methods can lead to performance improvements, provided that retrieval and response metrics are monitored and maintained effectively.

---

- [**Evaluating RAG Applications with RAGAs**](https://towardsdatascience.com/evaluating-rag-applications-with-ragas-81d67b0ee31a)  
The article discusses the challenges involved in evaluating Retrieval-Augmented Generation (RAG) pipelines, emphasizing the need to assess both the retriever and generator components separately and together for comprehensive evaluation. It highlights the importance of quantitative evaluation using appropriate metrics and datasets. With the emergence of various approaches for RAG evaluation frameworks, including RAGAs, the article aims to explore how RAG pipelines can be evaluated effectively using these frameworks.

## Team Members
- [Jair Ruiz](https://github.com/JNikolo) - Leader
- [Usman Abbas](https://github.com/uscod) - Systems Savvy
- [Evan Perez](https://github.com/evanperez444) - TechSmith

## More About Us
[Know about our team](https://docs.google.com/presentation/d/1SBlGVdz81NUZDpsXQ5xZXaC7oOi-OAkKURFXmy4CcT8/edit?usp=sharing)
