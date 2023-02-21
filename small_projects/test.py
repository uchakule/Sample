num_list = []

# below function to get numbers which is divisible by 7 and not multiple of 5


def divisible_by_seven():
    try:
        for num in range(2000, 3201):
            # Condition to divisible by 7 and not multiple of 5
            if (num % 7 == 0) and (num % 5 != 0):   
                # adding numbers which satisfy condition in numlist
                num_list.append(num)
        return num_list
    except:
        print("Something went wrong")


s = divisible_by_seven()
print(*s, sep=",")
