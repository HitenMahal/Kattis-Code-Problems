x, y = input().split()
if (int(x)*4 + int(y)*3) % 2 == 0:
    print("possible")
else:
    print("impossible")