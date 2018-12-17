import sqlite3
import pandas as pd

import datetime


def connect():
    return sqlite3.connect('../mysite/sqlite3.db')


def insert_orgao(orgaos):
    pg_conn = connect()
    cursor = pg_conn.cursor()
    # for each in orgaos:
    for key, value in orgaos.items():
        # print (value)
        cursor.execute(
            "INSERT INTO organograma_orgao (nome, responsavel, funcao, local)"
            " VALUES ( ? , ? , ? , 'Av. Marechal camara 370') "
            , (value['nome'], value['responsavel'], value['funcao']))
    pg_conn.commit()


def insert_pessoa(r):
    pg_conn = connect()
    cursor = pg_conn.cursor()
    # print (r)
    cursor.execute(
        "INSERT INTO organograma_pessoa (nome, texto ,cargo , salario,  funcao ) "
        "VALUES ( ? , ? , ? , ? ,? )  ",
        (r['NOME'], r['Descrição da Função'], r['Cargo'], float(r['Remuneração do cargo efetivo'].replace('R$ ', '').replace('.', '').replace(',', '.')), r['FUNÇÃO']))
    new_id = cursor.lastrowid

    conjunt_que_atua = str(r['Projetos Relacionados']).strip()
    # print(conjunt_que_atua)
    if conjunt_que_atua:
        conjunt_que_atua = conjunt_que_atua.replace(';', '')
        for p in conjunt_que_atua.split('\n'):
            project_key = p.split('-')[0].strip().upper()
            cursor.execute(
                " insert into organograma_pessoa_projetos (pessoa_id, projeto_id )"
                " select ?,  p.id from organograma_projeto p where p.nome = ? "
                , (new_id, project_key))

    pg_conn.commit()


def insert_projeto(projetos):
    pg_conn = connect()
    cursor = pg_conn.cursor()
    for key, value in projetos.items():
        cursor.execute(
            " INSERT INTO organograma_projeto (nome, updated_at, orgao_id) "
            " SELECT  trim(?) as n ,  ?, id from organograma_orgao where nome = ? "
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
            # print (row)
    orgaos = {}
    for pessoa in result:
        if pessoa['LOTAÇÃO'] not in orgaos:
            orgaos[pessoa['LOTAÇÃO']] = {'nome': pessoa['LOTAÇÃO'],
                                        'responsavel': pessoa['NOME'],
                                        'funcao': pessoa['FUNÇÃO'],
                                        'salario':pessoa['Rendimento líquido total']}
    return orgaos

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
                # print(projeto)
                if projeto['nome'] not in result:
                    projeto['lotacao'] = row['LOTAÇÃO']
                    if len(nome_texto) > 1:
                        projeto['texto'] = nome_texto[1]
                    result[project_key] = projeto
    print(result)
    return result

excel = pd.read_excel("../resources/gsi.xlsx")

# print(extract_organ(excel))
# insert_orgao(extract_organ(excel))
# # extract_project(excel)
# insert_projeto(extract_project(excel))
#
for index, row in excel.iterrows():
    insert_pessoa(row)
# print(row['NOME'])
