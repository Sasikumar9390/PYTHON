num = int(input('Enter a number is Strong Number or not: '))
bkp = num
s = 0

while num>0:
    t = num % 10
    f = 1

    while t>=1:
        f = f * t
        t = t -1
    s = s + f
    num = num //10

if s == bkp:
    print(bkp,'is a strong number')
else:
    print(bkp,'is not a strong number')
    
