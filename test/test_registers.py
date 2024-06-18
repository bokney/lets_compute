from src.registers import RegisterStuff

def test_register_is_defined_length():
    test_length = 11
    test_name = "test_register"
    test_register = RegisterStuff(test_name, test_length)
    expected =       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    not_expected_1 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    not_expected_2 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    result = test_register.register
    assert result == expected
    assert result != not_expected_1
    assert result != not_expected_2

def test_length_remains_unmodified():
    initial_length = 8
    updated_length = 5
    test_name = "test_register"
    test_register = RegisterStuff(test_name, initial_length)
    assert initial_length == 8
    assert len(test_register.register) == initial_length
    test_register.set_register_length(updated_length)
    assert updated_length == 5
    assert len(test_register.register) == updated_length

# def test_register_cleared():
#     test_register = [1, 0, 1, 1, 1, 1, 0, 1]
#     expected      = [0, 0, 0, 0, 0, 0, 0, 0]
#     clear(test_register)
#     assert test_register == expected