from sentence_transformers import SentenceTransformer
import joblib
import numpy as np

model = SentenceTransformer('intfloat/e5-small-v2')
classifier = joblib.load('models/log_classifier.joblib')

def classify_with_e5(log_message):
    # Format input as required by E5 model
    input_text = "passage: " + str(log_message)
    embedding = model.encode([input_text], convert_to_numpy=True)
    
    probs = classifier.predict_proba(embedding)[0]
    if max(probs) < 0.5:
        return "Uncertain"
    return classifier.predict(embedding)[0]
