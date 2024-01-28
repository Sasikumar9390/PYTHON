num = int(input('Enter a number to check Perfect number or not:  '))
s = 0
d = 1

while d<num:
    if num%d == 0:
        s = s + d

    d = d + 1

if s == num:
    print(num,'is a Perfect number')
else:
    print(num,'is not a perfect number')
