import random

def random_id(len):
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    id = ''
    for i in range(len):
        id += random.choice(alpha)
    return id

def to_string(s):
    str1 = ''
    for i in s:
        str1 += i + ' '
        
    return str1

def encode(txt):
    x = txt.split()

    for i, ch in enumerate(x):
        k = random_id(3)
        l = random_id(3)
            
        if(len(ch) >= 3):
            x[i] = x[i] + ch[0]
            x[i] = x[i][1:]
            x[i] = k + x[i] + l
        else:
            x[i] = x[i] + ch[0]
            x[i] = x[i][1:]
            
    new = to_string(x)
    return new

def decode(s):
    a = s.split()
    for i, ch in enumerate(a):
        if len(ch) > 3 :
            z = a[i][-4]
            a[i] = a[i][3:-4]
            a[i] = z + a[i]
        elif(len(ch) < 3):
            a[i] = a[i] + ch[0]
            a[i] = a[i][1:]
            
    v = to_string(a)
    return v
    
key = 12345
# txt = "welcome to the jungle of the gir"
txt = input("enter your string you want : ")
news = encode(txt)
print("encoded string is : ", news)

k = int(input("enter you key to decode the massage : "))

if k ==  key:
    print( decode(news))
else:
    print("your key is not valid!!")
