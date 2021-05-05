import sqlite3
import json
import requests
import codecs
import time

file = codecs.open('data_tech.json', 'r', 'utf-8-sig')
j_data = json.load(file)

conn = sqlite3.connect('glossary.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE tamil_glossary
             ([id] INTEGER PRIMARY KEY, [subject] text, [en_term] text, [ta_term] text)''')

for i, item in enumerate(j_data['tamil_glossary']):
    id = int(time.time() * 1000)
    subject = item['subject']
    en_term = item['en_term']
    ta_term = item['ta_term']
    print('inserting...%d' % i)
    query = "INSERT INTO tamil_glossary ('id', 'subject', 'en_term', 'ta_term') VALUES (?, ?, ?, ?);"
    value = (id, subject, en_term, ta_term)
    cursor.execute(query, value)
    conn.commit()

conn.close()
