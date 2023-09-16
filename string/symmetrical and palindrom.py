'''
Given a string. the task is to check if the string is symmetrical and palindrome or not. A string is said to be 
symmetrical if both the halves of the string are the same and a string is said to be a palindrome string if 
one half of the string is the reverse of the other half or if a string appears same when 
read forward or backward.

Example: 

Input: khokho
Output: 
The entered string is symmetrical
The entered string is not palindrome

Input:amaama
Output:
The entered string is symmetrical
The entered string is palindrome
'''

s = input("enter the string : ")
l = len(s)

if l%2 == 0:
    x = s[0 :int(l/2)]
    y = s[int(l/2) :l]
else:
    x = s[0 :int(l/2)]
    y = s[int(l/2)+1 :l]


def palindrom(a,b):
    if(a == b[::-1]):
        return "a palindrom"
    else:
        return "not a palindrom"
        
def symmetrical(x,y):
    if x == y:
        return "a symmetrical"
    else:
        return "not a symmmetrical"
        

print("this string is ", palindrom(x,y), " & this string is ", symmetrical(x,y))
