"""
Exercício 18 da seção de estrutura de decisão da Python Brasil:
https://wiki.python.org.br/EstruturaDeDecisao

Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.

    >>> validar_data('')
    'Data inválida'
    >>> validar_data('1')
    'Data inválida'
    >>> validar_data('1/2/2004')
    'Data válida'
    >>> validar_data('1/02/2004')
    'Data válida'
    >>> validar_data('01/02/2004')
    'Data válida'
    >>> validar_data('30/02/2004')
    'Data inválida'
    >>> validar_data('01/13/2004')
    'Data inválida'

"""


def validar_data(data: str):
    """Escreva aqui em baixo a sua solução"""
    try:
        lista = []
        for i, x in enumerate(data):
            if x == '/':
                lista.append(i)
        dia = data[:lista[0]]
        mes = data[lista[0] + 1:lista[1]]
        ano = data[lista[1] + 1:]
        dia = int(dia)
        mes = int(mes)
        ano = int(ano)
        lista_mes = [2, 4, 6, 9, 11]
        if mes > 0 and mes < 13:
            if (mes == 2 and dia > 29) or (mes in lista_mes and dia > 30):
                return 'Data inválida'
            if dia > 0 and dia < 32:
                if len(str(ano)) == 4:
                    return 'Data válida'
                else:
                    return 'Data inválida'
            else:
                return 'Data inválida'
        else:
            return 'Data inválida'
    except (ValueError, IndexError):
        return 'Data inválida'