import requests


def test_hello_world_with_pyleniumio(py):
    py.visit('http://localhost:5000')
    assert py.contains('Hello World')


def test_hello_world_with_requests():
    response = requests.get('http://localhost:5000')
    assert response.ok
