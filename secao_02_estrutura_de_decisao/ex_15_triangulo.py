"""
Exercício 15 da seção de estrutura de decisão da Python Brasil:
https://wiki.python.org.br/EstruturaDeDecisao

Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo. Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
Dicas:
Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
Triângulo Equilátero: três lados iguais;
Triângulo Isósceles: quaisquer dois lados iguais;
Triângulo Escaleno: três lados diferentes;

    >>> classificar_triangulo(2, 3, 4)
    'Triângulo Escaleno'
    >>> classificar_triangulo(2, 2, 3)
    'Triângulo Isósceles'
    >>> classificar_triangulo(2, 2, 2)
    'Triângulo Equilátero'
    >>> classificar_triangulo(2, 2, 5)
    'Não é um triângulo'
    >>> classificar_triangulo(5, 2, 2)
    'Não é um triângulo'
    >>> classificar_triangulo(2, 5, 2)
    'Não é um triângulo'

"""


def classificar_triangulo(lado_a: float, lado_b: float, lado_c: float):
    """Escreva aqui em baixo a sua solução"""
    soma_1 = lado_a + lado_b
    soma_2 = lado_a + lado_c
    soma_3 = lado_b + lado_c

    lista = [lado_a, lado_b, lado_c]

    if soma_1 > lado_c and soma_2 > lado_b and soma_3 > lado_a:
        if (lado_a + lado_b + lado_c) / 3 == lado_a:
            return 'Triângulo Equilátero'
        elif lado_a == lado_b or lado_a == lado_c or lado_b == lado_c:
            return 'Triângulo Isósceles'
        else:
            return 'Triângulo Escaleno'
    else:
        return 'Não é um triângulo'