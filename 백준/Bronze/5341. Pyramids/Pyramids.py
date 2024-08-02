while True:

    a = 0

    b = int(input())

    if not b:
        break

    for i in range(1, b+1):
        a += i
        
    print(a)