"""
Create a list with random numbers.
random_list = [5,1,3,2,4,5,6,7]
return list of tuples.
if n=5,
[(4,1),(3,2)]
"""

arr = [1,2,3,4,5,6,7,8]
result =[]
p = 5
s=()
n = len(arr)
for i in range(n):
    for j in range(n-i-1):
        if arr[i]+arr[j]==p:
            s=(arr[i],arr[j])
            result.append(s)
print(result)