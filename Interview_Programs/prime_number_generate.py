def prime(n):
    x =1
    for i in range(2,n):
        if (n%i==0):
            x=0
            break
        else:
            x=1
    return x

num = int(input("how much prime numbers you want?"))    
i =2
c =1
prime_numbers =[]
while True:
    if prime(i):
        prime_numbers.append(i)
        c =c+1
    i+=1
    if c>num:
        break
print(prime_numbers)    
