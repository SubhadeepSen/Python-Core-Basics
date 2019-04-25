#importing individual functions
#from simpleModule import printer
#from simpleModule import add_numbers

#importing multiple functions
#from simpleModule import printer,add_numbers

#importing the complete module
from simpleModule import*

printer();
result = add_numbers(10, 20);
print(result);

#importing the function with alias
from simpleModule import add_numbers as adder
result = adder(20, 20);
print(result);
