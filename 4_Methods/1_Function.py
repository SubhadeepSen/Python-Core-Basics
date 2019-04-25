def printer():
    '''It is documentation about the printer() function'''
    print("This is printer() function");


#Calling printer() function
printer();


def add_number(num_1, num_2):
    '''add_number function takes two parameters and return the sum of them'''
    return (num_1 + num_2);

#Calling add_number(10,20) function
result = add_number(10, 20);
print("The sum is : ", result);

def add_number(num_1 = 0, num_2 = 0):
    '''add_number function takes two parameters and return the sum of them.
       If no parameter is passed then it will take the default value.'''
    return (num_1 + num_2);

#Calling add_number() function
result = add_number();
print("The sum is : ", result);


def add_N_Numbers(*args):
    #args is a tuple
    '''add_N_Numbers function takes variable length parameters and return the sum of them'''
    #print(args[2]);    #prints the 3rd number
    #print(len(args));    #prints the length of args
    return (sum(args));

result = add_N_Numbers(10,20,30,40);
print("The sum is : ", result);


def keyword_args(**kwargs):
    #kwargs is a dictionary
    '''keyword_args function takes variable length arguments in key:value pairs'''
    print(kwargs);    #prints the 3rd number
    #print(len(args));    #prints the length of args

keyword_args(apple=10, mango=20)
    
