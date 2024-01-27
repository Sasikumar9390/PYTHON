num = int(input('Enter how many people: '))
n_sec = int(input('Enter how many section you want: '))

i = 0

sec = num//n_sec
extra = num%n_sec

while i<=n_sec:
    if i == n_sec:
        print('Section',i,sec+extra)

    else:
        print('Section',i,sec)

    i = i + 1
