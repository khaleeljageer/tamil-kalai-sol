import sqlite3
import json
import requests
import codecs
import time

file = codecs.open('data_tech.json', 'r', 'utf-8-sig')
j_data = json.load(file)

conn = sqlite3.connect('glossary.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE tamilGlossary
             ([id] INTEGER PRIMARY KEY NOT NULL, [subject] TEXT NOT NULL, [en_term] TEXT NOT NULL, [ta_term] TEXT NOT NULL)''')

for index, item in enumerate(j_data['tamil_glossary']):
    id = index
    subject = item['subject']
    en_term = item['en_term']
    ta_term = item['ta_term']
    print('inserting...%d' % index)
    query = "INSERT INTO tamilGlossary ('id', 'subject', 'en_term', 'ta_term') VALUES (?, ?, ?, ?);"
    value = (id, subject, en_term, ta_term)
    cursor.execute(query, value)
    conn.commit()

conn.close()
