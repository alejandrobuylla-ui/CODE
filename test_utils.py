from utils import greet, add


def test_greet():
    assert greet("World") == "Hello, World!"
    assert greet("Alejandro") == "Hello, Alejandro!"


def test_add():
    assert add(2, 3) == 5
    assert add(0, 0) == 0
    assert add(-1, 1) == 0
