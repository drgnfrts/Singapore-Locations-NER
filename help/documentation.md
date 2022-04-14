# Introduction

## Named Entity Recognition in the Urban Planning context

A lot of information can be presented in text. The fluidity of language means that text structures can both vary greatly and be very complex. Automating the extraction of information from text hence requires some form of Natural Language Processing (NLP).

NLP is a subset of artificial intelligence and involves the application of computational techniques to the analysis of human language. One key technique is Named Entity Recognition (NER) - the extraction of named entities (place names, persons, organisations, dates & times, etc.) from text. Modern NLP models often have tools to perform NER.

In the field of urban planning and analytics, NER models could be used to aid tagging of named entities (e.g. geotagging) and sentiment analysis.

## Project Objective

Create a re-trainable and potentially scalable Named Entity Recognition model for Singapore location names, using the spaCy library.

## Requirements

- Basic fundementals of Python 3 and pip.
- Some understanding of spaCy NLP Library (tutorial seperate from this markdown file)
- The specific software to be downloaded can be found on the requirements.txt file.

Note that the models built here are set to run on the CPU, but can be modified to run on the GPU (NVIDIA GPUs only).

## Table of Contents

- [Introduction](#introduction)
  - [Named Entity Recognition in the Urban Planning context](#named-entity-recognition-in-the-urban-planning-context)
  - [Project Objective](#project-objective)
  - [Requirements](#requirements)
  - [Table of Contents](#table-of-contents)
- [Models Available](#models-available)
  - [Pipes Available](#pipes-available)
- [Running the Model](#running-the-model)
  - [Running Model on Streamlit](#running-model-on-streamlit)
  - [Running Model within IDE](#running-model-within-ide)
- [Model Creation Process](#model-creation-process)
  - [Data Collection & Cleaning](#data-collection--cleaning)
  - [Data Annotation](#data-annotation)
    - [Automated Annotations with spaCy EntityRuler](#automated-annotations-with-spacy-entityruler)
    - [Manuak Annotations with Doccano](#manuak-annotations-with-doccano)
  - [Model Training](#model-training)
    - [Considerations and configuration for v1.1](#considerations-and-configuration-for-v11)
    - [Considerations and configuration for v2.0](#considerations-and-configuration-for-v20)
    - [Considerations and configuration for v3.0](#considerations-and-configuration-for-v30)

# Models Available

Two models were conceptualised to in creating the NER Model for Singapore location names.

1. A **Dictionary-centric Model** where a "dictionary of locations" would be added as an EntityRuler pipe, with a trained NER pipe acting as a backup.
2. An **Enhanced NER-based Model** where the NER pipe would be the sole pipe tagging locations.

| Models | Type               | Intent                                                   | Annotation Method | Recommended for Use |
| ------ | ------------------ | -------------------------------------------------------- | :---------------: | :-----------------: |
| v1.1   | Dictionary-centric | Build test pipeline                                      |    EntityRuler    |         ❌          |
| v2.0   | Dictionary-centric | Build base pipeline                                      |    EntityRuler    |         ❌          |
| v2.1   | Dictionary-centric | Add "Dictionary of Locations" to v2.0                    |    EntityRuler    |         ✔️          |
| v3.0   | Enhanced NER-based | Create more flexible model by only using an enhanced NER |      Doccano      |         ✔️          |

The Enhanced NER-based model is most flexible - it can pick out new locations, location names with case or spelling deviations, and has a rudimentary ability to differentiate named entities that can be tagged with both LOC and ORG

## Pipes Available

Pipes are arranged in order from left to right

| Models | Tokenizer | POS Tagger | Dependency Parser | "Locations Dictionary" EntityRuler | NER |
| ------ | :-------: | :--------: | :---------------: | :--------------------------------: | :-: |
| v1.1   |    ✔️     |     ❌     |        ❌         |                 ❌                 | ✔️  |
| v2.0   |    ✔️     |     ✔️     |        ✔️         |                 ❌                 | ✔️  |
| v2.1   |    ✔️     |     ✔️     |        ✔️         |                 ✔️                 | ✔️  |
| v3.0   |    ✔️     |     ✔️     |        ✔️         |                 ❌                 | ✔️  |

# Running the Model

## Running Model on Streamlit

1. Ensure that packages and dependencies for Streamlit are downloaded into your environment.
2. In your terminal, change directory to the main folder of this repo. Type in:

```
streamlit run streamlit/model_demo.py
```

3. You can now view the app at http://localhost:8501/

## Running Model within IDE

1. Ensure that packages and dependencies for spaCy (& Jupyter Notebook, if desired) are downloaded into your environment.
2. Create a new Jupyter Notebook or Python file.
3. Import the following packages

```
import spacy
from spacy import displacy
```

4. Link the path to the model of choice, and load it.

```
path = "models/model_v3.0/model_best"
nlp = spacy.load(path)
```

5. Type in your desired text for analysis and call the render function on display.

```
doc = nlp("This example text was created at 45 Maxwell Road.")
displacy.render(doc, style="ent")
```

# Model Creation Process

## Data Collection & Cleaning

## Data Annotation

### Automated Annotations with spaCy EntityRuler

### Manuak Annotations with Doccano

## Model Training

### Considerations and configuration for v1.1

### Considerations and configuration for v2.0

### Considerations and configuration for v3.0
