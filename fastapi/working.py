import spacy
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()
model_path = "../models/model_v3.0/model-best"
nlp = spacy.load(model_path)


class Input(BaseModel):
    text: str

    class Config:
        schema_extra = {
            "example": {
                "text": "The Urban Redevelopment Authority is located at 45 Maxwell Road."
            }
        }


@app.post("/find-locations-POST")
def find_locations_post(input: Input):
    doc = nlp(input.text)
    list_of_entities = []
    for ent in doc.ents:
        ent_result = {}
        ent_result["entity"] = ent.text
        ent_result["label"] = ent.label_
        list_of_entities.append(ent_result)
    return {"entities": list_of_entities}
