from fastapi.testclient import TestClient
from app.main import app
from config.config import OrderConfig

client = TestClient(app)


def test_valid_order():
    response = client.post("/api/orders", json={
        "id": "A0000001",
        "name": "Melody Holiday Inn",
        "address": {
            "city": "taipei-city",
            "district": "da-an-district",
            "street": "fuxing-south-road"
        },
        "price": 250,
        "currency": "TWD"
    })
    assert response.status_code == 200


def test_price_exchange():
    response = client.post("/api/orders", json={
        "id": "A0000001",
        "name": "Melody Holiday Inn",
        "address": {
            "city": "taipei-city",
            "district": "da-an-district",
            "street": "fuxing-south-road"
        },
        "price": 20,
        "currency": "USD"
    })
    assert response.status_code == 200
    assert response.json()["currency"] == "TWD"
    assert response.json()["price"] == 20 * OrderConfig.usd2twd_exchange_rate


def test_invalid_currency():
    response = client.post("/api/orders", json={
        "id": "A0000001",
        "name": "Melody Holiday Inn",
        "address": {
            "city": "taipei-city",
            "district": "da-an-district",
            "street": "fuxing-south-road"
        },
        "price": 250,
        "currency": "XYZ"
    })
    assert response.status_code == 400
    assert response.json() == {"detail": "Currency format is wrong"}


def test_negative_price():
    response = client.post("/api/orders", json={
        "id": "A0000001",
        "name": "Melody Holiday Inn",
        "address": {
            "city": "taipei-city",
            "district": "da-an-district",
            "street": "fuxing-south-road"
        },
        "price": -10,
        "currency": "TWD"
    })
    assert response.status_code == 400
    assert response.json() == {"detail": "Can not accept negative price"}


def test_invalid_price():
    response = client.post("/api/orders", json={
        "id": "A0000001",
        "name": "Melody Holiday Inn",
        "address": {
            "city": "taipei-city",
            "district": "da-an-district",
            "street": "fuxing-south-road"
        },
        "price": 2010,
        "currency": "TWD"
    })
    assert response.status_code == 400
    assert response.json() == {"detail": f"Price is over {OrderConfig.price_quota}"}


def test_invalid_name():
    response = client.post("/api/orders", json={
        "id": "A0000001",
        "name": "Melody Holiday Inn123",
        "address": {
            "city": "taipei-city",
            "district": "da-an-district",
            "street": "fuxing-south-road"
        },
        "price": 200,
        "currency": "TWD"
    })
    assert response.status_code == 400
    assert response.json() == {"detail": "Name contains non-English characters"}


def test_capital_name():
    response = client.post("/api/orders", json={
        "id": "A0000001",
        "name": "aMelody Holiday Inn",
        "address": {
            "city": "taipei-city",
            "district": "da-an-district",
            "street": "fuxing-south-road"
        },
        "price": 200,
        "currency": "TWD"
    })
    assert response.status_code == 400
    assert response.json() == {"detail": "Name is not capitalized"}
