num = int(input('Enter a number to count of digits: '))
count = 0

while num>0:
    num = num//10
    count = count + 1

print(count)