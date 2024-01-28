num = int(input('Enter a number to find Divisors: '))
d = 1

while d<=num:
    if num%d == 0:
        print(d)
    d = d + 1
    
