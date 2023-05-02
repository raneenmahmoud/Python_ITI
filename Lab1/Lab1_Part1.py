#Part One 

"""
1-Write a Python program which accepts the user's first and last name and print them in
reverse order with a space between them.

"""
print('Enter your first and last name: ')
first_name = input('\n Fist Name is ')
last_name = input('\n Last Name is ')
print(f'{first_name[::-1]} {last_name[::-1]}')
#------------------------------------------------------------------------

"""
2-Write a Python program that accepts an integer (n) and computes the value of
n+nn+nnn.
"""
n=input("Enter a Number:\n")
print (int(n)+int(n+n)+int(n+n+n))
#--------------------------------------------------------------------------

"""
3- Write a Python program to print the following here document.
Sample string :
"""
paragraph = """a string that you "don't" have to escape
This
is a ....... multi-line
heredoc string --------> example"""
print(paragraph)
#--------------------------------------------------------------------------

"""
4- Write a Python program to
 get the volume of a sphere with radius 6.
"""
import math
def get_volume_of_sphere(radius):
    return (4/3) * math.pi * radius ** 3
volume = get_volume_of_sphere(6)
print(f'volume of shpere is {volume}')
#--------------------------------------------------------------------------

"""
5- Write a Python program that will accept the base and height of a triangle and compute
the area.
"""     
def get_triangle_area(base, height):
    area = 0.5 * int(base) * int(height)
    return area

base = input('Enter the base of triangle: ')
height = input('\nEnter the height of triangle: ')
print('Area of triangle is: ', get_triangle_area(base, height))
#--------------------------------------------------------------------------

"""
6- Write a Python program to construct the following pattern, using a nested for loop.
"""
# paragraph = """Search about method
# end=””
# *
# * *
# * * *
# * * * *
# * * * * *
# * * * *
# * * *
# * *
# *"""
# print(paragraph)

for i in range(5):
    for j in range(i + 1):
        print("*", end=" ")
    print()


for i in range(4, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()
#--------------------------------------------------------------------------

"""
7- Write a Python program that accepts 
a word from the user and reverse it
"""
word = input('Enter the word: ')
print(f'{word[::-1]}')
#--------------------------------------------------------------------------

"""
8- Write a Python program that prints all 
the numbers from 0 to 6 except 3 and 6.
"""
for i in range(7):
    if i == 3 or i == 6:
        continue
    print(i)
#--------------------------------------------------------------------------

"""
9-Write a Python program to get 
the Fibonacci series between 0 to 50
"""
a, b = 0, 1
while b <= 50:
    print(b, end=' ')
    a, b = b, a+b
#--------------------------------------------------------------------------

"""
10- Write a Python program that accepts a string
 and calculate the number of digits and
letters.
"""
def get_num_digits_and_letters(string):
    count_digits = 0
    count_letters = 0
    for char in string:
        if char.isdigit():
            count_digits +=1
        elif char.isalpha():
            count_letters +=1
    print (f'Count of digits in string is: {count_digits} and Count of letters in string is: {count_letters}')

string = input('Enter the string: ')
get_num_digits_and_letters(string)
