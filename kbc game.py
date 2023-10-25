# kon banega carorpati game using python

# list of questions
list1 = ["what is your name" , "what is your surname", "when was chandrayan-3 launched",
         "who is the prime minister of the India", "Who is the defence minister of India",
         "how many cgpa was kalapi got in sem 1", "how far is Somnath from Maliya",
         "what is the age of Kalapi", "what is the name of rover used in chandrayan-3",
         "which share does kalapi hold in thier portfolio"]


# list of options
list2 = [["dev","sarthak","kalapi","narendra"], ["modi", "patel", "sing", "vadariya"], 
         ["14-july", "23-aug", "16-july", "21-july"], ["lalu", "modi", "gadkari", "yogi"], 
         ["rajnath sing", "S. jaysankar", "Nitin gadkari", "piyush goyel"], ["9.13", "8.93", "8.33", "9.03"], 
         ["35", "40", "42", "48"], ["17", "18", "20", "19"], 
         ["vikram", "pragya", "narendra modi", "aditya"], ["LIC", "nmdc steel", "mishtan food", "IRFC"]]

# list of correct ans
list3 = [4, 2, 1, 2, 1, 4, 3, 4, 2, 3]

i=1
sum = 0

print("for a ypu have to print 1, for b-2, for c - 3, for d - 4\n")

while(i<11):
    print("Question ", i)
    print(list1[i-1])
    print(list2[i-1])
    
    temp = int(input("Enter you ans : "))
    
    if(temp == list3[i-1]):
        sum = sum + 1000000*i
    else:
        break
    i = i+1
    
k = int(sum / 1000000)
        
print("The amount you win is : ", k, " million")

