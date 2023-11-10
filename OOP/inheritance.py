# base inheritance

class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f'I am {self.name} and I am {self.age} years old')

    def speak(self):
        print('no speak')


class Cat(Pet):
    def __init__(self, name, age, color):
        super().__init__(name, age)  # récupérer name age de Pet, call the super class
        self.color = color

    def speak(self):
        print('Meow')

    def show(self):
        print(f'I am {self.name} and I am {self.age} years old and I am {self.color}')


class Dog(Pet):
    def speak(self):
        print('Bark')


class Fish(Pet):
    pass


p = Pet('Tim', 19)
p.show()
c = Cat('Bill', 34, 'blue')
c.show()
c.speak()
d = Dog('Jill', 25)
d.show()
d.speak()
f = Fish('Bubble', 4)
f.speak()
