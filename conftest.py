import pytest
from api import Restful

@pytest.fixture(scope='session')
def client():
    client = Restful('http://localhost:32768')
    return client
