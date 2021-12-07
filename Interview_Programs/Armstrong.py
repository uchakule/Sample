"**..Armstrong Number....**"
class Armstrong:   
    def core(num):
        sum = 0
        temp = num
        while temp > 0:
            digit = temp % 10
            sum = sum + (digit **3)
            temp = temp//10
        return sum    

    def check_number(num):
        if Armstrong.core(num) == num:
            print('Entered number is armstrong number')
        else:
            print('Entered number is not armstrong number')

num = int(input('Enter number here :'))
Armstrong.check_number(num)
