'''
Input : str =" geeks quiz practice code"
Output : str = code practice quiz geeks  
Input : str = "my name is laxmi"
output : str= laxmi is name my 
'''


def to_string(list):
    id = ''
    for i in list:
        id += i + " "
    
    return id

s = input("enter your string you want to enter : ")

l = s.split()

print(to_string(l[::-1]))
