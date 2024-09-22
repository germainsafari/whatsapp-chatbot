import json
import os

def load_faq_data():
    with open(os.path.join("data", "faq_data.json")) as f:
        return json.load(f)

def handle_custom_data(question):
    faq_data = load_faq_data()

 
    for faq in faq_data:
        if faq["question"].lower() in question.lower():
            return faq["answer"]
    
    return None
