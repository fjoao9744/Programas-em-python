import sqlite3


def salvar_dados(dados):
    if dados["pontos"] != 0:
        conn = sqlite3.connect(r"nivel 3\jogo de matematica\database.db")
        cursor = conn.cursor()

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS pontos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT,
        pontos INTEGER NOT NULL
        )
        """)

        conn.commit()

        cursor.execute("""
        INSERT INTO pontos (nome, pontos) VALUES 
        (?, ?) """,
        (dados['nome'], dados['pontos']))

        conn.commit()

def exibir_dados():
    conn = sqlite3.connect(r"nivel 3\jogo de matematica\database.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS pontos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT,
    pontos INTEGER NOT NULL
    )
    """)

    conn.commit()

    cursor.execute(""" SELECT nome, pontos FROM pontos
    ORDER BY pontos DESC
    LIMIT 5""")

    return cursor.fetchall()


    

