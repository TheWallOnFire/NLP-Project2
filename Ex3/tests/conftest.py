import pytest
from app.core.schemas import QueryRequest

@pytest.fixture
def sample_query_request():
    return QueryRequest(query="I lost my credit card")

@pytest.fixture
def sample_queries():
    return [
        "What is my balance?",
        "My transfer failed",
        "I lost my card",
        "How do I unblock my account?"
    ]
