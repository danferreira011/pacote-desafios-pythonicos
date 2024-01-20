
a = 'abcd'
b = 'xyz'

print(len(a))
print(len(a ) /2)


print(len(a ) %2)

if len(a) % 2 == 0:
    f = len(a ) /2
    e = a[slice(0 ,int(f))]
    i = a[slice(int(f), len(a))]
    print(e,i)
else:
    f = (len(a ) /2 ) +1
    e = a[slice(0, int(f))]
    i = a[slice(int(f), len(a))]
    print (e,i)

if len(b) % 2 == 0:
    g = len(b ) /2
    h = b[slice(0 ,int(g))]
    j = b[slice(int(g), len(b))]
    print(h,j)
else:
    g = (len(b) / 2) +1
    h = b[slice(0, int(g))]
    j = b[slice(int(g), len(b))]
    print(h, j)


print(e[slice(0,int(f))]+h+i[slice(0,int(g))]+j )
