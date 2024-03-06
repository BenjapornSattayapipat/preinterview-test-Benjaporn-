def check_number(n, i, j):
    for num in range(1, n + 1):
        if num % i == 0 and num % j == 0:
            print(num ,"Ping Pong")
        elif num % i == 0:
            print(num ,"Ping")
        elif num % j == 0:
            print(num ,"Pong")
        

n = int(input("ป้อนตัวเลข n: "))
i = int(input("ป้อนตัวเลข i: "))
j = int(input("ป้อนตัวเลข j: "))
check_number(n, i, j)
