import sqlite3
import pandas as pd

import datetime

con = sqlite3.connect('../mysite/sqlite3.db')

cursor = con.cursor()


def insert_secretario():
    cursor.execute("insert into organograma_orgao "
                   "(sigla, nome, texto , responsavel ,funcao, local,  telefone, email)"
                   "values (? , ? , ? , ? ,?, ? ,? ,?) ",
                   ('STIC', 'SECRETARIA DE TECNOLOGIA DA INFORMAÇÃO E DE COMUNICAÇÃO', '', 'SANDRO DENIS DE SOUZA NUNES', 'SECRETÁRIO DE TI',
                    'Av. Marechal Camara 370', '(21) 2222-2222', 'sandro.nunes@mprj.mp.br'
                    ))
    # cursor.commit()


glp = [{
    'MGPE JUDICIAL': 34,
    'SINALID': 110,
    'MGPE EXTRAJUDICIAL': 115,
    'CLIC': 169,
}]

times = [
    {'nome': 'Judicial', }
]


def insert_secretario():
    cursor.execute("insert into organograma_orgao "
                   "(sigla, nome, texto , responsavel ,funcao, local,  telefone, email)"
                   "values (? , ? , ? , ? ,?, ? ,? ,?) ",
                   ('STIC', 'SECRETARIA DE TECNOLOGIA DA INFORMAÇÃO E DE COMUNICAÇÃO', '', 'SANDRO DENIS DE SOUZA NUNES', 'SECRETÁRIO DE TI',
                    'Av. Marechal Camara 370', '(21) 2222-2222', 'sandro.nunes@mprj.mp.br'
                    ))
    # cursor.commit()
