for i in range(10):
    print(i);

print('----RANGE-----');

for i in range(0,10):
    print(i);

print('----RANGE WITH STEP SIZE-----');

for i in range(0,10,2):
    print(i);

print('\n----FOR LOOP-----');

numbers = [9,8,7,6,5,4,3,2,1];
for n in numbers:
    print("Number: ", n);

print('\n----WHILE LOOP-----');

fruits = ['apple', 'banana', 'orange', 'pineapple', 'watermelon', 'mango'];
i = 0;
while i < len(fruits):
    print("-->", fruits[i]);
    i = i + 1;

print('\n----WHILE LOOP WITH ELSE-----');
names = [];
i = 0;
while i < len(names):
    print(name[i]);
else:
    print("Name list size: ", len(names));
