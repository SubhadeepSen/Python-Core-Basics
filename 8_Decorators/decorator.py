# This is the original function
def printer():
    print("This is printer function");


#This is the function which adds some extra features to printer() function
#by creating new function defintion.
#To avail the new features user will have to call this new defintion of the function()
def new_printer(original_func):
    def wrap_func():
        print("executing some code before printer() function");
        original_func();
        print("executing some code after printer() function");
    return wrap_func;

printer();
print("\n")
printer_new = new_printer(printer);
printer_new();

print("\n");
#We can add some extra features to an existing function without calling the new
#definition of the function by using decorator

def decorated_say_hello(original_func):
    def wrap_func():
        print("Executing new definition");
        original_func();
    return wrap_func;
    
@decorated_say_hello
def say_hello():
    print("Hello");

say_hello();
