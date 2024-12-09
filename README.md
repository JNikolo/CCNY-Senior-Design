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
    <li><a href="#usage">Usage</a></li>
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

## RAG Playground
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

