#Polymorphism
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


dog = Dog();
cat = Cat();

# Runtime evaluation of the type of object and making call to the respective method
for pet in [dog, cat]:
    print("Type: ", type(pet));
    pet.make_sound();
