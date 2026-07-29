from fastapi import FastAPI
import joblib
from src.preprocessing import clean_resume
app = FastAPI()

from fastapi import FastAPI

app = FastAPI()

model = joblib.load("models/model.pkl")
vectorizer = joblib.load("models/vectorizer.pkl")
encoder = joblib.load("models/label_encoder.pkl")

@app.get("/")
def home():
    return {
        "message": "Resume MLDevOps API is running!"
    }
    
from pydantic import BaseModel

class ResumeInput(BaseModel):
    resume: str
    
@app.post("/predict")
def predict(data: ResumeInput):

    cleaned = clean_resume(data.resume)

    vector = vectorizer.transform([cleaned])

    prediction = model.predict(vector)

    category = encoder.inverse_transform(prediction)

    return {
      "result": "success",
        "Predicted Category": category[0]
    }