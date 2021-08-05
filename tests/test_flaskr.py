import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        with app.app_context():
            pass
        yield client

def test_get_stores(client):
    response = client.get('/stores')
    assert response.status_code == 200

def test_get_store(client):
    response = client.get('/stores/3')
    assert response.status_code == 200

def test_create_stores(client):
    data = {
        'name': 'La tienda de los testeos',
        'address': 'El más allá #333, col. Algo',
        'city': 'Solidaridad',
        'state': 'Quintana Roo',
        'zip_code': '1999',
        'phone': '9980908765',
        'email': 'test@gmail.com'
    }
    response = client.post('/stores', json=data)
    assert response.status_code == 201

def test_update_stores(client):
    data = {
        'name': 'Tienda su sagrada actualización',
        'address': 'Test #987, col. Ceviche',
        'city': 'Solidaridad',
        'state': 'Quintana Roo',
        'zip_code': '1999',
        'phone': '9841256956',
        'email': 'updated@gmail.com'
    }
    response = client.post('/stores/4', json=data)
    assert response.status_code == 204