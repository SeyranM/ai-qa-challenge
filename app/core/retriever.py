import os, pandas as pd
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

KB_PATH = os.getenv("KB_PATH", "data/faq.csv")
_df = pd.read_csv(KB_PATH)
_model = SentenceTransformer("all-MiniLM-L6-v2")
_vectors = _model.encode(_df["question"].tolist())

def retrieve(query: str, k: int = 3):
    q_vec = _model.encode([query])
    sims = cosine_similarity(q_vec, _vectors)[0]
    idx = sims.argsort()[-k:][::-1]
    return _df.iloc[idx][["question", "answer"]].to_dict("records")
