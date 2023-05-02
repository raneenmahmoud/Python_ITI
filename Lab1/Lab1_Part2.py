"""
 1- Given a list of numbers, create a function that returns a list where all similar adjacent
    elements have been reduced to a single element, so [1,2,3.3] returns [1,2,3]
"""
# my_list = [1, 2, 3.3]

# def reduce_to_single_element(list):
#     adj_list = []
#     for element in list:
#         adj_element = round(element)
#         adj_list.append(adj_element)
#     return adj_list

# print (reduce_to_single_element(my_list))

# def check_for_uniqness(my_list):
#     unique_list = list(set(my_list))
#     return unique_list

# input_list = input("Enter list of elements sepsrated by , to know whether unique or not :\n")
# input_list = input_list.split(',')

# result = check_for_uniqness(input_list)
# print('Your list without dupliacte values is',result)
#--------------------------------------------------------------------------

"""
 2- Consider dividing a string into two halves
"""
"""
Case1:
    The length is even, the front and back halves are the same length
"""
# a_string  = input("Enter a String:\n")
# b_string = input("Enter a String:\n")

# a_front_length  = int(len(a_string)/2)
# b_front_length  = int(len(b_string)/2)
    
# def check_string_length(a_string, b_string):
#     if len(a_string)%2 == 0:
#         a_front = a_string[:a_front_length]
#         a_back  = a_string[a_front_length : len(a_string)]
#     else:
#         a_front = a_string[:a_front_length +1]
#         a_back = a_string[a_front_length +1 : len(a_string)]

#     if len(b_string)%2 == 0:
#         b_front = b_string[:b_front_length]
#         b_back  = b_string[b_front_length : len(b_string)]    
#     else:
#         b_front = b_string[:b_front_length +1]
#         b_back  = b_string[b_front_length +1: len(b_string)]

#     return a_front + b_front + a_back + b_back

# result = check_string_length(a_string, b_string)
# print(result) 
#--------------------------------------------------------------------------
"""
3- Write a Python function that takes a sequence of numbers and determines whether 
    all the numbers are different from each other.
"""
# def check_for_uniqness(my_list):
#     unique_list = list(set(my_list))
#     if len(my_list) == len(unique_list):
#         return True
#     return False

# input_list = input("Enter list of elements sepsrated by , to know whether unique or not :\n")
# input_list = input_list.split(',')

# result = check_for_uniqness(input_list)
# print('Is Your List Unique? ' , result)
#--------------------------------------------------------------------------
"""
4-Given unordered list, sort it using algorithm bubble sor
"""
# def bubble_sort(list):
#     n = len(list)
#     for i in range(n):
#         for j in range(0, n-i-1):
#             if list[j] > list[j+1] :
#                 list[j], list[j+1] = list[j+1], list[j]
#     return list

# input_list = input("Enter list of elements sepsrated by , to know whether unique or not :\n")
# input_list = input_list.split(',')
# sorted_list = bubble_sort(input_list)
# print(sorted_list) 
#--------------------------------------------------------------------------
"""
5- Gusses game
"""

import random

def guess_number():

    random_number = random.randint(1, 100)
    tries = 10
    guessed_numbers = []

    while tries > 0:
        guess_number = input('Enter your guessed number, it must be between 1, 100:')

        if not guess_number.isdigit() or int(guess_number) < 1 or int(guess_number) > 100:
            print("invalid input. Please enter an integer number between 1 and 100.")
            continue

        guess_number = int(guess_number)

        if guess_number in guessed_numbers:
            print("You already entered this number before. Please enter another different integer.")
            continue

        guessed_numbers.append(guess_number)

        if guess_number == random_number:
            print("Congratulations!. A number you guessed is correct in", 10-tries+1, "tries" )
            play_again()

        elif guess_number > random_number:
            print("This is wrong number. A number you guess must be lower than ", guess_number)
        
        else:
            print("This is wrong number. A number you guess must be greater than ", guess_number)

        tries -=1

    print("You didn't guess the number. The number was", random_number)    
    play_again()

def play_again():
    playing_again = input('Do you want to play again y or n:')
    if playing_again.lower() == "y":
        guess_number()
    else:
        print('Thanks for playing!')
    
guess_number()
