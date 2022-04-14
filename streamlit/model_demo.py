import streamlit as st
import spacy
from spacy import displacy, load
import re
import csv

st.set_page_config(
    page_title="NER for SG Locations",
    page_icon="🇸🇬",
)


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


_max_width_()


@st.cache(show_spinner=False, allow_output_mutation=True, suppress_st_warning=True)
def load_models():
    standard_model = spacy.load("en_core_web_sm")
    er_model = spacy.load("./models/model_v2.1")
    doccano_model = spacy.load("./models/model_v3.0/model-best")
    #doccano_model = spacy.load(doccano_model_path)
    models = {"std": standard_model, "erl": er_model, "dcn": doccano_model}
    return models


models = load_models()

abbreviation_dictionary = []
with open("./data/other_location_data/sg_abbreviations.csv", "r") as csv_file:
    csvtest = csv.reader(csv_file, delimiter=",")
    for row in csvtest:
        abbreviation_dictionary.append(row)


def lengthen_abbreviations(text):
    split = re.findall(r"[\w']+|[.,!?;&] | |-", text)
    print(split)
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
            csv_file.close()

        i += 1
    cleaned_text = ''.join(split)
    return cleaned_text


# Display a section header:
st.title("Named Entity Recogniser for Singapore Locations 📍")
# st.text_input takes a label and default text string:
st.write("Compare the Standard English NLP Model with the Trained SG Location Names Model.")


def clear_form():
    st.session_state[1] = ""


def find_ents(model, input):
    doc = model(lengthen_abbreviations(input))
    ent_html = displacy.render(doc, style="ent", jupyter=False)
    st.markdown(ent_html, unsafe_allow_html=True)
    st.write("")


with st.form("NER_form"):
    container = st.container()
    all = st.checkbox("Select all")
    if all:
        selected_options = container.multiselect("Choose one or more models to analyse text with:",['Standard Model', 'Dictionary Model', 'NER-based Model'],['Standard Model', 'Dictionary Model', 'NER-based Model'])
    else:
        selected_options =  container.multiselect("Choose one or more models to analyse text with:",['Standard Model', 'Dictionary Model', 'NER-based Model'])
    text_input = st.empty()
    input = text_input.text_area('Text to analyze:', key=1)
    c_submit, c_clear, c_last = st.columns([1, 1, 5])
    with c_submit:
        submitted = st.form_submit_button("Find Locations 🌎")
    with c_clear:
        click_clear = st.form_submit_button(
            'Clear text input ⌫', on_click=clear_form)
    if submitted:
        if "Standard Model" in selected_options:
            st.header("Pre-trained Standard English Model 💂")
            find_ents(models["std"], input)
        if "Dictionary Model" in selected_options:
            st.header("Custom Trained Dictionary-based Model for SG Locations 🦁")
            find_ents(models["erl"], input)
        if "NER-based Model" in selected_options:
            st.header("Custom Trained NER-based Model for SG Locations 🦁")
            find_ents(models["dcn"], input)

with st.expander("ℹ️ - About this app", expanded=False):
    st.write(
        """
-   This *Named Entity Recognition model for Singapore Location Names* detects Singaporean addresses, place names and building names from text. 
-   It was made with [spaCy v3](https://spacy.io/), an open-source library for Natural Language Processing.
-   Check out the source code here on my [Github repo](https://github.com/drgnfrts/Singapore-Locations-NER)! :)
	    """
    )
    st.markdown("")


