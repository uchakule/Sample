'''
1. An iterator is an object which contains a countable number of values and it is used to iterate over iterable objects like list, tuples, sets,etc.
2. Iterators are implemented using a class and a local variable for iterating is not required here, It follows lazy evaluation where the evaluation 
   of the expression will be on hold and stored in the memory until the item is called specifically which helps us to avoid repeated evaluation.
3. As lazy evaluation is implemented, it requires only 1 memory location to process the value and when we are using a large dataset then, 
   wastage of RAM space will be reduced the need to load the entire dataset at the same time will not be there.
4. iter() keyword is used to create an iterator containing an iterable object.
   next() keyword is used to call the next element in the iterable object.    
'''

it = iter((4,5,6,78,8,9))

print(next(it))
print(next(it))
print(next(it))

a = {3,4,5,3}
print((a))