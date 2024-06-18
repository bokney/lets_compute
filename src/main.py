
from src.registers import RegisterStuff

test_register = RegisterStuff("Test Register", 11)

test_register.print_register()

test_register.flip_bit(1)
test_register.flip_bit(3)
test_register.flip_bit(5)
test_register.flip_bit(7)

test_register.print_register()

test_register.set_register_length(8)

test_register.print_register()

test_register.flip_bit(0)
test_register.flip_bit(1)
test_register.flip_bit(2)
test_register.flip_bit(3)

test_register.print_register()





# register = [[1, 1, 1, 1, 1, 1, 1, 1],
#             [1, 1, 1, 1, 1, 1, 1, 1],
#             [1, 1, 1, 1, 1, 1, 1, 1],
#             [1, 1, 1, 1, 1, 1, 1, 1]]

# register = {'register': [], }

# REGISTER_SIZE = 8
# REGISTER = []
# REGISTER = REGISTER.append(create_register(REGISTER_SIZE))

# def do_something():
#     print(f'doing something... {REGISTER})
#     pass

# do_something()

# clear_registers()
# print(register)

