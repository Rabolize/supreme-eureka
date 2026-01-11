import pytest
from fastapi.testclient import TestClient
from src.app import app

client = TestClient(app)

def test_get_activities():
    response = client.get("/activities")
    assert response.status_code == 200
    assert isinstance(response.json(), dict)


def test_signup_activity():
    # Use a known activity name and email
    activities = client.get("/activities").json()
    if not activities:
        pytest.skip("No activities available to test signup.")
    activity_name = list(activities.keys())[0]
    email = "testuser@example.com"
    response = client.post(f"/activities/{activity_name}/signup?email={email}")
    assert response.status_code in (200, 400)  # 400 if already signed up
    # Check for expected keys in response
    assert "message" in response.json() or "detail" in response.json()
