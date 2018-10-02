tupleList = (1,2,"John",4,5);
print("Tuple: ", tupleList);

#Length of Tuple
length = len(tupleList);
print("Length: ", length);

#Accessing element with index
tupleList_3 = tupleList[2];
print("Element at index 3: ", tupleList_3);

#Tuple is immutable, hence cannot be modified once created
#tupleList_3[2] = 3;

#SubTuple
subTuple = tupleList[2:4];
print("Sub Tuple: ", subTuple);

#SubTuple with step sizes
subTuple = tupleList[0:5:2];
print("Sub Tuple with step size 2: ", subTuple);

#Reverse Tuple
revTuple = tupleList[::-1]
print("Reverse Tuple: ", revTuple);


