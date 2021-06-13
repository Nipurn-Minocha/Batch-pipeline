import os
import time
import pandas as pd
import psycopg2

sslmode = "sslmode=verify-ca"
sslrootcert = "sslrootcert={}".format(os.environ['PG_SSLROOTCERT'])
sslcert = "sslcert={}".format(os.environ['PG_SSLCERT'])
sslkey = "sslkey={}".format(os.environ['PG_SSLKEY'])
hostaddr = "hostaddr={}".format(os.environ['PG_HOST'])
user = "user=postgres"
password = "password={}".format(os.environ['PG_PASSWORD'])
dbname = "dbname=mgmt-qa-model"

# Construct database connect string
db_connect_string = " ".join([
    sslmode,
    sslrootcert,
    sslcert,
    sslkey,
    hostaddr,
    user,
    password,
    dbname
])

df_new = pd.read_csv(os.path.join("/pfs/getfiles/", "answer_db.csv"))

con = psycopg2.connect(db_connect_string)
cur = con.cursor()
for i,row in df_new.iterrows():
    sql = "INSERT INTO answers VALUES ('{question}','{context}','{model}','{answer}', '{timestamp}')"
    timestamp = int(time.time())
    cur.execute(sql.format(
        question=row['question'].replace("'", "''"),
        context=row['context'].replace("'", "''"),
        model = "distiled-bert",
        answer=row['answer'].replace("'", "''"),
        timestamp=str(timestamp)))
    con.commit()
con.close()
