'''
1.It is the another way to creating iterators in a simple way where it uses the keyword "yield" instead of returning it in a defined function.
2.Generators are implemented using functions just as a iterators, generators also follow lazy evaluation.
3.The yield function returns the data without affecting or existing the function.
4.It will return a sequence of data in an iterable format where we need to iterate over the sequence to use the data as they won't store the 
  entire sequence in the memory.
 
'''
def sq_numbers():
    n=1
    while n <=10:
        yield n*n
        n +=1
a =sq_numbers()
for i in a:
    print(i)