import sqlite3

try:           # Parte da Criação do BANCO DE DADOS
    conexao = sqlite3.connect("banco_de_dados.db") # Sustituir nome do banco de dados pelo definitivo
    cursor = conexao.cursor()

    cursor.execute("CREATE TABLE IF NOT EXISTS servicos(id_servico INTEGER PRIMARY KEY AUTOINCREMENT, id_cliente TEXT, id_prestador TEXT, data DATE, horario DATE, descricao_servico TEXT, valor DECIMAL(10,2), id_endereco TEXT, status TEXT)")
    conexao.commit()
    # Observar que alguns objetos da tabela serão ID's CHAVE SECUNDARIA DE OUTRAS TABELAS
except sqlite3.Error as erro:
    print('Erro no BD: ', erro)


def cadastrar_servico(id_cliente, id_prestador, id_endereco): # Função para cadastrar Serviço no BD
    try:
        data = input('Informe a data do Servico: ')
        horario = input('Informe o horario do Serviço: ')
        cursor.execute("SELECT id_servico FROM servicos WHERE id_prestador = ? AND data = ? AND horario = ?",(id_prestador, data, horario))
        if cursor.fetchone() is not None:   # Verifica se a Data e horario do Prestador já esta ocupada
           print('Esta Data/Horario não esta disponivel!')
           return
        else:
            print('Data Disponivel!')
            descricao_servico = input('Descreva o Seriço: ')
            valor = float(input('Informe o valor a ser pago pelo Serviço: '))
            status = input('Informe o Status do Serviço: ')
            cursor.execute("INSERT INTO servicos(id_cliente, id_prestador, data, horario, descricao_servico, valor, id_endereco, status) VALUES(?,?,?,?,?,?,?,?)",(id_cliente, id_prestador, data, horario,descricao_servico, valor, id_endereco, status))
            conexao.commit()
            print('Serviço Agendado com Sucesso!')

    except Exception as erro:
        print('Erro ao Cadastrar Serviço! ', erro)

cadastrar_servico(1, 111, 'Rua das Rosas')
