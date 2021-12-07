n1 = input('Enter First String:')
n2 = input('Enter Second String:')
n1 = n1.lower()
n2 = n2.lower()
if len(n1) == len(n2):
    n1_sorted = sorted(n1)
    n2_sorted = sorted(n2)
    if n1_sorted == n2_sorted:
        print(n1, "and", n2, "are Anagram")
    else:
        print(n1, "and", n2, "are not Anagram")
else:
    print(n1, "and", n2, "are not Anagram")