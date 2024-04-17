list = ['bbb', 'ccc', 'axx', 'xzz', 'xaa']
list1 = []
listx = []

for x in list:
    if x.startswith('x'):
        listx.append(x)
    else:
        list1.append(x)
        #list.remove(x)
        #print([listx])
listx.sort()
#print(listx)
list1.sort()
#print(list1)
print(listx+list1)

