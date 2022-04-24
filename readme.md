# Named Entity Recogniser for Singapore Location Names

Hello! This is my first repo and this project was done for Singapore's Urban Redevelopment Authority, where I am currently (Apr 2022) an intern. :)

spaCy NLP Library was utilised to create this Named Entity Recogniser. Three versions of the model have been trained. v1.1 and v2.0/2.1 used spaCy's native EntityRuler pipe to auto-annotate and create the training data, while v3.0's training data was annotated manually using [Doccano](https://github.com/doccano/doccano).

Some portions of code/data was derived from the following sources:

Data: [2017 OneMap Data](https://github.com/xkjyeah/singapore-postal-codes) by xkyyeah  
Model Training: [spaCy v3 Tutorials](https://github.com/wjbmattingly/spacy_tutorials_3x) | [spaCy NER Tutorials](https://github.com/wjbmattingly/ner_youtube/tree/main/lessons) by Dr W.J.B Mattingly

The necessary packages can be found in the [requirements.txt](./requirements.txt) file. Note that packages for newspaper3k, doccano and wikipediaapi are not included as they affect the Streamlit mini-app deployment If you are installing packages to your environment with the requirements.txt file, please add on these lines in the command terminal to install those packages:

        !pip install wikipediaapi
        !pip install newspaper3k
        !pip install doccano

## Documentation

Detailed documentation is available [here](./documentation/documentation.md) for the following items:

- Project Background
- Instructions on running the NER Model on Streamlit and within the IDE
- Model Creation Process and considerations behind the process

## Updates

CAA 240422:

- First draft of documentation completed.
- Scripts in training scripts folder given additional comments for reference
- Streamlit mini-app script cleaned and given comments for reference

CAA 160422:

- Updated documentation.md
- Reorganised some files

CAA 140422:

- Took down and reuploaded repo to remove residual Git LFS files, which were clogging up the previous iteration of the repo
- Fixed requirements.txt file. Note that it lacks the packages for newspaper3k, wikipediaapi and doccano as the file is used for Streamlit app deployment and some packages for these files affect app deployment.
- Added documentation.md

CAA 290322:

- Added scripts to handle and convert traindata from Doccano
- Added script to run a mini Streamlit app under streamlit/model_demo.py
- Added a third, Doccano-based model under model_v3.0/model_best
- Fixed some file references

CAA 100322:

- Added the Locations EntityRuler to the second model, labelled as model_v2.1
- First and second models renamed to model_v1.0 and model_v2.0 respectively
- Shifted scripts handling the training process to a new training_scripts folder

CAA 030322:

- Added a second model under models/second_model, the second model has tok2vec, tagger and parser components based off spaCy's native en_core_web_md model, which has improved the accuracy of the NER tagging
- Added requirements.text file. The list is lengthy as the environment was created with Anaconda, and not all files are required. Still trying to work out which exact files may be needed.
