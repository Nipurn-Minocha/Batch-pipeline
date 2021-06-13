import os
import io
from io import BytesIO
from google.cloud import storage
import pandas as pd
from transformers.pipelines import pipeline

distiled = pipeline('question-answering', model="distilbert-base-uncased-distilled-squad", tokenizer="distilbert-base-uncased-distilled-squad")

storage_client = storage.Client()
bucket = storage_client.get_bucket('psdp-assignment-mgmt-nipurn')

files = bucket.list_blobs()
fileList = [file.name for file in files if '.' in file.name]

answers = []
df1 = pd.DataFrame()
df2 = pd.DataFrame()
for i in fileList:
    blob = bucket.blob(i)
    data = blob.download_as_string()
    df_read = pd.read_csv(io.BytesIO(data), encoding = 'utf-8', sep = ',')
    df1 = df1.append(df_read,ignore_index = True)
    bucket.delete_blob(i)
    for i,row in df_read.iterrows():
        context = row['context']
        question = row['question']
        answer = distiled({'question': question, 'context': context})['answer']
        answers.append(answer)

df2['context'] = df1['context']
df2['question'] = df1['question']
df2['answer'] = answers

df2.to_csv("pfs/out/answer_db.csv", index=False)
