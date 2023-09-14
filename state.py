class Human:
    def __init__(self):
        self.name = 'I am nameless'
        # height = self.height
        # complexion = self.complexion
        # race = self.race 

    # def __add__(self, other):
    #     return str(self.height + other.height)

    def introduce(self):
        print('My name is {}'.format(self.name))

    def changename(self):
        self.name = str(input('Name change: '))

        

class Male(Human()):
    def __init__(self):
        self.gender = 'Male'
        
    def gendercheck(self):
        print('I am a Human {}'. format(self.gender))


class Female(Human()):
    def __init__(self):
        self.gender = 'Female'
        
    def gendercheck(self):
        print('I am a Human {}'. format(self.gender))


# Evan = Human()
# print(Evan.name)
# Evan.introduce()

# Evan.changename()
# Evan.introduce()

Adam = Male()
print(Adam.gendercheck())
# print(Adam.changename())
# print(Adam.introduce())

print('\n\n\n')

Eve = Female()
print(Eve.gendercheck())
# print(Eve.changename())
# print(Eve.introduce())