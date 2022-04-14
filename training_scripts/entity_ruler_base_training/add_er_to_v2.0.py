import spacy

nlp = spacy.load("..\..\models\model_v2.0\model-best")
loc_er = spacy.load("..\..\models\loc_er")

nlp.add_pipe("entity_ruler", source=loc_er, before="ner")
nlp.to_disk("..\..\models\model_v2.1")