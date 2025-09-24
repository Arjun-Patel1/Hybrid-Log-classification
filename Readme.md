🚀 Hybrid Log Classification Framework
A powerful, extensible system for log classification that blends rule-based and state-of-the-art machine learning techniques. Designed for both structured and unstructured log data, this project delivers exceptional accuracy and flexibility for modern log analysis needs.

🧩 Key Features
Hybrid Classification: Combines precise Regex-based rules with robust ML (Sentence Transformer + Logistic Regression) for best-in-class results.
Customizable: Easily extend regular expressions or retrain the ML model for your unique log sources.
High Accuracy: Achieves 99% overall accuracy and 0.99 weighted F1-score (see the results below).
API & CLI: Use via simple command-line scripts or spin up a FastAPI server for integration with your tools.
🏗️ Project Structure
Code
log_classifier_project/
├── processor_regex.py       # Rule-based classification
├── processor_e5.py          # Embedding + classifier logic
├── hybrid_classifier.py     # Hybrid logic controller
├── classify.py              # CLI-based classification
├── train_model.py           # Model training scripts
├── server.py                # FastAPI app (optional)
├── models/
│   └── log_classifier.joblib
├── data/
│   └── logs.csv
├── resources/
│   ├── arch.png
│   └── classification_metrics_heatmap.png
├── notebooks/
│   └── training_notebook.ipynb
└── requirements.txt
💡 How It Works
1. Regex Classification
Best For: Clearly structured patterns (e.g., login events, backups, system updates).
Benefits: Fast, deterministic, and easy to extend for known log types.
2. Transformer (E5-small-v2) + Logistic Regression
Best For: Unstructured or semi-structured logs.
How: Transforms log text into embeddings, then classifies using a trained logistic regression model.
📊 Performance
Label	Precision	Recall	F1-score	Support
Critical Error	0.90	1.00	0.95	46
Error	0.98	0.87	0.92	47
HTTP Status	1.00	1.00	1.00	316
Resource Usage	1.00	1.00	1.00	46
Security Alert	0.99	0.99	0.99	114
User Action	1.00	1.00	1.00	32
Overall Accuracy: 99%
Macro F1-score: 0.98
Weighted F1-score: 0.99

![Confusion Matrix](resources/classification_metrics_heatmap.png)

⚙️ Installation & Setup
Clone the Repository

bash
git clone https://github.com/Arjun-Patel1/Hybrid-Log-classification.git
cd Hybrid-Log-classification
Install Dependencies

bash
pip install -r requirements.txt
Required packages: sentence-transformers, scikit-learn, fastapi, uvicorn, python-multipart
🚀 Usage
CLI Classification
bash
python classify.py
Start FastAPI Server
bash
uvicorn server:app --reload
API Docs: http://127.0.0.1:8000/docs
ReDoc: http://127.0.0.1:8000/redoc
📝 Example Data
Input CSV:

Code
timestamp,source,log_message
2025-06-27 07:20:25,ModernCRM,"Email service experiencing issues with sending"
2025-07-12 00:24:16,ModernHR,"nova.osapi_compute.wsgi.server ... status: 200"
Output CSV:

Code
log_message,predicted_label
User User123 logged in.,User Action
Backup completed successfully.,System Notification
Multiple login failures occurred...,Security Alert
🙌 Contributions
Feel free to fork, submit issues, and contribute improvements! For major changes, open an issue first to discuss what you’d like to change.

👤 Author
Developed and maintained by Arjun Patel
