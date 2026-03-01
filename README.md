# SHL Assessment Recommendation Engine


🔗 **Live API:**  
https://shl-assessment-recommendation-engine-02wl.onrender.com  

📘 **API Documentation (Swagger):**  
https://shl-assessment-recommendation-engine-02wl.onrender.com/docs

---

## Problem Statement

Given a job description, recommend the most relevant SHL assessments from the product catalogue.

The system should intelligently match job requirements with assessments based on skills and description similarity.

---

## Approach

This solution uses semantic text embeddings to compare job descriptions with SHL assessment descriptions.

### Steps:

1. Combine assessment title, description, and skills into a single text representation.
2. Convert all assessment texts into vector embeddings using a pre-trained Sentence Transformer model.
3. Convert the input job description into an embedding.
4. Compute cosine similarity between job embedding and assessment embeddings.
5. Return the top-k most similar assessments.
6. Provide a simple explanation by highlighting matched skills.

---

## Model Used

- Model: `all-MiniLM-L6-v2`
- Library: `sentence-transformers`

### Why this model?

- Captures semantic meaning (not just keyword matching)
- Handles paraphrasing effectively
- Lightweight and efficient
- Suitable for small-to-medium catalog size

---

## Architecture Overview
Job Description
↓
Sentence Transformer Embedding
↓
Cosine Similarity Calculation
↓
Top-K Ranking
↓
API Response (with similarity score + explanation)

---

## Tech Stack

- Python 3.10
- FastAPI
- Sentence Transformers
- Scikit-learn
- Uvicorn

---

## How to Run Locally

1. Create virtual environment:
python -m venv venv
venv\Scripts\activate


2. Install dependencies:
pip install -r requirements.txt


3. Run server:
uvicorn app.main:app --reload

4. Open Swagger UI:
http://127.0.0.1:8000/docs

---

## API Usage

### Endpoint

POST `/recommend`

### Example Request

```json
{
"job_description": "Looking for a data analyst with strong SQL and Python skills",
"top_k": 3
}

Example Response
{
  "recommendations": [
    {
      "assessment_id": "A4",
      "title": "Data Analyst Assessment",
      "similarity_score": 0.59,
      "reason": "Matches skills: sql"
    }
  ]
}
---

## Design Decisions

- **Semantic embeddings instead of TF-IDF**:  
  TF-IDF relies on keyword overlap, while sentence transformers capture contextual meaning. This improves matching quality for paraphrased job descriptions.

- **Cosine similarity for ranking**:  
  Cosine similarity efficiently measures closeness between embedding vectors.

- **Precomputed catalogue embeddings**:  
  Assessment embeddings are computed once during startup to reduce inference latency.

- **Explainability layer added**:  
  A simple skill-matching logic is included to provide human-readable reasoning alongside similarity scores.

---

## Scalability Considerations

For larger catalogues, the following improvements can be implemented:

- Use FAISS or another vector database for faster similarity search.
- Store embeddings in a persistent database.
- Add caching for frequently requested job descriptions.
- Deploy using containerized infrastructure (Docker + Cloud deployment).

---

## Future Improvements

- Add filtering by experience level or industry.
- Add skill-weight boosting mechanism.
- Integrate a real SHL catalogue dataset.
- Add logging and monitoring for production use.