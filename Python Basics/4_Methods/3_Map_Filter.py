def square(num):
    return num**2;


numbers = [1,2,3,4,5,6,7,8];

#Using for loop
for n in numbers:
    print("Square of {} is {}".format(n, square(n)));


#Using map() function we can map a function to a list of elements
#map(functionNeedsToBeExecuted, listOfElemetns)
#returns map object
print(map(square, numbers));

for n in map(square, numbers):
    print(n);

squares = list(map(square, numbers));
print("Squares List", squares);

def even_square(num):
    if num%2==0:
        return num;

#Using filter() function
#filter(functionNeedsToBeExecuted, listOfElemetns)
even_squares = list(filter(even_square, squares));
print("Even Squares List", even_squares);
