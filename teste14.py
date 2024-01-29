from collections import defaultdict
from collections import Counter

with open('small.txt','r') as arquivo:
    conteudo = arquivo.read().lower().split()

    wlist=[]
    wlist=conteudo
    wdic={}
    wdic['']=[wlist[0]]

    contador=Counter(conteudo)
    #print([tuple(contador.items())])
    d=defaultdict(list)
    c = tuple(contador.items())
    for k,v in c:
        d[k].append(v)
    print(d.items())


    #print(wdic)

    wdic[conteudo[-1]]=['']
    #print(wdic.items())

