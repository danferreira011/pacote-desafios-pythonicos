"""
06. not_bad

Dada uma string, encontre a primeira aparição das
substrings 'not' e 'bad'. Se 'bad' aparecer depois
de 'not', troque todo o trecho entre 'not' e 'bad'
por 'good' e retorne a string resultante.

Exemplo: 'The dinner is not that bad!' retorna 'The dinner is good!'
"""

import re

from jupyter_core.migrate import regex


def not_bad(s):
    #Tentativa Teste
    '''''''''
    string = 'This movie is not so bad'
    ns = re.sub(r"not.*bad","good", string)
    print(re.findall('not',ns))
    #ns = string.replace('not so bad','good')
    #print(ns)
    '''''
    # +++ SUA SOLUÇÃO +++

    #ns = re.sub(r"not.*?bad", "good", s)
    # print(re.findall(r'not.*bad',s))
    #return ns
    return re.sub('not([0-9 a-zA-Z]*)?bad', 'good', s)


# --- Daqui para baixo são apenas códigos auxiliáries de teste. ---

def test(f, in_, expected):
    """
    Executa a função f com o parâmetro in_ e compara o resultado com expected.
    :return: Exibe uma mensagem indicando se a função f está correta ou não.
    """
    out = f(in_)

    if out == expected:
        sign = '✅'
        info = ''
    else:
        sign = '❌'
        info = f'e o correto é {expected!r}'

    print(f'{sign} {f.__name__}({in_!r}) retornou {out!r} {info}')


if __name__ == '__main__':
    # Testes que verificam o resultado do seu código em alguns cenários.
    test(not_bad, 'This movie is not so bad', 'This movie is good')
    test(not_bad, 'This dinner is not that bad!', 'This dinner is good!')
    test(not_bad, 'This tea is not hot', 'This tea is not hot')
    test(not_bad, "It's bad yet not", "It's bad yet not")
    test(not_bad, 'This is not so bad and i\'m not so bad', 'This is good and i\'m good')
    test(not_bad, 'I\'m not so good, but this food is not so bad', 'I\'m not so good, but this food is good')
