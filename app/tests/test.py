import pytest
from flask import Flask
from app import app

def test_hello_world():
    client = app.test_client()
    response = client.get('/')
    assert response.status_code == 200
    assert b"<p>Hello, World!</p>" in response.data

