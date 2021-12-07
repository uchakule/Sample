s = input('Enter your string :')
#******************* 1st Method ***********************************#
str =''
for i in s:
    str = i+str
print(str)
#********************** 2nd Method ***********************************#
n = len(s)
i =-1
while i>=-n:
    print(s[i],end='')
    i-=1
