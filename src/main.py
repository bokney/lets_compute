register = [[1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1]]

REGISTER_SIZE = 8
REGISTER_AMOUNT = 4

def clear_registers():
    for x in range(REGISTER_AMOUNT):
        for y in range(REGISTER_SIZE):
            register[x][y] = 0

clear_registers()
print(register)

