"""
i/p: String
o/p: True/False 
to check given string is palindrome or not
"""

s1= input ('Enter the string: ')

# [start: end: steps

s2= s1[::-1]
if s1==s2:
    print("True")
else:
    print("False")