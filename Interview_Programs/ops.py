def prime(num):
    if num >1:
        for i in range(2,num):
            if (num % i) ==0:
                print('is not prime number')
                break
            else:
                print('is prime number')
    else:
        print('is not prime number')

print(prime(4))                
















