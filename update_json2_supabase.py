import json
import requests
import codecs
import config

file = codecs.open('data/data_tech.json', 'r', 'utf-8-sig')
j_data = json.load(file)
tamil_glossary = j_data['tamil_glossary']

res = requests.post(url=config.tn_glossary_url, headers=config.supabase_headers, data=json.dumps(tamil_glossary))
print(res.status_code)