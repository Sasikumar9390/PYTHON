a = 0
b = 1

num = int(input('Enter how many series you want: '))

i = 1

while i<=num:

    c = a + b

    print(c)

    a = b

    b = c

    i = i + 1
    
