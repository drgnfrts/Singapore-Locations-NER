# Named Entity Recogniser for Singapore Location Names

Hello! This is my first repo and this project was done for Singapore's Urban Redevelopment Authority, where I am currently (Apr 2022) an intern. :)

spaCy NLP Library was utilised to create this Named Entity Recogniser. Three versions of the model have been trained. v1.1 and v2.0/2.1 used spaCy's native EntityRuler pipe to auto-annotate and create the training data, while v3.0's training data was annotated manually using [Doccano](https://github.com/doccano/doccano).

Some portions of code/data was derived from the following sources:

Data: [2017 OneMap Data](https://github.com/xkjyeah/singapore-postal-codes) by xkyyeah  
Model Training: [spaCy v3 Tutorials](https://github.com/wjbmattingly/spacy_tutorials_3x) | [spaCy NER Tutorials](https://github.com/wjbmattingly/ner_youtube/tree/main/lessons) by Dr W.J.B Mattingly

## Model Creation Process

### Model v1.1, v2.0 and v2.1

- Data was first cleaned and relevant building & road names extracted.
- An EntityRuler to tag location names with the LOC label was then created with the location name data and added as a a pipe to a pre-existing model.
- loc_er was then used to generate annotations to be used as training data.
- Training data (900+ sets) was converted to spaCy v3 binary files, with the ratio of training data to validation data being 50:50.

- By nature of the training config settings, v1.1 only consists of NER and tok2vec pipes. v2.0 and 2.1 have tagger and parser pipes added before the NER component, enabling the model greater accuracy.
- v2.1 has loc_er added as a pipe before the NER pipe to act as a "dictionary" to catch addresses that the NER may not be able to.

### Model v3.0

- Multiple articles and text were broken into sentences and passed into a txt file, with each sentence occupying a new line in the file.
- Sentences were annotated manually with LOC, ORG or FAC labels and the data downloaded back.
- Training data (~1600 sets) was converted to spaCy v3 binary files, with the ratio of training data to validation data being 80:20.

- The nature of manual annotation meant more entities could be captured, making it the most accurate model thus far. It is able to pick up addresses without the need for the loc_er pipe, and has a rudimentary ability to distinguish when a particular organisation is being referrred to as a location and vice versa.

## Updates

CAA 290322:

- Added scripts to handle and convert traindata from Doccano
- Added script to run a mini Streamlit app under streamlit/model_demo.py
- Added a third, Doccano-based model under model_v3.0/model_best
- Fixed some file references.

CAA 100322:

- Added the Locations EntityRuler to the second model, labelled as model_v2.1
- First and second models renamed to model_v1.0 and model_v2.0 respectively
- Shifted scripts handling the training process to a new training_scripts folder

CAA 030322:

- Added a second model under models/second_model, the second model has tok2vec, tagger and parser components based off spaCy's native en_core_web_md model, which has improved the accuracy of the NER tagging
- Added requirements.text file. The list is lengthy as the environment was created with Anaconda, and not all files are required. Still trying to work out which exact files may be needed.
