# CHANGELOG

## [1.1.0] 🗓️ - 08/06/2022

### Added

- New dataset of locations text & annotations (suffixed with \_v3.1)
- _model_v3.1_ , a new Enhanced NER-centric model trained on a larger (1598 > 2180) dataset
- "Gold Standard" Evaluation Annotated Dataset & Evaluation Script (golden_set.spacy)

### Changed

- Updated Streamlit Mini-App script to enable users to run Model 3.1 on Streamlit
- Updated Documentation for Model 3.1 + how to evaluate with the "Gold Standard" set

## [1.0.4] 🗓️ - 11/05/2022

### Added

- Script to run POST requests for NER with Model v3.0, built with FastAPI

## [1.0.3] 🗓️ - 04/05/2022

### Added

- Test Jupyter Notebook and a Plan Outline for Geocoding Locations phase of Project
- Proper CHANGELOG.md

### Changed

- Streamlined readme.md

## [1.0.2] 🗓️ - 28/04/2022

### Added

- LICENSE.md

## [1.0.1] 🗓️ - 24/04/2022

### Changed

- Finalised first version of _documentation.md_
- Updated readme.md
- Reorganised certain files

### Fixed

- Optimised Training Scripts and Streamlit Mini-App Script

### Removed

- Redundant file _data/training_datasets/train_data_er.json_

## [1.0.0] - 🗓️ 14/04/2022

### Added

- _documentation_ subfolder and _documentation.md_

### Changed

- Took down and reuploaded repo to remove residual Git LFS files from _model_v1.0_

### Fixed

- _requirements.txt_ file, following switchover to standard _virtualenv_ environment. File lacks packages for newspaper3k, wikipediaapi and doccano to enable functioning of Streamlit mini-app.
- Streamlit mini-app now fully functional

## [0.4.0] - 🗓️ 29/03/2022

### Added

- _model_v3.0_, an Enhanced NER-Centric Model
- Scripts used for model training of _model_v3.0_, including scripts used to handle and convert training data from Doccano
- Training datasets for _model_v3.0_. File names end with the _\_doccano_ suffix before their file extensions label
- Script to run Streamlit mini-app
- _model_v1.1_, a re-trained version of _model_v1.0_ without the excessively large vector file. Still fundementally useless, but much smaller in size now.

### Changed

- Reorganised data subfolder and its internal subfolders
- Names of files containing training datasets for the Dictionary-Centric Model appended with _\_er_ suffix before the file extension labels

### Removed

- _model_v1.0_ - excessively large vector file was clogging the repo

## [0.3.0] - 🗓️ 10/03/2022

### Added

- _model_v2.1_, the Third (final) Dictionary-Centric NER Model. Model uses the _model_v2.0_ as a base, with an EntityRuler pipe added to function as a "Dictionary of Locations" to find and match locations in text

### Changed

- First Model and Second Model renamed to _model_v1.0_ and _model_v2.0_.
- Scripts for data cleaning and model training shifted to new _training_scripts_ subfolder.
- Configuration files for model training shifted to new _training_config_ subfolder and renamed by model version number.

## [0.2.0] - 🗓️ 03/03/2022

### Added

- Second Dictionary-Centric NER Model custom-trained for Singapore Locations. Utilises _tok2vec, tagger & parser_ from spaCy's pre-built _en_core_web_md_, and a custom-trained NER pipe.
- _requirements.txt_ file. Anaconda environment used for development of project, future updates will further refine the file.
- - _config.cfg_ and _base_config.cfg_ for Second Model.

## [0.1.0] - 🗓️ 24/02/2022

### Added

- First iteration of scripts used to clean data for Dictionary-Centric Model
- Locations Data
- First Dictionary-Centric NER Model. Consists of _tok2vec_ and _ner_ pipes
- _config.cfg_ and _base_config.cfg_ for First Model
