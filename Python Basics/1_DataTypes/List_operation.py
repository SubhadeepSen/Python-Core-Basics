objectList = [1,2,"John",4,5];
print("List: ", objectList);

#Length of List
length = len(objectList);
print("Length: ", length);

#Accessing element with index
element_3 = objectList[2];
print("Element at index 3: ", element_3);

#Modifying the 3rd element
objectList[2] = 3;
print("Modifed List: ", objectList);

#SubList
subList = objectList[2:4];
print("Sub List: ", subList);

#SubList with step sizes
subList = objectList[0:5:2];
print("Sub List with step size 2: ", subList);

#Reverse List
revList = objectList[::-1]
print("Reverse List: ", revList);
