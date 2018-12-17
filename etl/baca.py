import sqlite3
import pandas as pd

import datetime


con = sqlite3.connect('../mysite/sqlite3.db')

con.cursor()

con.execute("insert into organograma_orgao "
            "(sigla, nome, texto , responsavel ,funcao, local,  telefone, email)"
            "values (? , ? , ? , ? ,?, ? ,? ,?) " ,
            ()
            )


