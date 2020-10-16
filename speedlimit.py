#https://open.kattis.com/problems/speedlimit


while True:
    travelled = 0   #Calculate new output
    x = int(input())
    if x < 0: #Exit condition
        break

    for i in range(x):
        speed,time = (int(x) for x in input().split())
        
        if i == 0:
            travelled += speed * time
            timeElapsed = time
        else:
            travelled += speed * (time - timeElapsed)
            timeElapsed = time
    print(travelled,"miles")