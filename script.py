import sqlite3
import pandas as pd

# Conectando ao banco SQLite (se não existir, será criado)
conn = sqlite3.connect('ecommerce.db')
cursor = conn.cursor()

# Criando as tabelas
cursor.execute('''
CREATE TABLE IF NOT EXISTS clientes (
    cliente_id INTEGER PRIMARY KEY,
    nome TEXT,
    email TEXT,
    data_cadastro DATE,
    cidade TEXT,
    estado TEXT
);
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS produtos (
    produto_id INTEGER PRIMARY KEY,
    nome TEXT,
    categoria TEXT,
    preco REAL
);
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS pedidos (
    pedido_id INTEGER PRIMARY KEY,
    cliente_id INTEGER,
    data_pedido DATE,
    canal_venda TEXT,
    status TEXT,
    FOREIGN KEY (cliente_id) REFERENCES clientes(cliente_id)
);
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS itens_pedido (
    item_id INTEGER PRIMARY KEY,
    pedido_id INTEGER,
    produto_id INTEGER,
    quantidade INTEGER,
    preco_unitario REAL,
    FOREIGN KEY (pedido_id) REFERENCES pedidos(pedido_id),
    FOREIGN KEY (produto_id) REFERENCES produtos(produto_id)
);
''')

# Carregando dados dos arquivos .csv
clientes_df = pd.read_csv('clientes.csv')
produtos_df = pd.read_csv('produtos.csv')
pedidos_df = pd.read_csv('pedidos.csv')
itens_pedido_df = pd.read_csv('itens_pedido.csv')

# Inserindo dados nas tabelas
clientes_df.to_sql('clientes', conn, if_exists='replace', index=False)
produtos_df.to_sql('produtos', conn, if_exists='replace', index=False)
pedidos_df.to_sql('pedidos', conn, if_exists='replace', index=False)
itens_pedido_df.to_sql('itens_pedido', conn, if_exists='replace', index=False)

# Commit e fechamento da conexão
conn.commit()
conn.close()

print("Banco de dados populado com sucesso!")
