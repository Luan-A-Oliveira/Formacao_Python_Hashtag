# -*- coding: utf-8 -*-
"""Listas 03.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1nA-3HEQmcREx3emp2nyBORKcwFrMyx9F

# Como descobrir o índice de um item de uma lista?

i = lista.index('item')

Exemplo:

Digamos que você puxou do Banco de Dados da sua empresa uma lista com todos os produtos que a empresa vende e a quantidade em estoque de todos eles.
"""

produtos = ['tv', 'celular', 'tablet',
            'mouse', 'teclado', 'geladeira', 'forno']
estoque = [100, 150, 100, 120, 70, 180, 80]

"""Nesse caso a lista é "pequena" para fins didáticos, mas essa lista poderia ter dezenas de milhares de produtos diferentes.

E agora, como eu faço para descobrir a quantidade em estoque do produto geladeira?
"""
i = produtos.index('geladeira')
print(i)

print(produtos[i])

qnt_estoque = estoque[i]
print(qnt_estoque)


"""Crie um programa para fazer uma consulta de estoque. O usuário do programa deve inserir o nome do produto e, caso ele não exista na lista, ele deve ser avisado. Caso exista, o programa deve dizer a quantidade de unidades em estoque do produto"""

produto = input('insira um produto: ')
if produto in produtos:
    i = produtos.index(produto)
    qnt_estoque = estoque[i]
    print('Temos {} unidades de {} no estoquer'.format(qnt_estoque, produto))
else:
    print('produto invalido')
