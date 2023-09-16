'''
Input : str =" geeks quiz practice code"
Output : str = skeeg ziuq ecitcarp edoc  
Input : str = "my name is laxmi"
output : str= ym eman si imxal 
'''


def to_string(list):
    id = ''
    for i in list:
        id += i + " "
    
    return id

s = input("enter your string you want to enter : ")

l = s.split()

for i,ch in enumerate(l):
    l[i] = l[i][::-1]

print(to_string(l))
