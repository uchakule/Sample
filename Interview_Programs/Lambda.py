#--------------Lambda---------------------
#lamba is also called as anonymous function or function without name (nameless function)
#it's use for temporay used
#rather than def keyword we used lampda
# using reference variable it will call the lambda function

s = lambda x,y:x+y
print(s(5,6))


#---------------Map------------------------
#process each and every elements collect inside output
#input = output
#list(map(function,iterable))

num = [2,3,4,5,6,7,8,9]
s = list((map(lambda x:x*x,num)))
print(s)

#-------------Filter------------------------
#whichever elements satisfies our condition only collect them inside output
#list(filter(function,iterable))

num = [2,3,4,5,6,7,8,9]
s = list((filter(lambda x:x>=5,num)))
print(s)

#-------------Reduce------------------------

from functools import reduce
num = [2,3,4,5,6,7,8,9]
add = reduce(lambda x,y:x+y,num)
print(add)