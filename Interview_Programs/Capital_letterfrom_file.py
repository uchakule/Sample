with open('D:\\MySmallPrograms\\UC.txt') as file:
    count = 0
    text =file.read()
    for ch in text:
        if ch.isupper():
            count+=1
print(count)