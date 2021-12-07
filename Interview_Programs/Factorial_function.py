#1. Factorial using recursion logic
# def factorial(n):
#     if n==0:
#         result =1
#     else:
#         result = n*factorial(n-1)
#     return result
# print('Factorial of 4 is',factorial(4))

#2. Factorial using if....elif....else without functions
num = int(input('Enter number:'))
def factorial(num):
    factorial = 1
    if num<0 :
        print("factorial does not exist for -ve numbers")
    elif num ==0:
        return factorial
    else:
        for i in range(1,num+1):
            factorial=factorial*i
        return factorial
print(factorial(num))        
    
#3. Factorial of numbers from 1 to 8
# def fact(num):
#     factorial = 1
#     while num>=1:
#         factorial = factorial*num
#         num = num-1
#     return factorial
# for i in range(9):
#     print('Factorial of {} is {}'.format(i,fact(i)))