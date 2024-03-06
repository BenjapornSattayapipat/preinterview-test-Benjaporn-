
def check_number(n):
    for num in range(1, n + 1):
        if num % 3 == 0 and num % 5 == 0:
            print(num ,"Ping Pong")
        elif num % 3 == 0:
            print(num ,"Ping")
        elif num % 5 == 0:
            print(num ,"Pong")

n = int(input("ป้อนตัวเลข n: "))
check_number(n)
