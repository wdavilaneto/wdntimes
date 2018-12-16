import pandas as pd
import psycopg2

import datetime


def connect():
    return psycopg2.connect(
        "dbname='sgfmqpzj' user='sgfmqpzj' host='elmer.db.elephantsql.com' password='YrB-Ge294Cn9buQQGD665hSUbZaCRy9Y'")


def insert_orgao(orgaos):
    pg_conn = connect()
    cursor = pg_conn.cursor()
    for each in orgaos:
        cursor.execute(
            "INSERT INTO organograma_orgao (nome, responsavel, funcao, local)"
            " VALUES ( %s , %s , %s , 'Av. Marechal camara 370') "
            , (each['LOTAÇÃO'], each['NOME'], each['FUNÇÃO']))
    pg_conn.commit()


def insert_pessoa(r):
    pg_conn = connect()
    cursor = pg_conn.cursor()
    # print (r)
    cursor.execute(
        "INSERT INTO organograma_pessoa (nome, texto ,cargo , salario,  funcao ) "
        "VALUES ( %s , %s , %s , %s ,%s ) RETURNING id ",
        (r['NOME'], r['Descrição da Função'], r['Cargo'], float(r['Remuneração do cargo efetivo'].replace('R$ ', '').replace('.', '').replace(',', '.')), r['FUNÇÃO']))
    new_id = cursor.fetchone()[0]

    conjunt_que_atua = str(r['Projetos Relacionados']).strip()
    # print(conjunt_que_atua)
    if conjunt_que_atua:
        conjunt_que_atua = conjunt_que_atua.replace(';', '')
        for p in conjunt_que_atua.split('\n'):
            project_key = p.split('-')[0].strip().upper()
            cursor.execute(
                " insert into organograma_pessoa_projetos (pessoa_id, projeto_id )"
                " select %s,  p.id from organograma_projeto p where p.nome = %s "
                , (new_id, project_key))

    pg_conn.commit()


def insert_projeto(projetos):
    pg_conn = connect()
    cursor = pg_conn.cursor()
    for key, value in projetos.items():
        cursor.execute(
            " INSERT INTO organograma_projeto (nome, updated_at, orgao_id) "
            " SELECT  trim(%s) as n ,  %s, id from organograma_orgao where nome = %s "
            , (key, datetime.datetime.now(), value['lotacao'],))
    pg_conn.commit()


def extract_organ(excel):
    responsaveis = ['WALTER D`AVILA NETO']
    # orgaos = extrato["LOTAÇÃO"].unique()
    # print(orgaos)
    result = []
    for each in responsaveis:
        gerente = excel.loc[excel['NOME'] == each]
        for i, row in gerente.head(1).iterrows():
            result.append(row)
    print(result)
    return result


def extract_project(excel):
    result = dict()
    for i, row in excel.iterrows():
        conjunt_que_atua = str(row['Projetos Relacionados']).strip()
        # print(conjunt_que_atua)
        if conjunt_que_atua:
            conjunt_que_atua = conjunt_que_atua.replace(';', '')
            for p in conjunt_que_atua.split('\n'):
                projeto = {}
                nome_texto = p.split(' - ')
                project_key = nome_texto[0].strip().upper()
                projeto['nome'] = project_key
                print(projeto)
                if projeto['nome'] not in result:
                    projeto['lotacao'] = row['LOTAÇÃO']
                    if len(nome_texto) > 1:
                        projeto['texto'] = nome_texto[1]
                    result[project_key] = projeto
    # print (result)
    return result

excel = pd.read_excel("../resources/gsi.xlsx")

# inset_orgao(extract_organ(excel))
# extract_project(excel)
# insert_projeto(extract_project(excel))

for index, row in excel.iterrows():
    insert_pessoa(row)
# print(row['NOME'])
