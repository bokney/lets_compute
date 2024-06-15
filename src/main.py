
from src.registers import create_register

# register = [[1, 1, 1, 1, 1, 1, 1, 1],
#             [1, 1, 1, 1, 1, 1, 1, 1],
#             [1, 1, 1, 1, 1, 1, 1, 1],
#             [1, 1, 1, 1, 1, 1, 1, 1]]

# register = {'register': [], }

REGISTER_SIZE = 8
REGISTER = []
REGISTER = REGISTER.append(create_register(REGISTER_SIZE))

def do_something():
    print(f'doing something... {REGISTER})
    pass

do_something()

# clear_registers()
# print(register)

