"""
Exercício 17 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaSequencial

Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e
que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
comprar apenas latas de 18 litros;
comprar apenas galões de 3,6 litros;
misturar latas e galões, de forma que o custo seja menor.
Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.

    >>> from secao_01_estrutura_sequencial import ex_17_loja_de_tintas_complexa
    >>> ex_17_loja_de_tintas_complexa.input = lambda k: '100'
    >>> ex_17_loja_de_tintas_complexa.calcular_latas_e_preco_de_tinta()
    Você deve comprar 19 litros de tinta.
    Você pode comprar 2 lata(s) de 18 litros a um custo de R$ 160. Vão sobrar 17.0 litro(s) de tinta.
    Você pode comprar 6 lata(s) de 3.6 litros a um custo de R$ 150. Vão sobrar 2.6 litro(s) de tinta.
    Para menor custo, você pode comprar 1 lata(s) de 18 litros e 1 galão(ões) de 3.6 litros a um custo de R$ 105. Vão sobrar 2.6 litro(s) de tinta.
    >>> ex_17_loja_de_tintas_complexa.input = lambda k: '200'
    >>> ex_17_loja_de_tintas_complexa.calcular_latas_e_preco_de_tinta()
    Você deve comprar 37 litros de tinta.
    Você pode comprar 3 lata(s) de 18 litros a um custo de R$ 240. Vão sobrar 17.0 litro(s) de tinta.
    Você pode comprar 11 lata(s) de 3.6 litros a um custo de R$ 275. Vão sobrar 2.6 litro(s) de tinta.
    Para menor custo, você pode comprar 2 lata(s) de 18 litros e 1 galão(ões) de 3.6 litros a um custo de R$ 185. Vão sobrar 2.6 litro(s) de tinta.

"""


def calcular_latas_e_preco_de_tinta():
    """Escreva aqui em baixo a sua solução"""
    area_pintada = float(input('Digite o tamanho da área (m²) a ser pintada: ')) * 1.1

    litros_galao = 3.6
    galao_faz = 21.6
    preco_galao = 25

    litro_faz = 6

    litros_lata = 18
    lata_faz = 108
    preco_lata = 80

    quantidade_lata = area_pintada / lata_faz
    comprar_litros = area_pintada // litro_faz
    resto_litros = area_pintada % litro_faz

    if resto_litros > 0:
        comprar_litros += 1

    if area_pintada % lata_faz > 0:
        quantidade_lata = area_pintada // lata_faz + 1

    sobrou = quantidade_lata * litros_lata - comprar_litros
    preco_total = preco_lata * quantidade_lata
    quantidade_galao = area_pintada / galao_faz

    if area_pintada % galao_faz > 0:
        quantidade_galao = area_pintada // galao_faz + 1

    sobrou1 = quantidade_galao * litros_galao - comprar_litros
    preco_total1 = preco_galao * quantidade_galao

    quantidade_lata1 = area_pintada // lata_faz
    sobra_area = area_pintada - (quantidade_lata1 * lata_faz)
    quantidade_galao1 = sobra_area / galao_faz

    if sobra_area % galao_faz > 0:
        quantidade_galao1 = sobra_area // galao_faz + 1

    if quantidade_galao1 > 3:
        preco_total_lata = preco_lata * (quantidade_lata1 + 1)
        sobrou2 = quantidade_lata1 * litros_lata - comprar_litros
        preco_total2 = preco_total_lata

    else:
        preco_total_lata = preco_lata * quantidade_lata1
        preco_total_galao = preco_galao * quantidade_galao1
        preco_total2 = preco_total_lata + preco_total_galao
        sobrou2 = (quantidade_galao1 * litros_galao) + (quantidade_lata1 * litros_lata) - comprar_litros

    print(f'Você deve comprar {comprar_litros:.0f} litros de tinta.')
    print(
        f'Você pode comprar {quantidade_lata:.0f} lata(s) de {litros_lata} litros a um custo de R$ {preco_total:.0f}.'
        f' Vão sobrar {sobrou:.1f} litro(s) de tinta.')
    print(
        f'Você pode comprar {quantidade_galao:.0f} lata(s) de {litros_galao} litros a um custo de R$ {preco_total1:.0f}'
        f'. Vão sobrar {sobrou1:.1f} litro(s) de tinta.')
    print(
        f'Para menor custo, você pode comprar {quantidade_lata1:.0f} lata(s) de {litros_lata} litros e'
        f' {quantidade_galao1:.0f} galão(ões) de {litros_galao} litros a um custo de R$ {preco_total2:.0f}.'
        f' Vão sobrar {sobrou2:.1f} litro(s) de tinta.')
