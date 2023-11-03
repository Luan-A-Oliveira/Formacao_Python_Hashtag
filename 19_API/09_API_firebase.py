# Criar o projeto no Firebase

# Link documento REST API Firebase
# https://firebase.google.com/docs/reference/rest/database

# Criar o Database (atenção às regras de segurança)
# Estrutura de árvore

# Interação com o Database (REST API)
import requests
import json

link = "link do BD firebase"

# Criar uma venda (POST)
dados = {'cliente': 'alon', 'preco': 150, 'produto': 'teclado'}
requisicao = requests.post(f'{link}/vendas/.json', data=json.dumps(dados))
print(requisicao)
print(requisicao.text)

# Criar um novo produto (POST)
dados = {'nome': 'teclado', 'preco': 150, 'quantidade': 80}
requisicao = requests.post(f'{link}/Produtos/.json', data=json.dumps(dados))
print(requisicao)
print(requisicao.text)

# Editar a venda (PATCH)
dados = {'cliente': 'regina'}
requisicao = requests.patch(
    f'{link}/vendas/-NiKP4da4SiWiV2j--s9/.json', data=json.dumps(dados))
print(requisicao)
print(requisicao.text)

# Pegar uma venda específico ou todas as vendas (GET)
requisicao = requests.get(f'{link}/vendas/.json')
print(requisicao)
dic_requisicao = requisicao.json()
id_regina = None
for id_venda in dic_requisicao:
    cliente = dic_requisicao[id_venda]['cliente']
    if cliente == "regina":
        print(id_venda)
        id_regina = id_venda

# Deletar uma venda (DELETE)
requisicao = requests.delete(f'{link}/vendas/{id_regina}/.json')
print(requisicao)
print(requisicao.text)
