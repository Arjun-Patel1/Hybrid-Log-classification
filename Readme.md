# 🚀 Log Classification with Hybrid Classification Framework

This project implements a **hybrid log classification system** that combines two intelligent methods:

* **Regex-based classification** for structured patterns
* **Transformer (E5-small-v2) + Logistic Regression** for complex log messages

The aim is to accurately label logs by leveraging the strengths of both rule-based and ML-based approaches.

---

## 🔍 Classification Approaches

### 1. 🔤 Regular Expression (Regex)

* Best for predictable log formats such as:

  * Login events
  * Backup completion
  * System updates
* Provides fast and deterministic classification.

### 2. 🧠 Sentence Transformer (E5-small-v2) + Logistic Regression

* Handles unstructured and semi-structured logs.
* Converts messages to embeddings using E5-small-v2.
* Applies Logistic Regression to classify logs based on trained patterns.

---

## 📊 Evaluation Results

| Label          | Precision | Recall | F1-score | Support |
| -------------- | --------- | ------ | -------- | ------- |
| Critical Error | 0.90      | 1.00   | 0.95     | 46      |
| Error          | 0.98      | 0.87   | 0.92     | 47      |
| HTTP Status    | 1.00      | 1.00   | 1.00     | 316     |
| Resource Usage | 1.00      | 1.00   | 1.00     | 46      |
| Security Alert | 0.99      | 0.99   | 0.99     | 114     |
| User Action    | 1.00      | 1.00   | 1.00     | 32      |

**Overall Accuracy:** `99%`

**Macro F1-score:** `0.98`

**Weighted F1-score:** `0.99`

![Confusion Matrix](resources/classification_metrics_heatmap.png)

---

## 📁 Folder Structure

```bash
log_classifier_project/
├── processor_regex.py       # Rule-based classification
├── processor_e5.py          # Embedding + classifier logic
├── hybrid_classifier.py     # Combined hybrid logic
├── classify.py              # CLI-based classification
├── train_model.py           # Training script
├── server.py                # FastAPI server (optional)
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
```

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/log-classifier.git
cd log-classifier
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

Make sure to have the following installed:

* `sentence-transformers`
* `scikit-learn`
* `fastapi`
* `uvicorn`
* `python-multipart`

---

## 🚪 Run the App

### 🔹 CLI Classification

```bash
python classify.py
```

### 🌐 Start FastAPI Server

```bash
uvicorn server:app --reload
```

Visit these endpoints:

* Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
* ReDoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

## 📃 Example Input CSV Format

```
timestamp,source,log_message
2025-06-27 07:20:25,ModernCRM,"Email service experiencing issues with sending"
2025-07-12 00:24:16,ModernHR,"nova.osapi_compute.wsgi.server ... status: 200"
```

Output CSV:

```
log_message,predicted_label
User User123 logged in.,User Action
Backup completed successfully.,System Notification
Multiple login failures occurred...,Security Alert
```

---

## 🔒 Disclaimer

This project is for educational purposes only.

© 2025 @Codebasics Inc | @LearnerX Pvt Ltd. All rights reserved.

Developed and maintained by Arjun Patel


