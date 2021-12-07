
class Project:
    def bubble_sort(arr):
        n = len(arr)
        for i in range(n):
            for j in range(n-i-1):
                if arr[j]>arr[j+1]:
                    arr[j],arr[j+1]=arr[j+1],arr[j]

arr = eval(input('Enter your list:'))
print(type(arr))

Project.bubble_sort(arr)
for i in range(len(arr)):
    print(arr[i])