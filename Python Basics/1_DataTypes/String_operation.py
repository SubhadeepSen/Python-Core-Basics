name = "Subhadeep Sen";
print("Name: ", name);

#Length of a given string
length = len(name);
print("Length: ", length);

#Character at particular index
name_0 = name[0];
print("Name[0]: ", name_0);

name_5 = name[5];
print("Name[5]: ", name_5);

#Substring
# str[startIndex:lastIndex]
firstName = name[0:9];
print("First Name: ", firstName);

#Substring from startIndex to last of the string
# str[startIndex:]
lastName = name[10:];
print("Last Name: ", lastName);

#Substring with step size
# str[startIndex:lastIndex:stepSize]
steppedName = name[0:9:2];
print("Stepped Name: ", steppedName);

#Read string from the end
lastChar = name[-1];
print("Last Character: ", lastChar);

last_5_Char = name[-5];
print("Last 5th Character: ", last_5_Char);

#Reverse String
reverse_name = name[::-1];
print("Reverse Name: ", reverse_name);

#String concatenation
firstName = "Sunny";
concatedString = "Hello " + firstName + ", how are you?";
print(concatedString);

#String is immutable
#Uncomment the below line and you will see,
#TypeError: 'str' object does not support item assignment
#name[0] = "K";

#String formatting
print("You name is {name}".format(name="Subhadeep Sen"));
print("You name is {name} and age is {age}".format(name="Subhadeep Sen", age=25));
name="Subhadeep Sen";
age=25;
print("You name is {0} and age is {1}".format(name, age));
salary = 25312.45975;
print("You name is {0} and age is {1} and salary is {2:5.2f}".format(name, age, salary))
