#RIGHT ROTATAION

x = [10,20,30,40,50,60,70,80,90,100]
element = int(input('Enter a element to start rotation: '))
if element in x:
    output = []
    idx = x.index(element)
    output.extend(x[idx+1:])
    output.extend(x[:idx+1])
    print('Right rotation =',output)
else:
    print('Right rotation is not possible because element is not found')

#LEFT ROATAION

x = [10,20,30,40,50,60,70,80]
element = int(input('Enter a element to start: '))
if element in x:
    output = []
    idx = x.index(element)
    output.extend(x[idx-1::-1])
    output.extend(x[:idx-1:-1])
    print('Left rotation =',output)
else:
    print('Left rotation is not possible because element is not found')
