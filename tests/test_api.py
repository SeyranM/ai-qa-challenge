from fastapi.testclient import TestClient
from app.main import app
c = TestClient(app)

def test_ask():
    r = c.post("/api/ask", json={"question":"return policy"})
    assert r.status_code == 200 and "answer" in r.json()
