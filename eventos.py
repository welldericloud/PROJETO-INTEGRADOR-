
import sqlite3

try:
    # Criação do Banco de Dados Evebtos
    conexao = sqlite3.connect('bd_geral.db')
    cursor = conexao.cursor()

    # Criando Tabela
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS eventos (
            id_evento INTEGER PRIMARY KEY AUTOINCREMENT,
            id_organizador TEXT,
            titulo TEXT,
            categoria TEXT,
            nome_local TEXT,
            endereco TEXT,
            data DATE,
            horario TIME,
            valor_entrada DECIMAL(10,2),
            descricao TEXT,
            imagem TEXT,
            status TEXT DEFAULT 'PUBLICADO',
            destaque INTEGER DEFAULT 0
        )
    """)

    conexao.commit()

    print('Tabela de eventos criada com sucesso!')

except sqlite3.Error as erro:
    print('Erro no Banco de Dados! ', erro)

finally:
    if 'conexao' in locals():
        conexao.close()
