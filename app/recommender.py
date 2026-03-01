from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np


class SHLRecommender:
    def __init__(self, catalogue_df):
        self.model = SentenceTransformer("all-MiniLM-L6-v2")
        self.catalogue = catalogue_df
        self.catalogue_embeddings = self.model.encode(
            catalogue_df["combined_text"].tolist(),
            convert_to_tensor=False
        )

    def recommend(self, job_description, top_k=5):
        job_embedding = self.model.encode([job_description])
        similarities = cosine_similarity(job_embedding, self.catalogue_embeddings)[0]

        top_indices = np.argsort(similarities)[::-1][:top_k]

        job_lower = job_description.lower()

        results = []
        for idx in top_indices:
            assessment = self.catalogue.iloc[idx]

            skill_list = str(assessment["skills"]).lower().split(",")

            matched_skills = [
                skill.strip()
                for skill in skill_list
                if skill.strip() in job_lower
            ]

            if matched_skills:
                reason_text = f"Matches skills: {', '.join(matched_skills)}"
            else:
                reason_text = "High semantic similarity to job description."

            results.append({
                "assessment_id": assessment["assessment_id"],
                "title": assessment["title"],
                "similarity_score": float(similarities[idx]),
                "reason": reason_text
            })

        return results