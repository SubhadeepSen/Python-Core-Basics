class Printer:

    def __init__(self):
        print("calling __init__()");

    def printName(self, name = ""):
        print("Your name is: ",name);


printer = Printer();
print("Printer Object: ", printer);
#print("Printer Object Length: ", len(printer));    #TypeError: object of type 'Printer' has no len()
print("Printer Object String Representation: ", str(printer));
del printer;

print("\n");

class NewPrinter:

    def __init__(self):
        print("calling __init__()");

    def printName(self, name = ""):
        print("Your name is: ",name);

#Overriding the default implementation of the following methods
    def __str__(self):
        return "This is New Printer Object";

    def __len__(self):
        return 0;

    def __del__(self):
        print("Printer Object has been removed from memory");


printer = NewPrinter();
print("Printer Object: ", printer);
print("Printer Object Length: ", len(printer));    #TypeError: object of type 'Printer' has no len()
print("Printer Object String Representation: ", str(printer));
del printer;
