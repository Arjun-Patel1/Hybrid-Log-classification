from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
import io
from hybrid_classifier import hybrid_classify

app = FastAPI(
    title="Hybrid Log Classifier",
    description="Classifies log messages using Regex + Embedding + Logistic Regression",
    version="1.0.0"
)

# Allow CORS (Optional if testing from browser frontend)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Set specific origin in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "Log classification server is running 🚀"}

@app.post("/classify_log/")
def classify_single_log(log_message: str):
    label = hybrid_classify(log_message)
    return {"log_message": log_message, "predicted_label": label}

@app.post("/upload_csv/")
async def classify_logs_csv(file: UploadFile = File(...)):
    contents = await file.read()
    df = pd.read_csv(io.BytesIO(contents))

    if "log_message" not in df.columns:
        return {"error": "CSV must contain a 'log_message' column."}

    df["predicted_label"] = df["log_message"].apply(hybrid_classify)

    output = io.StringIO()
    df.to_csv(output, index=False)
    output.seek(0)

    return {"message": "Classification complete ✅", "preview": df.head(5).to_dict(orient="records")}
