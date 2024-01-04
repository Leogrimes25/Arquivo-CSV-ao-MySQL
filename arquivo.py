import csv
import mysql.connector

try:

    conexao = mysql.connector.connect(host='localhost', user='root', password='vinicius', database='objetivos')
    cursor = conexao.cursor(dictionary=True)
    print("Conexão Estabelecida !")

except ConnectionError:
    print("Conexão Inválida")

entrada = r"C:\Users\Vinicius Oliveira\Desktop\Mineração Dados\Cópia de Objetivos de aprendizagem pós aula (1).csv"


def enviar_arquivo():
    with open(entrada, 'r', encoding='utf-8') as arquivo_entrada:
        leitor = csv.reader(arquivo_entrada)
        next(leitor, None)
        for linha in leitor:
            query = "INSERT INTO objetivos1 (nome, grupos, email, datas, questao1, questao2, questao3, questao4) " \
                    "VALUES ({})".format(', '.join(['%s'] * len(linha)))
            cursor.execute(query, linha)
            conexao.commit()


enviar_arquivo()
