
import random
import math
"""
while True:
    print("1.Roll The Dice     2.Exit ")
    user = int(input("what you want to do\n"))
    if user ==1:
        number = random.randint(1,6)
        print(number)
    else:
        break    
"""    

# def even_or_odd():
#     x = int(input("enter number: "))
#     if (x % 2) == 0:
#         print(x,"is even number")
#     else:
#         print(x,"is odd number") 

# even_or_odd()    


s = 'aabbbccccddddd'
st = ''
k = 1
for i in s:
    if i not in st:
        st = st + i
        k = 1
    else:
        st = st + str(k)
        k += 1
print(st)