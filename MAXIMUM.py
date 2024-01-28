x = [10,40,20,40,50,100,130,60,70,30]
max_val = max(x)
print('Maximum value is',max_val)

#With_out using max function
x = [10,40,20,40,50,100,130,60,70,30]

first = x[0]
second = x[1]

for i in x:
    if i>first:
        first = i

    if i>second and i<first:
        second = i

print('First:-',first,'Second:-',second)
