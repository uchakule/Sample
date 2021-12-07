s = 'aabbbcccc'
k = 1
st = ''
for i in s:
    if i not in st:
        st = st + i
        k =1
    else:
        st = st + str(k)
        k += 1
print(st)

