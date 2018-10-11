# Upload quiz3.py file to Blackboard - Session 12


def get_middle(a, b):
    '''
    Given 2 lists, a and b, return a new list containing their middle elements.
    '''
    # I am assuming that by middle you mean everything that is not the first and last number, not just one number in the middle of the list
    for i in range(0,len(a)):
        del a[0]
        del a[-1]
    print(a)
    
    for i in range(0,len(b)):
        del b[0]
        del b[-1]
    print(b)

    c = a + b 
    print (c)
   #Add new lists together
    

# Uncomment the following lines to test
# a = [1, 2, 3]
# b = [4, 5, 6, 7]
# c = [8, 9, 10, 11, 12]
# print(get_middle(a, b))
# print(get_middle(a, c))

# Expected output:
# [2, 5, 6]
# [2, 10]

import math

def replace_even(data):
    '''
    Replace all elements at an even index in the list with its square root. If the element at an even index is negative, replace it with 0.
    No return is required.
    data: the list of values to process
    '''
    
    for i in range(0,len(data),2):
        if n is negative:
            data[i] = 0
        else:
            data[i] = math.sqrt(i)
            
    
# Uncomment the following lines to test
# a = [4, 1, 0, 2, -2, 3, 23]
# replace_even(a)
# print(a)

# Expected output:
# [2.0, 1, 0, 2, 0, 3, 4.795831523312719]


def is_increasing(data):
    '''
    Return True if the list is currently sorted in increasing order.
    '''
    for n in range(0, len(data)):
        if [0]<[1]<[2]:
            return True
        else:
            return False 


# Uncomment the following lines to test
# data_1 = [10, 11, 2018]
# data_2 = [11, 10, 2018]
# data_3 = [10, 10, 2018]
# print(is_increasing(data_1))
# print(is_increasing(data_2))
# print(is_increasing(data_3))

# Expected output:
# True
# False
# False


def print_hist(data):
    '''
    given a dictionary of letter: positive integer pairs, 
    print rows with the letter and a number of asterisks equal
    to the positive integer. The rows should be printed in key order.
    No return is required.
    data: a dictionary of letter: positive integer pairs
    Example:
    letter_counts={'C': 6, 'A': 3, 'B': 10, 'Z': 8}
    print_hist(letter_counts)
    Expected output:
    A: ***
    B: **********
    C: ******
    Z: ********
    '''
    for item in sorted(data):
    g = data[x]
    print(x, ":", g*'*')


    # letter_counts={'C': 6, 'A': 3, 'B': 10, 'Z': 8}
    # print_hist(letter_counts)