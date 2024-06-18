
class RegisterStuff:

    def __init__(self, name, length):
        self.register = []
        self.register_name = name
        self.register_length = length
        self.set_register_length(length)
        pass

    def set_register_length(self, size = 8):
        self.register.clear()
        for x in range(size):
            self.register.append(0)

    def clear_register(self):
        for i in range(len(self.register)):
            self.register[i] = 0

    def flip_bit(self, bit):
        if (bit < self.register_length):
            if (self.register[bit] == 0):
                self.register[bit] = 1
            else:
                self.register[bit] = 0

    def print_register(self):
        print(f'>> {self.register_name} = {self.register}')

# # # # # # # # # # # # # # # # 

    # def create_register(size = 8):
    #     new_register = []
    #     for x in range(size):
    #         new_register.append(0)
    #     print(f'created new_register: {new_register}')
    #     return new_register
    # def clear_register(register):
    #     for i in enumerate(register):
    #         register[i] = 0
    #     print(f'register cleared: {register}')
    #     return register
    # def destroy_register(register):
    #     list.clear(register)