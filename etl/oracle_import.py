from etl.oracle import oracle_connection
import psycopg2

# postgres_conection = psycopg2.connect(
#   "dbname='postgres' user='bi' host='d-postgres01.pgj.rj.gov.br' password='bi_des'")
postgres_conection = psycopg2.connect(
    "dbname='sgfmqpzj' user='sgfmqpzj' host='elmer.db.elephantsql.com' password='YrB-Ge294Cn9buQQGD665hSUbZaCRy9Y'")

stic_db = postgres_conection.cursor()
cursor = oracle_connection().cursor()

sql = """ select
        RE.RREP_MES_ANO_PAGTO MES_ANO,
        RE.RREP_CDMATRICULA_FUNCIONARIO MATRICULA,
        RE.RREP_NOME NOME,
        RE.RREP_REMUN_CARGO_EF CARGO_EF,
        RE.RREP_FUNC_CONF_CG_COMIS CARGO_COMISS,
        F.FOTO,
        RE.RREP_NMORGAO,
        RE.RREP_DESCONTOS,
        RE.RREP_FERIAS,
        RE.RREP_GRATIFIC_NATAL,
        RE.RREP_INDENIZACOES,
        RE.RREP_IR,
        RE.RREP_LIQUIDO,
        RE.RREP_MES_ANO_PAGTO,
        RE.RREP_NMCARGO,
        RE.RREP_OUTRAS_VERB_REMUN,
        RE.RREP_PREVIDENCIA,
        RE.RREP_TETO,
        RE.RREP_RETROATIVOS,
        RE.RREP_TOTAL_BRUTO
    from RH_REMUNERACAO_PT re
    join RH_FUNCIONARIO fu on RE.RREP_CDMATRICULA_FUNCIONARIO = Fu.CDMATRICULA
    left join RH_FUNC_IMG f on RE.RREP_CDMATRICULA_FUNCIONARIO = F.CDMATRICULA
    where
        to_date(RE.RREP_MES_ANO_PAGTO,	'mmyyyy') = (select max( add_months(to_date(RE2.RREP_MES_ANO_PAGTO, 'mmyyyy'), -2))
        from RH_REMUNERACAO_PT re2)
        and RE.RREP_NUM_PENSAO = 0
        and FU.CDORGAO in (
            select  distinct OO.ORGI_CDORGAO from ORGI_ORGAO oo 
            connect by prior OO.ORGI_Dk = OO.ORGI_ORGI_DK_SUPERIOR
            start with OO.ORGI_DK = 400802 
        ) order by  RE.RREP_NMORGAO, RE.RREP_NOME
"""
cursor.execute(sql)

for each in cursor:
    texto = each[1]
    nome = each[2]
    foto = each[5]
    if foto:
        fotostream = foto.read()
    else:
        fotostream = None
    salario = each[19]
    cargo = each[14]

    print(each)
    id = stic_db.execute(
        "INSERT INTO organograma_pessoa (nome, texto ,cargo , salario, foto, funcao ) VALUES ( %s , %s , %s , %s ,%s , 'x' ) ",
        (nome, texto, cargo, salario, fotostream, ))

postgres_conection.commit()


sql = """select distinct *
        from
            ORGI_ORGAO oo
        WHERE ORGI_DT_FIM IS null
        connect by
            prior OO.ORGI_Dk = OO.ORGI_ORGI_DK_SUPERIOR
        start with
            OO.ORGI_DK = 400802 """
cursor.execute(sql)

for each in cursor:
    id = each[0]
    nome = each[6]
    print(each)
    stic_db.execute("INSERT INTO organograma_orgao (nome, texto) VALUES ( %s , %s ) ", (nome,id,))
postgres_conection.commit()


# ********************************
sql = """
        select
            RE.RREP_CDMATRICULA_FUNCIONARIO MATRICULA,
            RE.RREP_NOME NOME,
            RE.RREP_REMUN_CARGO_EF CARGO_EF,
            RE.RREP_FUNC_CONF_CG_COMIS CARGO_COMISS,
            F.FOTO,
            RE.RREP_NMORGAO,
            RE.RREP_NMCARGO
        from RH_REMUNERACAO_PT re
        join RH_FUNCIONARIO fu on RE.RREP_CDMATRICULA_FUNCIONARIO = Fu.CDMATRICULA
        left join RH_FUNC_IMG f on RE.RREP_CDMATRICULA_FUNCIONARIO = F.CDMATRICULA
        where
            to_date(RE.RREP_MES_ANO_PAGTO,	'mmyyyy') = (select max(to_date(RE2.RREP_MES_ANO_PAGTO, 'mmyyyy') )
            from RH_REMUNERACAO_PT re2)
            and RE.RREP_NUM_PENSAO = 0
            and FU.CDORGAO in (
                select distinct OO.ORGI_CDORGAO
                from ORGI_ORGAO oo
                connect by prior OO.ORGI_Dk = OO.ORGI_ORGI_DK_SUPERIOR
                start with OO.ORGI_DK = 400802 )
            AND Fu.CDMATRICULA IN (00007349,00006984, 00006276 , 00007774, 00809786, 08005075, 00003612, 00006419, 00004328,00002235)		
        order by
            RE.RREP_NMORGAO,
            RE.RREP_NOME
        """
cursor.execute(sql)

for each in cursor:
    print(each)
    nome = each[1]
    foto = each[4]
    orgao = each[5]
    cargo = each[6]
    if foto:
        fotostream = foto.read()
    else:
        fotostream = None
    stic_db.execute("UPDATE organograma_orgao set  responsavel = %s ,  funcao = %s, foto  = %s where nome = %s ",
                    (nome, cargo, fotostream, orgao,))

postgres_conection.commit()
