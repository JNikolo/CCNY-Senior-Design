# CCNY-Senior-Design
This repository is for the Senior Design class Project. 

# Net Design 

## Table of Contents
- [Team Members](#team-members)
- [RAG Playground](#rag-playground)
  - [Key Features](#key-features)
- [Project Proposal](#project-proposal)
- [Dataset](#dataset)

-----

## Team Members
- [Jair Ruiz](https://github.com/JNikolo) - Leader
- [Usman Abbas](https://github.com/uscod) - Systems Savvy
- [Evan Perez](https://github.com/evanperez444) - Tech-Smith

-----
## Quick Links
- [Notebooks for training model, data mining, and evaluation](Notebooks/)
- [Code for the full-stack application](RAG_Playground/)

-----

## RAG Playground
This project focuses on building/finetuning a deep learning model to perform abstractive text summarization. Additionally, the project aims to create an interactive platform for hands-on exploration of Retrieval-Augmented Generation (RAG) systems. Users will be able to compare the performance of the standalone model with that of the RAG system in summarization tasks. The platform will feature a user-friendly interface for real-time experimentation with RAG, offering customization of parameters, enhanced visualizations, and detailed performance metrics to facilitate in-depth analysis and understanding.
![image](https://github.com/JNikolo/CCNY-Senior-Design/assets/125705821/6c4abf42-2fba-4084-a32c-974465161a3d)

### Key Features
1. Enhanced Visualization: Incorporate advanced visualization tools to provide users with an intuitive understanding of how RAG models performed. Visualize answer correctness histogram, document embedding similarity map.

2. Abstractive Summarization: Training a deep learning model to perform abstractive summarization of texts.

3. Customization Options: Provide users with the ability to customize various parameters of the RAG models, such as the retrieval strategy, generation settings, and input data sources. This flexibility enables users to tailor the platform to their specific use cases and preferences.

4. Performance Metrics: Include performance metrics and analytics to evaluate the effectiveness of the RAG models. Measure response times, accuracy, and relevance of the generated responses to provide users with valuable insights into the model's performance and capabilities.

5. Performance Comparison: Allowing users to compare the summarization performance of our model against the AI system.
     
---
## Project Proposal

- You can access to our project proposal [here](SD_Propject_Proposal.pdf)  
Note: For a summarized version check the slides of our final presentation [here](SD_Final_presentation.pdf)

## Dataset
This [dataset](https://www.kaggle.com/datasets/snap/amazon-fine-food-reviews) consists of reviews of fine foods from amazon. The data span a period of more than 10 years, including all ~500,000 reviews up to October 2012. Reviews include product and user information, ratings, and a plain text review. It also includes reviews from all other Amazon categories.
- Provides Food Reviews Summaries in ~10 words or less
- Data fields
  - ID
  - ASIN (Amazon product ID)
  - Text (Food Review)
  - Summary 
- Splits
  - Train: 314,573
  - Validation: 78,644
Entry sample:
```
{
  "id": 456
  "Text": "These cookies are absolutely delicious! They are crispy, not too sweet, and have a nice buttery flavor. I can't stop eating them. Will definitely buy again!",
  "summary": "Best cookies ever!",
  "asin": "B01N6P0FHH",
}
```


----

## About Us
[Know about our team](https://docs.google.com/presentation/d/1SBlGVdz81NUZDpsXQ5xZXaC7oOi-OAkKURFXmy4CcT8/edit?usp=sharing)
