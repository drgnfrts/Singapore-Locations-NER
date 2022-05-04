# This is the script to run the Streamlit mini-app.

from pickle import TRUE
import streamlit as st
import spacy
from spacy import displacy, load
import re
import csv


# Page title and icon for the browser bar
st.set_page_config(
    page_title="NER for SG Locations",
    page_icon="🇸🇬",
)


# Makes the app width the full length of the screen, unless it exceeds 1400px.
def _max_width_():
    max_width_str = f"max-width: 1400px;"
    st.markdown(
        f"""
    <style>
    .main .block-container{{
        {max_width_str}
    }}
    </style>
    """,
        unsafe_allow_html=True,
    )


# Call _max_width_() function
_max_width_()


# Function to load models, and cache them to ensure no reloading of the model occurs every time we try to re-run the whole app. The models are stored in a dictionary to enable easy access.
@st.cache(show_spinner=False, allow_output_mutation=True, suppress_st_warning=True)
def load_models():
    standard_model = spacy.load("en_core_web_md")
    er_model = spacy.load("./models/model_v2.1")
    doccano_model = spacy.load("./models/model_v3.0/model-best")
    models = {"std": standard_model, "erl": er_model, "dcn": doccano_model}
    return models


models = load_models()


# Pull the list of locations.
abbreviation_dictionary = []
with open("./data/extracted_locations/sg_abbreviations.csv", "r") as csv_file:
    csvtest = csv.reader(csv_file, delimiter=",")
    for row in csvtest:
        abbreviation_dictionary.append(row)


# Function below utilises the list to lengthen the abbreviations
def lengthen_abbreviations(text):
    split = re.findall(r"[\w']+|[.,!?;&] | |-", text)
    i = 0
    for word in split:
        for row in abbreviation_dictionary:
            check_column = 0
            while check_column < 4:
                if word == "":
                    split[i] = ''
                elif word == row[check_column]:
                    split[i] = row[3]
                check_column += 1
        i += 1
    cleaned_text = ''.join(split)
    return cleaned_text


### ACTUAL START OF APP CONTENTS ###
st.title("Named Entity Recogniser for Singapore Locations 📍")
st.write("Compare the Standard English NLP Model with the Trained SG Location Names Model.")


# Function to clear the inputs in the form by clearing the session state of the input box. The key for the text input box here is "1".
def clear_form():
    st.session_state[1] = ""


# Function to enable selection of any number of the NLP models
def select_models(all_models_selected):
    if all_models_selected == True:
        selected_models = container.multiselect("Choose one or more models to analyse text with:", [
            'Standard Model', 'Dictionary Model', 'NER-based Model'], ['Standard Model', 'Dictionary Model', 'NER-based Model'])
    else:
        selected_models = container.multiselect("Choose one or more models to analyse text with:", [
            'Standard Model', 'Dictionary Model', 'NER-based Model'])
    return selected_models


# Function to find the entities in text, depending on choice of model and whether abbreviations need to be lengthened
def find_ents(model, input, abr_lengthen):
    if abr_lengthen == True:
        doc = model(lengthen_abbreviations(input))
    else:
        doc = model(input)
    ent_html = displacy.render(doc, style="ent", jupyter=False)
    st.markdown(ent_html, unsafe_allow_html=True)
    st.write("")


# Dictionary for def display_models() to reference
model_choice = {"Standard Model": ("Pre-trained Standard English Model 💂", models["std"]),
                "Dictionary Model": ("Dictionary-centric Model for SG Locations 📖", models["erl"]),
                "NER-based Model": ("Enhanced NER-centric Model for SG Locations 🦁", models["dcn"])
                }


# Function to display the models and the text analysed with def find_ents()
def display_models(selected_models, text_input, abbreviation_status):
    for selected_model in selected_models:
        st.header(model_choice[selected_model][0])
        find_ents(model_choice[selected_model][1],
                  text_input, abbreviation_status)


# The actual form with inputs for model type, lengthening abbreviations and text to be analysed.
with st.form("NER_form"):
    # First item is a container that will display models to be used
    container = st.container()
    # Below the container is the checkboxes to enable selection of all models and abbreviations lengthening
    c_all_model_selection, c_abbreviate_selection, c_selection_last = st.columns([
        1, 1, 3])
    with c_all_model_selection:
        all_models_selected = st.checkbox("Select all models")
    with c_abbreviate_selection:
        abbreviation_status = st.checkbox("Lengthen abbreviations")
    # Multiselect option for the container is below
    selected_models = select_models(all_models_selected)
    # Clear the text input the first time around
    text_input = st.empty()
    # Text input is a text area box with the key "1". The key is to allow reference for def clear_form() to clear the text input box by resetting the session state.
    input = text_input.text_area('Text to analyze:', key=1)
    # Buttons to find the locations and clear the form
    c_submit, c_clear, c_last = st.columns([1, 1, 5])
    with c_submit:
        submitted = st.form_submit_button("Find Locations 🌎")
    with c_clear:
        click_clear = st.form_submit_button(
            'Clear text input ⌫', on_click=clear_form)
    if submitted:
        display_models(selected_models, input, abbreviation_status)


# Drop-down "About" section
with st.expander("ℹ️ - About this app", expanded=False):
    st.write(
        """
-   This *Named Entity Recognition model for Singapore Location Names* detects Singaporean addresses, place names and building names from text.
-   It was made with [spaCy v3](https://spacy.io/), an open-source library for Natural Language Processing.
-   Check out the source code here on my [Github repo](https://github.com/drgnfrts/Singapore-Locations-NER)! :)
	    """
    )
    st.markdown("")
