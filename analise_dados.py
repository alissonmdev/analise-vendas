import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Carregar os arquivos .csv
clientes = pd.read_csv('clientes.csv')
produtos = pd.read_csv('produtos.csv')
pedidos = pd.read_csv('pedidos.csv')
itens = pd.read_csv('itens_pedido.csv')

# Juntar os dados
df = itens.merge(pedidos, on='id_pedido') \
          .merge(produtos, on='id_produto') \
          .merge(clientes, on='id_cliente')

# Renomear colunas para evitar ambiguidade
df = df.rename(columns={
    'nome_x': 'produto',
    'nome_y': 'cliente'
})

# Calcular faturamento
df['faturamento'] = df['quantidade'] * df['preco']

# Converter coluna de data
df['data'] = pd.to_datetime(df['data'])

# Criar coluna de mês
df['mes'] = df['data'].dt.to_period('M')

# ------------------ Análises ------------------

# 1. Faturamento total por cliente
faturamento_cliente = df.groupby('cliente')['faturamento'].sum().sort_values(ascending=False)

# 2. Faturamento por produto
faturamento_produto = df.groupby('produto')['faturamento'].sum().sort_values(ascending=False)

# 3. Pedidos por mês
pedidos_por_mes = df.groupby('mes')['id_pedido'].nunique()

# 4. Ticket médio por pedido
ticket_medio = df.groupby('id_pedido')['faturamento'].sum().mean()

# 5. Top 5 clientes
top5 = faturamento_cliente.head(5)

# ------------------ Visualizações ------------------

sns.set(style='whitegrid')

# Top 5 clientes
plt.figure(figsize=(8,5))
sns.barplot(x=top5.values, y=top5.index, palette='viridis')
plt.title('Top 5 Clientes por Faturamento')
plt.xlabel('Faturamento (R$)')
plt.tight_layout()
plt.savefig('top5_clientes.png')
plt.show()

# Faturamento por produto
plt.figure(figsize=(8,5))
sns.barplot(x=faturamento_produto.values, y=faturamento_produto.index, palette='magma')
plt.title('Faturamento por Produto')
plt.xlabel('Faturamento (R$)')
plt.tight_layout()
plt.savefig('faturamento_produto.png')
plt.show()

# Pedidos por mês
plt.figure(figsize=(10,5))
pedidos_por_mes.plot(marker='o')
plt.title('Número de Pedidos por Mês')
plt.xlabel('Mês')
plt.ylabel('Quantidade de Pedidos')
plt.tight_layout()
plt.savefig('pedidos_por_mes.png')
plt.show()

# Exibir ticket médio no terminal
print(f'Ticket médio por pedido: R$ {ticket_medio:.2f}')
