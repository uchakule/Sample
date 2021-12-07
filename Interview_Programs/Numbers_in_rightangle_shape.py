n = int(input("Enter a no. of rows:"))
k = 1
for i in range(1,1+n):          #i - to display the rows (here range(1,6) that means it will show 5 rows
    for j in range(1,i+1):      #j - to repeat 1 to i times here range(1,2) that means repaet star for one time in that row
        print(k,end=' ')
        k += 1
    print()