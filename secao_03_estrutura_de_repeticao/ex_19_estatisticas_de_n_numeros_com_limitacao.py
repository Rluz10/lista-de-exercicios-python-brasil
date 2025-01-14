"""
Exercício 19 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaDeRepeticao

Altere o programa anterior para que ele aceite apenas números entre 0 e 1000.

    >>> calcular_estatisticas()
    'Maior valor: não existe. Menor valor: não existe. Soma: 0'
    >>> calcular_estatisticas(1)
    'Maior valor: 1. Menor valor: 1. Soma: 1'
    >>> calcular_estatisticas(1, 2)
    'Maior valor: 2. Menor valor: 1. Soma: 3'
    >>> calcular_estatisticas(1, 2, -1)
    'Somente números de 0 a 1000 são permitidos'
    >>> calcular_estatisticas(1, 2, -10)
    'Somente números de 0 a 1000 são permitidos'
    >>> calcular_estatisticas(1, 2, 1001)
    'Somente números de 0 a 1000 são permitidos'
    >>> calcular_estatisticas(1, 2, 1198)
    'Somente números de 0 a 1000 são permitidos'

"""


def calcular_estatisticas(*numeros) -> str:
    """Escreva aqui em baixo a sua solução"""
    if len(numeros) == 0:
        return f'Maior valor: não existe. Menor valor: não existe. Soma: 0'
    else:
        menor_valor = numeros[0]
        maior_valor = numeros[0]
        soma = 0
        for n in numeros:
            if n < 0 or n > 1000:
                return 'Somente números de 0 a 1000 são permitidos'
            if maior_valor < n:
                maior_valor = n
            if menor_valor > n:
                menor_valor = n
            soma += n
        return f'Maior valor: {maior_valor}. Menor valor: {menor_valor}. Soma: {soma}'