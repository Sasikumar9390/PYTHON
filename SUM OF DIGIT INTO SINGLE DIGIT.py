num = int(input('Enter a number: '))
while True:
    s = 0
    while num>0:
        t = num%10
        s = s + t
        num = num//10

    if s>9:
        num = s
    else:
        print(s)
        break

