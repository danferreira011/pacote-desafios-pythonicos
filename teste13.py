#arquivo = open('letras.txt', 'r')
#conteudo = arquivo.read()
#with open('letras.txt', 'r') as arquivo:
#    conteudo = arquivo.read()
#l=conteudo[:].lower().split()
##print(l)
#leters=[]
#nums=[]
#for w in l:
#   if w in l:
#      leters.append(w)
#      nums.append(l.count(w))
#      l1= (sorted(set(leters)))
#      l2 = (sorted(set(nums)))
#      #print(l1)
#      #print(l2)
#      l3=list(zip(l1, l2))
#print (l3)
def print_words(filename):
    with open(filename, 'r') as arquivo:
        conteudo = arquivo.read()
    l = conteudo[:].lower().split()
    # print(l)
    leters = []
    nums = []
    for w in l:
        if w in l:
            leters.append(w)
            nums.append(l.count(w))
            l1 = (sorted(set(leters)))
            l2 = (sorted(set(nums)))
            # print(l1)
            # print(l2)
            l3 = list(zip(l1, l2))
    return(l3)

print(print_words('letras.txt') )