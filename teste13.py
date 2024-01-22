arquivo = open('letras.txt', 'r')

conteudo = arquivo.read()
#print(conteudo)
nl=conteudo[:].lower().split()
print(nl)

for w in nl:
   if w in nl:
       print 
       print (nl.count(w))
