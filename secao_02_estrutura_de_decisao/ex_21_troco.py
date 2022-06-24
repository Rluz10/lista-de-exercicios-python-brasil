"""
Exercício 21 da seção de estrutura de decisão da Python Brasil:
https://wiki.python.org.br/EstruturaDeDecisao

Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário a valor do saque e depois informar
quantas notas de cada valor serão fornecidas. As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. O valor mínimo
é de 1 real e o máximo de 600 reais. O programa não deve se preocupar com a quantidade de notas existentes na máquina.
Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50, uma nota de 5 e uma
nota de 1;
Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma nota de 50, quatro notas de 10,
uma nota de 5 e quatro notas de 1.

    >>> calcular_troco(256)
    '2 notas de R$ 100, 1 nota de R$ 50, 1 nota de R$ 5 e 1 nota de R$ 1'
    >>> calcular_troco(1)
    '1 nota de R$ 1'
    >>> calcular_troco(5)
    '1 nota de R$ 5'
    >>> calcular_troco(10)
    '1 nota de R$ 10'
    >>> calcular_troco(11)
    '1 nota de R$ 10 e 1 nota de R$ 1'
    >>> calcular_troco(399)
    '3 notas de R$ 100, 1 nota de R$ 50, 4 notas de R$ 10, 1 nota de R$ 5 e 4 notas de R$ 1'
"""


def calcular_troco(valor: int) -> str:
    """Escreva aqui em baixo a sua solução"""
    if valor < 1 or valor > 600:
        return 'O valor mínimo precisa ser de 1 real e o máximo de 600 reais'
    else:
        cem = valor // 100
        resto = valor % 100
        if cem > 0:
            if cem == 1:
                a = f'{cem} nota de R$ 100'
            else:
                a = f'{cem} notas de R$ 100'
        else:
            a = 0

        cinquenta = resto // 50
        resto1 = resto % 50
        if cinquenta > 0:
            if cinquenta == 1:
                b = f'{cinquenta} nota de R$ 50'
            else:
                b = f'{cinquenta} notas de R$ 50'
        else:
            b = 0

        dez = resto1 // 10
        resto2 = resto1 % 10
        if dez > 0:
            if dez == 1:
                c = f'{dez} nota de R$ 10'
            else:
                c = f'{dez} notas de R$ 10'
        else:
            c = 0

        cinco = resto2 // 5
        resto3 = resto2 % 5
        if cinco > 0:
            if cinco == 1:
                d = f'{cinco} nota de R$ 5'
            else:
                d = f'{cinco} notas de R$ 5'
        else:
            d = 0

        um = resto3 // 1
        resto4 = resto3 % 1
        if um > 0:
            if um == 1:
                e = f'{um} nota de R$ 1'
            else:
                e = f'{um} notas de R$ 1'
        else:
            e = 0

        lista = [a, b, c, d, e]
        lista_temp = []
        for i in lista:
            if i != 0:
                lista_temp.append(i)
        contador = len(lista_temp)
        if contador == 5:
            return f'{lista_temp[0]}, {lista_temp[1]}, {lista_temp[2]}, {lista_temp[3]} e {lista_temp[4]}'
        elif contador == 4:
            return f'{lista_temp[0]}, {lista_temp[1]}, {lista_temp[2]} e {lista_temp[3]}'
        elif contador == 3:
            return f'{lista_temp[0]}, {lista_temp[1]} e {lista_temp[2]}'
        elif contador == 2:
            return f'{lista_temp[0]} e {lista_temp[1]}'
        elif contador == 1:
            return f'{lista_temp[0]}'