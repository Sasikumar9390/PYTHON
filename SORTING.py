#SORTING

x = [10,5,9,15,3,11,2]
x.sort()
print(x)

#WITHOUT SORT FUNCTION

x = [10,5,9,15,3,11,2] 
for i in range(0,len(x)):
    min_value = min(x[i:])
    idx = x.index(min_value)
    x[i],x[idx] = x[idx],x[i]
print(x)


#WITHOUT SORT FUNCTION IN DUPLICATE VALUES
x = [10,5,2,3,9,15,3,11,2]
for i in range(0,len(x)):
    min_value = min(x[i:])
    idx = x[i:].index(min_value)+i
    x[i],x[idx] = x[idx],x[i]

print(x)
