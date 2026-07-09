class Dog:
    '''a simple class ...of Dog'''
    def __init__(self, name, age, weight):
        self.ten = name
        self.tuoi = age
        self.nang = weight
    def sit(self):
        '''docstring of method 1'''
        print('sitting')
    def roll(self):
        '''docstring of method 2'''
        print('rolling')

my_dog = Dog('Xoai', '2kg', 2)
print(my_dog.name)