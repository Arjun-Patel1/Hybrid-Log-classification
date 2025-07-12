import os
import pandas as pd
from hybrid_classifier import hybrid_classify  # ✅ now imports the right function

log_messages = [
    "User User123 logged in.",
    "Backup completed successfully.",
    "Multiple login failures occurred on user 6454 account",
    "Unexpected shutdown detected in system A-34.",
    "Hey bro, chill ya!",
    "System updated to version 3.5.1"
]

results = []
for log in log_messages:
    label = hybrid_classify(log)
    results.append({"log_message": log, "predicted_label": label})

# Create output folder if needed
os.makedirs("output", exist_ok=True)

# Save classified logs
pd.DataFrame(results).to_csv("output/classified_logs.csv", index=False)

print("✅ Logs classified and saved to output/classified_logs.csv")
