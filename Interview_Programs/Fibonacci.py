"Fibonacci Sequence Program"

nterms =int(input('How many terms required ?'))
n2 = 1
n1 = 0
count =0
if nterms<=0:
    print('Please enter postive integer')
elif nterms ==1:
    print('fibonacci sequence upto',nterms,'is',n1)
else:
    print('Fibonacci Sequence :')
    while count < nterms:
        print(n1)
        nth = n1+n2
        n1 = n2
        n2 = nth
        count+=1            