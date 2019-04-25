#Inheritance
class Animal:
    def __init__(self):
        print("creating object of Animal class");

    def make_sound(self, sound = ""):
        print("Sound: ", sound);


#Extending Animal class
class Dog(Animal):
    def __init__(self):
        Animal.__init__(self);
        print("creating object of Dog class");

    def make_sound(self, sound = "Bhowwww"):
        print("Sound: ", sound);

#Extending Animal class
class Cat(Animal):
    def __init__(self):
        Animal.__init__(self);
        print("creating object of Cat class");

    def make_sound(self, sound = "Mewwww"):
        print("Sound: ", sound);


animal = Animal();
animal.make_sound();
print(type(animal));
print("\n");

animal = Dog();
animal.make_sound();
print(type(animal));
print("\n");

animal = Cat();
animal.make_sound();
print(type(animal));
print("\n");
