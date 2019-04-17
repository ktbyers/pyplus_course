def my_add(x, y):
    """Simple function to add two integers together"""
    return x + y


def my_mul(x, y):
    """Simple function to multiply two integers together"""
    return x * y


def test_my_add():
    """Simple test to test the "my_ad" function"""
    assert my_add(5, 11) == 16
    assert my_add(1, 9) == 10


def test_my_mul():
    """Simple test to test the "my_mul" function"""
    assert my_mul(2, 7) == 14
    assert my_mul(9, 9) == 81
