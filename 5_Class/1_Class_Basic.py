class Printer:

    def __init__(self):
        print("calling __init__()");

    def printName(self, name=""):
        print("Your name is: ",name);


#creating the object of Printer class
#The constructor AKA __init__ will be called
printer = Printer();
printer.printName("Subhadeep Sen");
print("\n");

# Any method defined in a Class always takes self as the first paramter whether
# it takes any other parameter or not.
# This self parameter refers to the object itself


class Calculator:

    def __init__(self):
        print("Creating object of calculator class");

    def add(self, n1 = 0, n2 = 0):
        return (n1 + n2);

    def sub(self, n1 = 0, n2 = 0):
        return abs(n1 - n2);

    def mul(self, n1 = 0, n2 = 0):
        return (n1 * n2);

    def div(self, n1 = 0, n2 = 1):
        result = 0;
        if (n2!= 0):
            result = (n1 / n2);
        return result;


cal = Calculator();
result = cal.add(20,10);
print("Addition: ", result);

result = cal.sub(20,10);
print("Subtraction: ", result);

result = cal.mul(20,10);
print("Multiplication: ", result);

result = cal.div(20,10);
print("Division: ", result);
