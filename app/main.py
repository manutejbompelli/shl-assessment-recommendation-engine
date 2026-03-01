from fastapi import FastAPI
from pydantic import BaseModel
from app.data_loader import load_catalogue
from app.recommender import SHLRecommender

app = FastAPI(title="SHL Assessment Recommendation Engine")

catalogue_df = load_catalogue()
recommender = SHLRecommender(catalogue_df)

class JobInput(BaseModel):
    job_description: str
    top_k: int = 5

@app.post("/recommend")
def recommend_assessments(job: JobInput):
    results = recommender.recommend(job.job_description, job.top_k)
    return {"recommendations": results}