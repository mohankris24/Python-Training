import random
print('hello world')
a=4
print(a)
print(random.uniform(7,0))
L = ('Hello World')
print(L.upper())
print(L.lower())
print(L.split())
print(L[::-1])
print(L[1:4])
print(L + ' bye')
# Print formating
first_name = 'Mohan'
last_name = 'krishna'
print(f'First name is {first_name} and last name is {last_name}')

# List
cities = ['bangalore','chennai','mumbai','mysore','delhi']
print(cities)
# List Functions
cities.append('kolkata')
print(cities)
cities.pop(3)
print(cities)
cities.sort()
print(cities)

# Dictionaris
err = {'error1': 'unknown error', 'error2': 'invalid input'}
print(err)
print(err['error1'].upper())



# Tuples (Tuples are list which are immutablity)
tup = ('honda','hyundai','nissan','toyota')
print(tup)
print(tup.count('honda'))

# Booleans, True (T caps) False (F caps)
K=1
J=2
B=1*2
print(B>0)
print(K>J)

# I/O with basic files
spectrum = open("C:\\Users\\mohan\\Desktop\\spectrum.txt")
# seek will reset the cursor
spectrum.seek(0)
print(spectrum.readlines())
spectrum.close()

# Read (with statement) , mode (r-read, a-append, r+ - read and write
with open(r"C:\Users\mohan\Desktop\spectrum.txt") as spectrum_text:
    display_content = spectrum_text.read().splitlines()
    print(display_content)

# Append new data to the file
#with open("C:\\Users\\mohan\\Desktop\\spectrum.txt",mode='a') as spectrum_append:
#    write_content = spectrum_append.write('Python testing 1')
#    print(spectrum_text.read())

# Python Statements
msgs = {'msgs1': 'true', 'msgs2': 'false', 'msgs3': 'invalid'}
print(display_content[0])
if display_content[0] == '8552220102':
    print(msgs['msgs1'])
elif display_content)[0] == ']':
    print(msgs['msgs3'])
else:
    print(msgs['msgs2'])

# For loop
input_var = ''
for for_loop in display_content:
    if str(for_loop) == '':
        for_loop = ' '
    input_var = input_var + for_loop

print(input_var)
counter = 0
for for_loop2 in input_var:
    counter = counter + 1
    if counter == 80:
        break
    else:
        continue

print(counter, 'Characters')
print(for_loop2)

for for_loop3 in range(1):
    print(for_loop3)

# for loop to display dictionary values
for d_keys,d_values in err.items():
    print(d_keys,d_values)

# While loops

x=10
while x<15:
    print(f'The current value of x is {x}')
    x = x + 1
else:
    print('end of loop')

# Zip function
list1=[1,2,3,4,5]
list2=['a', 'b', 'c', 'd']

for for_loop4 in zip(list1,list2):
    print(for_loop4)

# in operator in list and Dictionary

print('error1' in err.keys())
if 'error1' in err.keys():
    print(err['error1'])

print('8552220102' in display_content)

# Min & Max operator

print(min(list1))
print(max(list2))

# Shuffle
from random import shuffle
shuffle(list1)
print(list1)

# Input
mobile_num = input('Enter your phone number')
print(mobile_num)