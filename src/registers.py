
# class RegisterStuff:

def create_register(size = 8):
    new_register = []
    for x in range(size):
        new_register.append(0)
    print(f'created new_register: {new_register}')
    return new_register

def clear_register(register):
    for i in enumerate(register):
        register[i] = 0
    print(f'register cleared: {register}')
    return register

def destroy_register(register):
    list.clear(register)