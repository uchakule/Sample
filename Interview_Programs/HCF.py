#******** To Find HCF of two numbers**********

def HCF(n1,n2):
    """ Create HCF function to get HCF of 2 numbers"""
    if (n1<n2):
        min = n1
    else:
        min= n2
    """ looping all the numbers till min one"""    
    for i in range(1,min+1):      
        if ((n1 % i ==0) and (n2 % i ==0)):
            hcf = i
    return hcf
        
n1 = int(input("Enter first value: "))
n2 = int(input("Enter second value: "))

print(HCF(n1,n2))