from processor_regex import classify_with_regex
from processor_e5 import classify_with_e5

def hybrid_classify(log_message):
    # Try regex first
    regex_label = classify_with_regex(log_message)
    if regex_label:
        return regex_label

    # Fallback to E5 + classifier
    return classify_with_e5(log_message)
