decimal = [100,90,50,40,10,9,5,4,1]
roman = ['C','XC','L','XL','X','IX','V','IV','I']
num = int(input('Enter a number: '))

for d in decimal:
    q = num//d
    idx = decimal.index(d)
    print(roman[idx]*q,end='')
    num = num%d














