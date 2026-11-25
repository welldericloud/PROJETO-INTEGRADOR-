import sqlite3

try:    # Criação do Banco de Dados - Geral (Wellder)
    conexao = sqlite3.connect('bd_geral.db')
    cursor = conexao.cursor()

    # Criando Tabela de AGENDAMENTOS - WELLDER
    cursor.execute("CREATE TABLE IF NOT EXISTS agendamento(id_servico INTEGER PRIMARY KEY AUTOINCREMENT, id_cliente TEXT, id_prestador TEXT, data DATE, horario DATE, descricao_servico TEXT, valor DECIMAL(10,2), id_endereco TEXT, status TEXT)")
    conexao.commit()

#    cursor.execute("INSERT INTO agendamento(id_cliente, id_prestador, data, horario, descricao_servico, valor, id_endereco, status) VALUES(?,?,?,?,?,?,?,?)",(11, 111, '15/02/2026', '15:30', 'Reparo de uma Pia', 150.00, 5, 'CONCLUIDO'))
#    conexao.commit()
#   ESSE INSERT FOI USADO SÓ PARA TESTE DO CODIGO

except sqlite3.Error as erro:
    print('Erro no Banco de Dados! ', erro)