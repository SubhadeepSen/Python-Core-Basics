dictionary = {"A":5, "B":4, "C":3, "D":2, "E":1};
print("Dictionary: ", dictionary);

#Length of Dictionary
length = len(dictionary);
print("Length: ", length);

#Accessing element using key
element = dictionary['B'];
print("Element for Key ['B']: ", element);

#Modifying element using key
dictionary['B'] = 9;
element = dictionary['B'];
print("Element for Key ['B']: ", element);
