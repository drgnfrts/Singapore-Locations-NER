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
- [Repo Organisation](#repo-organisation)
- [Model Creation Process](#model-creation-process)
  - [Location Data Collection & Cleaning](#location-data-collection--cleaning)
    - [Locations Entry Extraction](#locations-entry-extraction)
    - [Conversion of Entries to Standard Capitalisation](#conversion-of-entries-to-standard-capitalisation)
    - [Manual Cleaning of Extracted Data](#manual-cleaning-of-extracted-data)
  - [Sourcing Data for Annotations](#sourcing-data-for-annotations)
  - [Data Annotation](#data-annotation)
    - [Automated Annotations with spaCy EntityRuler](#automated-annotations-with-spacy-entityruler)
    - [Manual Annotations with Doccano](#manual-annotations-with-doccano)
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

Pipes are arranged in order from left to right.

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

Note that the Streamlit mini-app will only display Model v2.1 and v3.0.

## Running Model within IDE

1. Ensure that packages and dependencies for spaCy (& Jupyter Notebook, if desired) are downloaded into your environment.
2. Create a new Jupyter Notebook or Python file.
3. Import the following packages

```
import spacy
from spacy import displacy
```

4. Link the path to the model of choice, and load it.

- For models v1.0, v2.0 and v3.0, note that you will need to further reference the model-best folder

```
path = "models/model_v3.0/model_best"
nlp = spacy.load(path)
```

5. Type in your desired text for analysis and call the render function on display.

```
doc = nlp("This example text was created at 45 Maxwell Road.")
displacy.render(doc, style="ent")
```

# Repo Organisation

The repo is organised into the following folders:

| Folder           | Subfolder                  | Contents                                                                    |
| ---------------- | -------------------------- | --------------------------------------------------------------------------- |
| archive          |                            | Jupyter Notebooks use to trial certain scripts                              |
|                  | doccano_trial              | Imported data from a Doccano test annotation trial                          |
| data             | doccano_annotated_data     | Imported final Doccano annotations for v3.0                                 |
|                  | extracted_locations        | Singapore locations data, post-cleaning                                     |
|                  | singapore-postal-codes     | [OneMap Data](https://github.com/xkjyeah/singapore-postal-codes) by xkyyeah |
|                  | text_data                  | Text for annotations                                                        |
|                  | training_datasets          | Training and Test Datasets for spaCy in json and spacy binary formats       |
| models           | loc_er                     | _en_core_web_md_ model with "locations dictionary" EntityRuler pipe added   |
|                  | v1.1                       | Trial to create base model for Dictionary-centric method                    |
|                  | v2.0                       | Base model for Dictionary-centric method                                    |
|                  | v2.1                       | v2.0/model-best with "locations dictionary" EntityRuler pipe added          |
|                  | v3.0                       | Enhanced NER-based model                                                    |
| streamlit        |                            | Model Demo for Streamlit                                                    |
| training_config  |                            | Base configuration and final configuration files for models                 |
| training_scripts | doccano_base_training      | Scripts for model training specific to Enhanced NER-based model             |
|                  | entity_ruler_base_training | Scripts for model training specific to Dictionary-centric model             |
|                  |                            | Scripts for model training common to both methods                           |

# Model Creation Process

Different steps were taken to create Dictionary-centric Models (v1.0, v2.0, v2.1) and Enhanced NER-based Model (v3.0).

**Dictionary-centric Models**

1. Sourcing and cleaning location names data
2. Sourcing annotation data
3. Utilising the location names data to create annotations automatically with spaCy EntityRuler
4. Training the model with the annotations
5. Adding the location names data as an EntityRuler pipe

**Enhanced NER-based Model**

1. Sourcing annotation data
2. Creating annotations manually with Doccano
3. Training the model with the annotations

## Location Data Collection & Cleaning

**Relevant Script**: [training_scripts/entity_ruler_base_training/onemap_names_filter.ipynb](../training_scripts/entity_ruler_base_training/onemap_names_filter.ipynb)

For the location names and addresses data, a [repo of Singapore location names](https://github.com/xkjyeah/singapore-postal-codes) was cloned and saved to [data/singapore-postal-codes](../data/singapore-postal-codes/).

A raw data entry looks like this:

![Example of raw location data entry](./images/location-data-example.png)

For each location data entry, the desired outcomes were as such:

1. Extract the building name, street name, postal code and address
2. Convert these item names from Title Case (block letters) to standard English capitalisation

### Locations Entry Extraction

For each location, extracting the building name, street name, postal code and address was desired. A script was created to extract the first three from the data entries directly.

For the latter, extracting a simple address consisting of the building/block number and street name was preferred over extracting the full, raw address entry. This is as location addresses in Singapore are more often referred to in this manner. The initial method to do so relied on the method below

    #not code
    SIMPLE ADDRESS = ADDRESS - POSTAL CODE - SEARCHVAL(if SEARCHVAL != ROAD NAME)

However, this method would not work for examples such this one, where the SEARCHVAL entry reflected the estate name, especially for private estates. The SIMPLE ADDRESS for this particular entry, for instance, would just be "1".

![Example of data entry with odd SEARCHVAL value](./images/weird-location-data-entry.png)

This would result in the simple address only being the building number. This occured for multiple estates. While some SEARCHVAL values were manually corrected, it was untenable to do so for all entries in the list of addresses and buildings. A second method was attempted to create the SIMPLE ADDRESS ENTRY

    #not code
    SIMPLE ADDRESS = BLK_NO + ROAD_NAME

The list was iterated over with this method, followed by removal of duplicate entries with _list(set(list))_.

### Conversion of Entries to Standard Capitalisation

As the data entries are in title case, a snippet of code was created to convert the entries to standard capitalisation before they were extracted. Proper capitalisation is one of the factors the spaCy pipeline takes into account when tagging named entities, therefore

This is as the spaCy pipeline tags named entities by taking

    def properly_capitalise(location_name):
      properly_capitalised_name = location_name.lower().title()
      return properly_capitalised_name

However, this method resulted in some oddities being output, especially when capital letters were used for non-first letters in the words.

!["SCDF" and "HQ" not being fully capitalised in the entry "1st SCDF Division HQ"](./images/capitalisation-off.png)

### Manual Cleaning of Extracted Data

The building names list was manually looked through in order to correct any inaccuracies in letter case for each entry. During this process, it was also discovered that there were location entries that were merely tenants/organisations within the building, rather than being unique buildings with distinct adresses.

This particularly applied to kindergartens and pre-schools, which are typically housed below apartment blocks or in commercial buildings. These facilities were listed as locations in the original [OneMap Data](https://github.com/xkjyeah/singapore-postal-codes) repo as OneMap has a query function for kindergartens and pre-schools.

For instance, this particular pre-school ended up in the scraped list of buildings, when it is not a unique building but a tenant of the building.

![Zulfa Kindergarten at Sembawang Mart listed as a location in the scraped data](./images/building-tenant-example.png)

![The kindergaten is not a unique building as it is housed in Sembawang Mart commerical building](./images/zulfa-sembawang-mart.png)

The number of unique entries for building reduced was afterward reduced from 16000 to 11000. The list can be found in [data/extracted_locations/short_manual_buildings_name_list.json](../data/extracted_locations/short_manual_buildings_name_list.json).

The cleaned building names list was then compiled with the other extracted locations list in [data/extracted_locations/combined_locations.json](../data/extracted_locations/combined_locations.json)

## Sourcing Data for Annotations

## Data Annotation

### Automated Annotations with spaCy EntityRuler

### Manual Annotations with Doccano

## Model Training

### Considerations and configuration for v1.1

### Considerations and configuration for v2.0

### Considerations and configuration for v3.0
