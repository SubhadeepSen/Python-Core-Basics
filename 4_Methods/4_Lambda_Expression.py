#def square(num):
#    return num**2;

#lambda expression of the above function
square = lambda num: num**2;

numbers = [1,2,3,4,5,6,7,8];

#passing lambda expression instead function
squares = list(map(square, numbers));
print("Squares List", squares);

#def even_square(num):
#    if num%2==0:
#        return num;

#lambda expression of the above function
even_square = lambda num: num%2==0;

#passing lambda expression instead function
even_squares = list(filter(even_square, squares));
print("Even Squares List", even_squares);
