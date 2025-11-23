from sqlalchemy import create_engine, text


USER = "postgres"
PASSWORD = "gui123reis13"
HOST = "localhost"
PORT = "5433"
DB = "tp3-pb"
SCHEMA = "mercadinho"

DATABASE_URL = (
    f"postgresql+psycopg2://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB}"
    f"?options=-csearch_path%3D{SCHEMA}"
)

engine = create_engine(DATABASE_URL)

# CONSULTAS (SQL PURO)


sql_inner_join = text("""
    SELECT c.nome AS cliente, c.telefone, v.data
    FROM clientes c
    INNER JOIN vendas v ON c.id_cliente = v.id_cliente;
""")

sql_left_join = text("""
    SELECT cat.nome AS categoria, p.nome AS produto
    FROM categorias cat
    LEFT JOIN produtos p ON cat.id_categoria = p.id_categoria;
""")

sql_right_join = text("""
    SELECT p.nome AS produto, cat.nome AS categoria
    FROM produtos p
    RIGHT JOIN categorias cat ON p.id_categoria = cat.id_categoria;
""")

# EXECUÇÃO DAS CONSULTAS E POPULAÇÃO EM LISTAS


with engine.connect() as conn:
    inner_join_lista = [dict(row) for row in conn.execute(sql_inner_join).fetchall()]
    left_join_lista = [dict(row) for row in conn.execute(sql_left_join).fetchall()]
    right_join_lista = [dict(row) for row in conn.execute(sql_right_join).fetchall()]

# EXIBIÇÃO DOS RESULTADOS


print("\n=== INNER JOIN: CLIENTES COM VENDAS ===")
for item in inner_join_lista:
    print(item)

print("\n=== LEFT JOIN: CATEGORIAS E PRODUTOS ===")
for item in left_join_lista:
    print(item)

print("\n=== RIGHT JOIN: PRODUTOS E CATEGORIAS ===")
for item in right_join_lista:
    print(item)
