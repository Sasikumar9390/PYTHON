num = int(input('Enter a number to check Amstrong or not: '))
bkp = num
count = 0

while num>0:
    num = num//10
    count = count + 1

num = bkp
s = 0

while num>0:
    t = num%10
    s = s + t**count
    num = num //10

if s == bkp:
    print(bkp,'is a Amstrong Number')
else:
    print(bkp,'is not a Amstrong number')
