#******** To Find HCF of two numbers**********

def LCM(n1,n2):
    if (n1>n2):
        max = n1
    else:
        max = n2
    """ check each and every element whose satisfies the both condition below"""    
    while True:
        if (max % n1 ==0 and max % n2 ==0):  
            break
        max = max+1 
    return max            

n1 = int(input("Enter first value: "))
n2 = int(input("Enter second value: "))

print(LCM(n1,n2))