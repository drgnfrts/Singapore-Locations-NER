# Named Entity Recogniser for Singapore Location Names

Hello! This is my first repo and this project was done for the Design & Planning Lab at Singapore's Urban Redevelopment Authority, where I am interning at through July 2022. :)

Named Entity Recognition (NER) is a component of Natural Language Processing, where named entities in text are detected and labelled accordingly. This repo contains NER Models built to handle Singapore Location Names, and the underlying scripts and configurations used to train the NER models.

Four NER Models are included in this repo - with v2.1 and v3.0/model-best most optimal for direct use.

## Installation and Usage

_git clone_ the repo to your local machine. The required packages for running and viewing the NER Models are on the [requirements.txt](./requirements.txt) file. There are some additional packages used for model training that are not included as they affect the Streamlit Mini-App deployment - see the Additional Packages section below for more information.

### Running Streamlit Mini-App

For quick viewing of the NER Models' capabilities, you can run the Streamlit Mini-App

1.  Ensure that packages and dependencies for Streamlit are downloaded into your environment
2.  Ensure that the base requirements.txt file from the repo is NOT modified.
3.  In your terminal, change directory to the main folder of this repo. Type in:

                streamlit run streamlit/model_demo.py

4.  You can now view the app at http://localhost:8501/. Note that the app will take approximately 3-5 minutes to load up.

### Comparison to Other Models

An Evaluation Dataset unseen by the Model is available for you to make a comparison with any other seperately trained NER Model. Note that this Evaluation Dataset is only to be used for comparisons with Model 3.1.

1.  Ensure that packages and dependencies for spaCy are downloaded into your environment
2.  In your terminal, change directory to the main folder of this repo. Type in:

        spacy evaluate (link to your model) data/training_datasets/golden_set.spacy

### Additional Packages

You can run the model both in IDE and Streamlit with only the packages in the base requirements.txt file.

Addtional packages used for model training (specifically _newspaper3k_, _doccano_ and _wikipediaapi_, and their associated dependencies) are **NOT included** in the base requirements.txt file as they affect the Streamlit mini-app deployment.

Downloading addtional packages onto your local environment **will NOT affect** the mini-app, but as Streamlit checks the requirements.txt file to get the necessary packages when hosting, the base requirements.text **should not be modified**. To keep track of additional dependencies, you may need to create a "secondary" requirements.txt file somewhere else.

To install the _newspaper3k_, _doccano_ and _wikipediaapi_ packages used to develop the model, add on these lines in the command terminal:

        !pip install wikipediaapi
        !pip install newspaper3k
        !pip install doccano

The packages to run the script for FastAPI are currently not yet on the requirements.txt file while I figure out if the dependencies will affect Streamlit deployment. For now, please add on:

        !pip install fastapi
        !pip install pydantic
        !pip install uvicorn

## Documentation

Detailed documentation is available [here](./documentation/documentation.md) for the following items:

- Project Background
- Instructions on running the NER Model within an IDE
- Model Creation Process and considerations behind the process

## Credits

The NER Models were trained using libraries and model creation frameworks from [spaCy v3](https://spacy.io/), with manual annotations for the models created using [Doccano](https://github.com/doccano/doccano).

Some data and portions of code in the scripts were derived or sourced directly from the following sources:

Locations Data: [2017 OneMap Data - GitHub](https://github.com/xkjyeah/singapore-postal-codes) by Daniel Sim/xkyyeah  
spaCy v3 Model Training Scripts: [spaCy Tutorials 3x - GitHub](https://github.com/wjbmattingly/spacy_tutorials_3x) | [spaCy NER Youtube Tutorials - GitHub](https://github.com/wjbmattingly/ner_youtube/tree/main/lessons) by Dr William Mattingly  
Doccano to spaCy v2 Script: [Training spaCy NER Models with Doccano](https://medium.com/@justindavies/training-spacy-ner-models-with-doccano-8d8203e29bfa) by Justin Davies

I would like to sincerely thank the Urban Redevelopment Authority's Design & Planning Lab for allocating resources and support to enable the creation of this project, especially my internship mentors, who have provided much needed strategic and technical guidance.

## Licenses

2017 OneMap Data - [Daniel Sim / xkyyeah](https://github.com/xkjyeah) & © [Singapore Land Authority](https://www.onemap.gov.sg/legal/termsofuse.html)  
spaCy v3 Tutorials & spaCy NER Tutorials - © [Dr William Mattingly](https://wjbmattingly.com/)  
Training spaCy NER Models with Doccano - © [Justin Davies](https://medium.com/@justindavies)  
Other Raw Training Data - respective copyright holders
spaCy functionalities - © [Explosion AI](https://github.com/explosion/spaCy/blob/master/LICENSE)

Everything else - [MIT © 2022 Nicolas Tang](LICENSE.md)
