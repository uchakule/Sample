x = int(input('Enter your first number:'))
y = int(input('Enter your second number:'))
print('Numbers befor swapping')
print('first number - {} and second number - {}'.format(x,y))
temp = x
x = y
y = temp
print('Numbers after swappings')
print('first number - {} and second number - {}'.format(x,y))