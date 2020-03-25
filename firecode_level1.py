'''
Given an list containing 9 numbers ranging from 1 to 10, write a function to find the missing number. 
Assume you have 9 numbers between 1 to 10 and only one number is missing.

input_list: [1, 2, 4, 5, 6, 7, 8, 9, 10]
find_missing_number(input_list) => 3



def find_missing_number(list_numbers):
    return (sum(list(range(1,11)))- sum(list_numbers))

print(find_missing_number ([1, 2, 4, 5, 6, 7, 8, 9, 10]))
    
'''

'''
You are given an m x n 2D image matrix (List of Lists) 
where each integer represents a pixel. Flip it in-place along its vertical axis.

Example:
Input image :
1 0              
1 0 

Modified to :
0 1              
0 1


NOTE!!! Your code runs in O(n^2). The solution is in O(n). Improve!
  

def flip_vertical_axis(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            placeholder = matrix[i][0] #1, 4, 7
            if j==(len(matrix[i])-1):
                matrix[i][0]=matrix[i][j]
                matrix[i][j]=placeholder
    return matrix

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print (flip_vertical_axis(matrix))
'''  



'''
A palindrome is a string or sequence of characters that reads the same backward and forward. 
For example, "madam" is a palindrome.
Write a function that takes in a string and returns a Boolean -> True 
if the input string is a palindrome and False
if it is not. An empty string is considered a palindrome. 
You also need to account for the space character. For example, "race car" should return 
False as read backward it is "rac ecar".

Examples:
is_palindrome("madam") -> True

is_palindrome("aabb") -> False

is_palindrome("race car") -> False

is_palindrome("") -> True


def is_palindrome(input_string):
    return (input_string == input_string[::-1])

print(is_palindrome("race car"))
'''

'''
Write a function that takes in a string and returns the reversed version of the string.

Examples:

reverse_string("abcde") -> "edcba"

reverse_string("1") -> "1"

reverse_string("") -> ""

reverse_string("madam") -> "madam"


def reverse_string(a_string):
    return (a_string[::-1])

print (reverse_string('abcde'))

'''

'''
You are given an m x n 2D image matrix (List of Lists) 
where each integer represents a pixel. Flip it in-place along its horizontal axis.

Example:

Input image :  
              1 1
              0 0 
Modified to :   
              0 0
              1 1
              
[[1,2,3],[4,5,6],[7,8,9]]

[[7, 8, 9], [4, 5, 6], [1, 2, 3]]              


def flip_horizontal_axis(matrix):
    placeholder = matrix[0]    
    for i in range(len(matrix)):
        if i == (len(matrix)-1):
            matrix[0] = matrix[i]
            matrix[i] = placeholder
    return matrix

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print (flip_horizontal_axis(matrix))
'''


'''
Write a function to compute the binary representation of a positive decimal integer. 
The method should return a string. 

Example:
dec_to_bin(6) ==> "110"

dec_to_bin(5) ==> "101"


def dec_to_bin (number):
    if number//2 == 0:
        return 1
    else:
        return str(dec_to_bin(number//2)) + str(number%2) 
    
print (dec_to_bin(6))
'''

'''
Write a function - duplicate_items to find the redundant or repeated items in a list and return them in sorted order. 
This method should return a list of redundant integers in ascending sorted order (as illustrated below). 

Examples:
duplicate_items([1, 3, 4, 2, 1]) => [1]

duplicate_items([1, 3, 4, 2, 1, 2, 4]) => [1, 2, 4]

def duplicate_items(list_numbers):
    duplicates = []
    for i in list_numbers:
        counter = list_numbers.count(i)
        if counter>1:
            duplicates.append(i)   
    return list(set(duplicates))

print (duplicate_items([1, 3, 4, 2, 1, 2, 4]))
'''


'''

The Fibonacci Sequence is the series of numbers: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ... 
The next number is found by adding up the two numbers before it.
Write a recursive method fib(n) that returns the nth Fibonacci number. 
n is 0 indexed, which means that in the sequence 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ..., n == 0 should 
return 0 and n == 3 should return 2. 

Assume n is less than 15.
Even though this problem asks you to use recursion, 
more efficient ways to solve it include using an Array, 
or better still using 3 volatile variables to keep a track of all required values. 
Check out this blog post to examine better solutions for this problem.

Examples:
fib(0) ==> 0

fib(1) ==> 1

fib(3) ==> 2
fib(10) ==> 55
'''
def fib(n):
    if n==0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

n = 10
print (fib(n))


















