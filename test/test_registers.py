from src.registers import RegisterStuff

RegisterStuff

def test_register_is_within_bounds():
    test_length = 11
    expected = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    result = create(test_length)
    assert result == expected

def test_size_unmodified():
    test_register = [1, 0, 1, 1, 1, 1, 0, 1]
    test_size = 11
    expected = 11

def test_register_cleared():
    test_register = [1, 0, 1, 1, 1, 1, 0, 1]
    expected      = [0, 0, 0, 0, 0, 0, 0, 0]
    clear(test_register)
    assert test_register == expected