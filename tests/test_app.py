import pytest
from fastapi.testclient import TestClient

from main import app

payload = {
    "posts": [
        {
            "id": "a0f5b8bf-abef-4053-a833-0725f10b6c08",
            "created_at": "2017-03-31T14:24:07.000000",
            "author_id": "a0f5b8bf-abef-4053-a833-0725f10b6a08",
            "is_repost": False,
            "text": "#lebron is the best",
            "hashtags": ["#lebron"],
        },
        {
            "id": "a0f5b8bf-abef-4053-a833-0725f10b6c08",
            "created_at": "2017-03-31T14:24:07.000000",
            "author_id": "a0f5b8bf-abef-4053-a833-0725f10b6a09",
            "is_repost": False,
            "text": "How can he still do it/?? #lebron",
            "hashtags": ["#lebron"],
        },
    ],
    "accounts": [
        {
            "id": "a0f5b8bf-abef-4053-a833-0725f10b6a09",
            "created_at": "2017-03-31T14:24:07.000000",
            "screen_name": "lebron_number_one_goat",
        },
        {
            "id": "a0f5b8bf-abef-4053-a833-0725f10b6a08",
            "created_at": "2017-03-31T14:24:07.000000",
            "screen_name": "lebron_number_one_goooatt",
        },
    ],
    "hashtag": "#covid",
    "min_similarity": 0.5,
}


def test_get_prediction():
    with TestClient(app) as client:
        # The FastAPI test client does not support JSON in
        # GET requests
        with pytest.raises(TypeError):
            response = client.get("/", json=payload)
            assert response.status_code == 200
