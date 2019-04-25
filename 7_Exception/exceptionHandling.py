
try:
    #calling arbitary method which does not exist
    one();
except:
    print("Method does not exist");
finally:
    print("Executing finally block");


def division(num_1, num_2):
    if num_2==0:
        raise ZeroDivisionError('Second parameter cannot be zero');
    else:
        return (num_1 / num_2);


#division(10,0);
    
try:
    division(10,0);
except ZeroDivisionError:
    print("cannot be divided by zero");
