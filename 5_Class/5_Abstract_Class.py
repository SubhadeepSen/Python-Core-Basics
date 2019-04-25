#Abstract class
class Animal:
    def __init__(self):
        print("creating object of Animal class");

    def make_sound(self, sound = ""):
        raise NotImplementedError("Sub class must implement this abstract method!");


#animal = Animal();
#animal.make_sound();

#Extending Animal class
class Dog(Animal):
    def __init__(self):
        Animal.__init__(self);
        print("creating object of Dog class");

    def make_sound(self, sound = "Bhowwww"):
        print("Sound: ", sound);


dog = Dog();
dog.make_sound();
