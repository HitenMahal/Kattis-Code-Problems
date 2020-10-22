#https://open.kattis.com/contests/ontdsq/problems/apaxianparent

first, last = input().split()
checker = first[-1]
vowels = ["a","i","o","u"]

if checker == 'e':
    print(first + "x" + last)
elif checker in vowels:
        print(first[:-1] + "ex" + last)
elif first[-2:] == "ex":
    print(first + last)
else:
    print(first + "ex" + last)