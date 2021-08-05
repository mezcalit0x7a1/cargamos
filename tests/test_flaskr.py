# -*- coding: utf-8 -*-
"""
    test.test_flaskr
    ~~~~~~~~~~~~~~
    API test
    :copyright: (c) 2021 by Luis Rdz
"""
import pytest
import asyncio
from app import app
from random import randint


@pytest.fixture
def client():
    """Get app object

    Yields:
        object: Flask app
    """    
    with app.test_client() as client:
        with app.app_context():
            pass
        yield client


def test_add_inventory(client):
    """Get products from a store, then add stock

    Args:
        client (object): Flask app
    """    
    response = client.get("/store_products/stores/1")
    json_data = response.get_json()
    assert response.status_code == 200
    for data in json_data["resource"]:
        id = data["id"]
        sku = data["sku"]
        stock = data["stock"]
        price = data["price"]
        product_id = data["product_id"]
        store_id = data["store_id"]
        if stock < 5:
            new_stock = randint(50, 150)
            req_data = {"sku": sku, "stock": new_stock, "price": price, "product_id": product_id, "store_id": store_id}
            print(f"Adding store products to id ---> {id}")
            update_response = client.put(f"/store_products/{id}", json=req_data)
            assert update_response.status_code == 204


def test_get_stores(client):
    """Get stores

    Args:
        client (object): Flask app
    """    
    response = client.get("/stores")
    assert response.status_code == 200


def test_get_store(client):
    """Get store by id

    Args:
        client (object): Flask app
    """
    response = client.get("/stores/3")
    assert response.status_code == 200


# def test_create_stores(client):
#     data = {
#         'name': 'La tienda de los testeos',
#         'address': 'El más allá #333, col. Algo',
#         'city': 'Solidaridad',
#         'state': 'Quintana Roo',
#         'zip_code': '1999',
#         'phone': '9980908765',
#         'email': 'test@gmail.com',
#     }
#     response = client.post('/stores', json=data)
#     assert response.status_code == 201


def test_update_stores(client):
    """Make a test updating a store

    Args:
        client (object): Flask app
    """    
    data = {
        "name": "Gamer Store",
        "address": "Fornite #123 col. Sin Tiempo",
        "city": "Solidaridad",
        "state": "Quintana Roo",
        "zip_code": "1234",
        "phone": "9847658900",
        "email": "gamerstore@gmail.com",
    }
    response = client.put("/stores/6", json=data)
    assert response.status_code == 204


def test_unique_keys(client):
    """Make a test with UNIQUE attributes

    Args:
        client (object): Flask app
    """    
    data = {"sku": "WEBUSB9087234", "stock": 98, "price": 666, "product_id": 6, "store_id": 1}
    response = client.post("/store_products", json=data)
    assert response.status_code == 400


async def buy(client, data, number):
    """Execute asyncio to remove products from stock

    Args:
        client (object): Flask app
        data (dict): data request
        number (int): iteration number
    """    
    log = {"request": number, "quantity": data["quantity"], "response_code": 0, "message": "", "stock": "?"}
    response = client.patch("/store_products/1", json=data)
    json_data = response.get_json()
    log["response_code"] = response.status_code
    if response.status_code == 400:
        log["message"] = json_data["message"]
        assert json_data["message"] == "Out of stock" or json_data["message"] == "Invalid quantity"
    elif response.status_code == 200:
        log["stock"] = json_data["resource"]["stock"]
        assert json_data["resource"]["stock"] >= 0
    if response.status_code == 500:
        log["message"] = json_data["message"]
        assert True
    return log


async def main(client):
    """Async function to log how products are removed from stock

    Args:
        client (object): Flask app
    """    
    tasks = []
    for number in range(0, 150):
        quantity = randint(1, 7)
        data = {"quantity": quantity}
        tasks.append(asyncio.ensure_future(buy(client, data, number)))

    responses = await asyncio.gather(*tasks)
    for log in responses:
        num = log["request"]
        quantity = log["quantity"]
        code = log["response_code"]
        msg = log["message"]
        stock = log["stock"]
        print(f"#{num}, Buy {quantity} items, Response code {code}, Message -> {msg}, {stock} In stock")


def testing_stock(client):
    """Execute asyncio to remove products from stock

    Args:
        client (object): Flask app
    """    
    asyncio.run(main(client))
