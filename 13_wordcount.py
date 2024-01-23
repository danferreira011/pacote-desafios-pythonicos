"""
13. wordcount

Este desafio é um programa que conta palavras de um arquivo qualquer de duas
formas diferentes.

A. Lista todas as palavras por ordem alfabética indicando suas ocorrências.

Ou seja...

Dado um arquivo letras.txt contendo as palavras: A a C c c B b b B
Quando você executa o programa: python wordcount.py --count letras.txt
Ele deve imprimir todas as palavras em ordem alfabética seguidas
do número de ocorrências.

Por exemplo:

$ python wordcount.py --count letras.txt
a 2
b 4
c 3

B. Lista as 20 palavras mais frequêntes indicando suas ocorrências.

Ou seja...

Dado um ar
quivo letras.txt contendo as palavras: A a C c c B b b B
Quando você executa o programa: python wordcount.py --topcount letras.txt
Ele deve imprimir as 20 palavras mais frequêntes seguidas
do número de ocorrências, em ordem crescente de ocorrências.

Por exemplo:

$ python wordcount.py --topcount letras.txt
b 4
c 3
a 2

Abaixo já existe um esqueleto do programa para você preencher.

Você encontrará a função main() chama as funções print_words() e
print_top() de acordo com o parâmetro --count ou --topcount.

Seu trabalho é implementar as funções print_words() e depois print_top().

Dicas:
* Armazene todas as palavras em caixa baixa, assim, as palavras 'A' e 'a'
  contam como a mesma palavra.
* Use str.split() (sem parêmatros) para fazer separar as palavras.
* Não construa todo o programade uma vez. Faça por partes executando
e conferindo cada etapa do seu progresso.
"""

import sys


# +++ SUA SOLUÇÃO +++
# Defina as funções print_words(filename) e print_top(filename).
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
    print(l3)

    def print_top()(filename):
        with open(filename, 'r') as arquivo:
            conteudo = arquivo.read()
        l = conteudo[:].lower().split()
        # print(l)
        leters = []
        nums = []
        for w in l:
            if w in l and w:
                leters.append(w)
                nums.append(l.count(w))
                l1 = (sorted(set(leters)))
                l2 = (sorted(set(nums)))
                # print(l1)
                # print(l2)
                l3 = list(zip(l1, l2))
        print(l3)


# A função abaixo chama print_words() ou print_top() de acordo com os
# parêtros do programa.
def main():
    if len(sys.argv) != 3:
        print('Utilização: ./13_wordcount.py {--count | --topcount} file')
        sys.exit(1)

    option = sys.argv[1]
    filename = sys.argv[2]
    if option == '--count':
        print_words(filename)
    elif option == '--topcount':
        print_top(filename)
    else:
        print('unknown option: ' + option)
        sys.exit(1)


if __name__ == '__main__':
    main()
