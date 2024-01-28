num = int(input('Enter a number to check Palindron or not: '))
bkp = num
rev = 0

while num>0:
    t = num%10
    rev = rev*10 + t
    num = num//10
if rev == bkp:
    print(bkp,'is a palindrom')
else:
    print(bkp,'is not  a palindrom')
