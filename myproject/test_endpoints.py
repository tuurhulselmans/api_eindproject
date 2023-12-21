import requests
import pytest

# De basis-URL van je API
BASE_URL = "http://localhost:8000"

# Test voor het GET-eindpunt '/forecast/'
def test_get_forecasts():
    response = requests.get(f"{BASE_URL}/forecast/")
    assert response.status_code == 200  # Controleer of de statuscode 200 is (OK)


# Test voor het GET-eindpunt '/forecast/{forecast_id}'
def test_get_forecast_by_id():
    forecast_id = 1  # Voer de test uit met een bestaand forecast_id
    response = requests.get(f"{BASE_URL}/forecast/{forecast_id}")
    assert response.status_code == 200  # Controleer of de statuscode 200 is (OK)
    forecast_data = response.json()
    assert forecast_data["city"] == "Turnhout"  # Validate if the city is Turnhout
    assert forecast_data["date"] == "21-12-2023"
    assert forecast_data["description"] == "Regen"
    assert forecast_data["temperature_high"] == 8
    assert forecast_data["temperature_low"] == 5
    assert forecast_data["id"] == 1

# Test voor het GET-eindpunt '/forecast_ordered/{city}'
def test_get_forecast_ordered_by_city():
    city = "Turnhout"  # Voer de test uit met een bestaande stad
    response = requests.get(f"{BASE_URL}/forecast_ordered/{city}")
    assert response.status_code == 200  # Controleer of de statuscode 200 is (OK)
    forecasts_data = response.json()
    for forecast_data in forecasts_data:
        assert forecast_data["city"] == "Turnhout"

# Test voor het GET-eindpunt '/locations/{location_id}'
def test_get_location_by_id():
    location_id = 1  # Voer de test uit met een bestaand location_id
    response = requests.get(f"{BASE_URL}/locations/{location_id}")
    assert response.status_code == 200  # Controleer of de statuscode 200 is (OK)


# Test voor het GET-eindpunt '/users/'
def test_get_users():
    response = requests.get(f"{BASE_URL}/users/")
    assert response.status_code == 200  # Controleer of de statuscode 200 is (OK)


# Test voor het GET-eindpunt '/users/{user_id}'
def test_get_user_by_id():
    user_id = 1  # Voer de test uit met een bestaand user_id
    response = requests.get(f"{BASE_URL}/users/{user_id}")
    assert response.status_code == 200  # Controleer of de statuscode 200 is (OK)
    forecast_data = response.json()
    assert forecast_data["email"] == "test@test.be"



# Test uitvoeren met pytest
if __name__ == "__main__":
    pytest.main()
