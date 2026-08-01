from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_health_endpoint():
    response = client.get("/api/v1/system/health")

    assert response.status_code == 200


def test_research_requires_query():
    response = client.post(
        "/api/v1/research",
        json={}
    )

    assert response.status_code == 422


def test_research_invalid_query_type():
    response = client.post(
        "/api/v1/research",
        json={"query": 123}
    )

    assert response.status_code == 422


def test_research_endpoint(monkeypatch):

    def mock_run_research(query):
        return {
            "report": "Mock research report",
            "evaluation": {
                "score": 0.9,
                "groundedness": 0.9,
                "relevance": 0.9
            }
        }

    monkeypatch.setattr(
        "app.api.routes.research_routes.run_research",
        mock_run_research
    )

    response = client.post(
        "/api/v1/research",
        json={"query": "Explain RAG"}
    )

    assert response.status_code == 200

    data = response.json()

    assert data["report"] == "Mock research report"
    assert "evaluation" in data