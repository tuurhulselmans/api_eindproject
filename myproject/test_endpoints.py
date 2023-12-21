import requests
import pytest

BASE_URL = "http://localhost:8000"  # Replace with your API URL

# Test user data for creation and login
test_user_data = {
    "email": "test@example.be",
    "password": "test_password"
}

# User authentication token
auth_token = None

# Forecast ID placeholder
forecast_id = 1

# User ID placeholder
user_id = 1

# Test for creating a user
def test_create_user():
    global auth_token, user_id
    response = requests.post(f"{BASE_URL}/users/", json=test_user_data)
    assert response.status_code == 200  # Assuming 200 is the success status code
    user_id = response.json().get("id")
    auth_token = response.json().get("access_token")



# Test for user login
def test_user_login():
    global auth_token
    response = requests.post(f"{BASE_URL}/token", data={
        "username": test_user_data["email"],
        "password": test_user_data["password"]
    })
    assert response.status_code == 200  # Assuming 200 is the success status code
    auth_token = response.json().get("access_token")
    assert auth_token is not None


# Test for posting a forecast
def test_post_forecast():
    global auth_token, forecast_id
    headers = {"Authorization": f"Bearer {auth_token}"}
    forecast_data = {
        "city": "YourCity",
        "date": "2024-01-01",
        "description": "Sunny day",
        "temperature_high": 30,
        "temperature_low": 20
    }
    response = requests.post(f"{BASE_URL}/forecast/", headers=headers, json=forecast_data)
    assert response.status_code == 200  # Assuming 200 is the success status code
    forecast_id = response.json().get("id")
    assert forecast_id is not None


# Test for getting forecast data by ID
def test_get_forecast_by_id():
    global auth_token, forecast_id
    headers = {"Authorization": f"Bearer {auth_token}"}
    response = requests.get(f"{BASE_URL}/forecast/{forecast_id}", headers=headers)
    assert response.status_code == 200  # Assuming 200 is the success status code
    forecast_data = response.json()
    assert forecast_data.get("id") == forecast_id


# Test for getting forecast data
def test_get_forecasts():
    global auth_token
    headers = {"Authorization": f"Bearer {auth_token}"}
    response = requests.get(f"{BASE_URL}/forecast/", headers=headers)
    assert response.status_code == 200  # Assuming 200 is the success status code
    forecast_data = response.json()
    assert len(forecast_data) > 0  # Check if the forecast data is received


# Test for getting user data by ID
def test_get_user_by_id():
    global auth_token, user_id
    headers = {"Authorization": f"Bearer {auth_token}"}
    response = requests.get(f"{BASE_URL}/users/{user_id}", headers=headers)
    assert response.status_code == 200  # Assuming 200 is the success status code
    user_data = response.json()
    assert user_data.get("id") == user_id


# Test for getting user data
def test_get_user():
    global auth_token
    headers = {"Authorization": f"Bearer {auth_token}"}
    response = requests.get(f"{BASE_URL}/users/", headers=headers)
    assert response.status_code == 200  # Assuming 200 is the success status code
    user_data = response.json()
    assert len(user_data) > 0  # Check if the user data is received


# Run tests
if __name__ == "__main__":
    pytest.main()
