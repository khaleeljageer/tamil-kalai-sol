import json
import requests
import codecs

file = codecs.open('data_tech.json', 'r', 'utf-8-sig')
j_data = json.load(file)

headers = {
    'accept' : 'application/json',
    'Authorization' : 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MSwiaWF0IjoxNjE5NjcyMjcxLCJleHAiOjE2MjIyNjQyNzF9.TGyJ-KcVx2_Gxo6utmnK5d_DkqBDcMUa6TNN25zI6is',
    'Content-Type' : 'application/json'
}

for item in j_data['tamil_glossary']:
    data = {
        'subject' : item['subject'],
        'en_term' : item['en_term'],
        'ta_term' : item['ta_term']
    }
    r = requests.post('http://localhost:1337/tamil-glossaries', data= json.dumps(data, ensure_ascii=False).encode('utf-8'), headers=headers)
    print(r.status_code)