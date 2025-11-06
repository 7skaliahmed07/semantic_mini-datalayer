import spacy

# Load the English NLP model once
nlp = spacy.load("en_core_web_sm")

def extract_entities(text):
    """
    Extract named entities from a single text string.
    Returns a list of {'text': entity_text, 'label': entity_label}.
    """
    doc = nlp(text)
    entities = [{"text": ent.text, "label": ent.label_} for ent in doc.ents]
    return entities
