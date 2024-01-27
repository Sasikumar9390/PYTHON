num = int(input('Enter a number: '))

x = 0

y = 1

cnt = 0

while True:

    z = x + y

    if z%2 == 0:

        cnt = cnt + 1


    if cnt == num:
        print(z)

        break

    x = y

    y = z
