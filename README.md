# CCNY-Senior-Design
This repository is for the Senior Design class Project. 

# Net Design 

## Table of Contents
- [Team Members](#team-members)
- [RAG Playground](#rag-playground)
  - [Key Features](#key-features)
- [Project Proposal](#project-proposal)
  - [Dataset](#dataset)
  - [Project Plan](#project-plan)
  - [Project updates](#project-updates)
- [About us](#about-us)

-----

## Team Members
- [Jair Ruiz](https://github.com/JNikolo) - Leader
- [Usman Abbas](https://github.com/uscod) - Systems Savvy
- [Evan Perez](https://github.com/evanperez444) - Tech-Smith

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

### Dataset
The [CNN/Daily-Mail News Dataset](https://huggingface.co/datasets/ccdv/cnn_dailymail) is a very popular option for Text summarization purposes, and that's why we decided to go with it. It has almost ~300k entries in total, only based on a variety of topics from CNN and Dailymail News. It is composed of three features:
- id: An encrypted string of the URL where the news was retrieved
- article: The main content. The piece of data that authors describe all the information.
- highlights: It is where authors try to encapsulate the article information. This will be the reference summary.
Entry sample:
```
{'id': '0054d6d30dbcad772e20b22771153a2a9cbeaf62',
 'article': '(CNN) -- An American woman died aboard a cruise ship that docked at Rio de Janeiro on Tuesday, the same ship on which 86 passengers previously fell ill, according to the state-run Brazilian news agency, Agencia Brasil. The American tourist died aboard the MS Veendam, owned by cruise operator Holland America. Federal Police told Agencia Brasil that forensic doctors were investigating her death. The ship's doctors told police that the woman was elderly and suffered from diabetes and hypertension, according the agency. The other passengers came down with diarrhea prior to her death during an earlier part of the trip, the ship's doctors said. The Veendam left New York 36 days ago for a South America tour.'
 'highlights': 'The elderly woman suffered from diabetes and hypertension, ship's doctors say .\nPreviously, 86 passengers had fallen ill on the ship, Agencia Brasil says .'}
```

### Project Updates
- **09/16/2024**: [Slides](https://docs.google.com/presentation/d/1zdITAq-Jup3Cn-_ZQrCusIorHMXZGKbc2iP00UaLSrc/edit?usp=drivesdk)
- **09/30/2024**: Added Notebooks of data mining and data pre-processing [here](./Notebooks/README.md)

### Project Plan
This Plan considers Week 1 starting on Monday, September 2nd 2024, and Week 15 ending on Wednesday, December 11th 2024.
| Week | Tasks | Deliverables | Roles |
|------|------|------|------|
| 1    | <ul><li>Refine project plan.</li><li>Decide final environments for training and development</li><li>Choose languages and frameworks</li></ul>| <ul><li>[X] Refined Project Plan</li><li>[ ] Frameworks and environments</li></ul> | Everyone | 
| 2    | <ul><li>Select specific datasets for model training</li><li>Research/choose ML model architecture.</li></ul> | <ul><li>[ ] Dataset and Model Architecture Selection</li></ul> | Everyone | 
| 3    | <ul><li>Obtain data</li><li>Begin pre-processing.</li></ul> | <ul><li>[ ] Notebook with pre-processing functions</li></ul>| <ul><li>**Usman**: Get data</li><li>**Evan & Jair**: Pre-processing</li></ul> |
| 4    | <ul><li>Complete pre-processing</li><li>Start model training.>/li></ul> | <ul><li>[ ] Notebook with architecture and training</li></ul> | <ul><li>**Usman & Evan**: Train model</li><li>**Jair**: Finish pre-processing</li></ul> |
| 5    | <ul><li>Continue model training</li></ul>| <ul><li>[ ] Finished notebook with architecture and training</li></ul> | Everyone | 
| 6    | <ul><li>Present current progress</li></ul> | <ul><li>[ ] Slideshow summarizing project so far </li></ul> | Everyone |
| 7    |  <ul><li>Conduct testing </li><li>Improvement of Model</li></ul> | <ul><li>[ ] Notebook with testing </li><li>[ ] Document with results and improvements </li></ul> | <ul><li>**Evan**: Model testing</li><li>**Jair & Usman**: Training</li> |
| 8    | <ul><li>Start Final Report Draft</li><li>More testing and improvement</li> | <ul><li>[ ] Model improved</li><li>[ ] Google Doc with draft content</li></ul> | <ul><li>**Jair & Usman**: Improving and testing the model</li><li>**Evan**: Drafting</li></ul> |
| 9    | <ul><li>Continue drafting</li><li>Debug and saving model</li></ul> | <ul>><li>[ ] DL Model saved </li></ul> | <ul><li>**Jair**: Draft</li><li>**Usman & Evan**: Debug and save model</li></ul> |
| 10   | <ul><li>Submit first draft of the final report</li><li>Start ful-stack development</li></ul> | <ul><li>[ ] Mock API to serve the model</li><li>[ ] Front end started </li></ul> | <ul><li>**Jair**: Frontend</li><li>**Usman & Evan**: Backend</li></ul>
| 11   | <ul><li>Continue frontend and backend development.</li></ul> | <ul><li>[ ] Back end with custom RAG started</li><li>Front end working for DL model</li> | <ul><li>**Jair & Evan**: Backend and RAG</li><li>**Usman**: Front end</li></ul> | 
| 12   | <ul><li>Continue development</li><li>Start final report draft.</li></ul> | <ul><li>[ ] Finish front end</li><li>[ ] Finish Back end and RAG</li></ul> | <ul><li>**Jair**: Report</li><li>**Usman**: Backend</li><li>**Evan**: Frontend</li></ul> |
| 13   | <ul><li>Conduct final tests</li><li>Deploy app (optional) </li><li>Wrap up the project.</li></ul> | <ul><li>[ ] Complete full-stack app</li><li>[ ] Link to deployed app (optional)</li></ul> | Everyone |
| 14   | <ul><li>Prepare for Demo day</li><li>Continue final report</li></ul> | <ul><li>[ ] Slideshow for project demo</li></ul> | Everyone |
| 15   | <ul><li>Submit the final report</li><li>Provide and gather feedback</li></ul>  | <ul><li>[ ] Final report submission</li></ul> | Everyone |


----

## About Us
[Know about our team](https://docs.google.com/presentation/d/1SBlGVdz81NUZDpsXQ5xZXaC7oOi-OAkKURFXmy4CcT8/edit?usp=sharing)
