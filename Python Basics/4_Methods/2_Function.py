#Inner function

def outer(value = 0):
    print("This is outer outer function call and value = ", value);

    def inner():
        y = value*2;
        print("This is inner outer function call and value = ", y);

    #Inner function must be called from the function itself
    inner();


outer(50);


#function can be returned
def outer():
    def inner():
        print("This is inner function");
    #returning the reference of inner()
    return inner;

inner_function = outer();
inner_function();   #Executing inner function
