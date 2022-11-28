import pytest

@pytest.fixture()
def login():
    print('\n这是前置步骤')
    yield
    print('\n这是后置处理')