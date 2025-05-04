import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

# Criar dados de clientes
clientes = pd.DataFrame({
    'id_cliente': range(1, 11),
    'nome': [f'Cliente {i}' for i in range(1, 11)],
    'email': [f'cliente{i}@email.com' for i in range(1, 11)],
    'cidade': random.choices(['São Paulo', 'Rio de Janeiro', 'Belo Horizonte', 'Curitiba', 'Recife'], k=10)
})

# Criar dados de produtos
produtos = pd.DataFrame({
    'id_produto': range(1, 6),
    'nome': ['Camiseta', 'Calça', 'Tênis', 'Boné', 'Jaqueta'],
    'preco': [49.90, 99.90, 199.90, 29.90, 149.90]
})

# Criar dados de pedidos
pedidos = []
for i in range(1, 21):
    pedidos.append({
        'id_pedido': i,
        'id_cliente': random.randint(1, 10),
        'data': (datetime.now() - timedelta(days=random.randint(1, 365))).strftime('%Y-%m-%d')
    })
pedidos = pd.DataFrame(pedidos)

# Criar dados de itens do pedido
itens = []
for pedido_id in pedidos['id_pedido']:
    for _ in range(random.randint(1, 4)):  # de 1 a 4 produtos por pedido
        produto_id = random.randint(1, 5)
        quantidade = random.randint(1, 3)
        itens.append({
            'id_pedido': pedido_id,
            'id_produto': produto_id,
            'quantidade': quantidade
        })
itens_pedido = pd.DataFrame(itens)

# Salvar os arquivos .csv
clientes.to_csv('clientes.csv', index=False)
produtos.to_csv('produtos.csv', index=False)
pedidos.to_csv('pedidos.csv', index=False)
itens_pedido.to_csv('itens_pedido.csv', index=False)

print("Arquivos .csv gerados com sucesso!")
