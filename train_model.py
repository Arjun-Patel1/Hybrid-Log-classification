import pandas as pd
from sentence_transformers import SentenceTransformer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import joblib
import os

# ✅ Use your existing dataset path
csv_path = 'training/dataset/synthetic_logs.csv'

# ✅ Load data
if not os.path.exists(csv_path):
    raise FileNotFoundError(f"CSV file not found at: {csv_path}")

df = pd.read_csv(csv_path)

# ✅ Filter rows that have target labels
df = df[df['target_label'].notnull()]

# ✅ Prepare embeddings
model = SentenceTransformer('intfloat/e5-small-v2')
log_texts = ["passage: " + msg for msg in df['log_message']]
embeddings = model.encode(log_texts, convert_to_numpy=True)
labels = df['target_label'].values

# ✅ Train/test split
X_train, X_test, y_train, y_test = train_test_split(embeddings, labels, test_size=0.3, random_state=42)
clf = LogisticRegression(max_iter=1000)
clf.fit(X_train, y_train)

# ✅ Save model
os.makedirs("models", exist_ok=True)
joblib.dump(clf, 'models/log_classifier.joblib')

# ✅ Evaluate model
y_pred = clf.predict(X_test)
print(classification_report(y_test, y_pred))
