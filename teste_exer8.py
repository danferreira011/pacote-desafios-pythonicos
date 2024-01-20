a = ['aaa', 'be', 'abc', 'hello']
i = 0
j = 0
for n in a:
    if len(n) >= 2 and n.startswith(n[i]) and n.endswith(n[i]):
        print(n)
        j += 1
i += 1
print(j)
