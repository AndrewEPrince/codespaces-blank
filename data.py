#@title Imports
import json
import requests
import pandas as pd
import numpy as np

url = "https://ballchasing.com/api/groups/9amateur-zmcevpgmnn/"
headers = {'Authorization': '8wjl1G9d8V8Ymfju7hH8K57aKNUiNhYe5oOYOxNr'}

response = requests.get(url, headers=headers)
data = json.loads(response.text)

with open('S8-1Premier.json') as f:
    data = json.load(f)
    df1 = pd.json_normalize(data)

with open('S8-2Master.json') as f:
    data = json.load(f)
    df2 = pd.json_normalize(data)

with open('S8-3Elite.json') as f:
    data = json.load(f)
    df3 = pd.json_normalize(data)

with open('S8-4Veteran.json') as f:
    data = json.load(f)
    df4 = pd.json_normalize(data)

with open('S8-5Rival.json') as f:
    data = json.load(f)
    df5 = pd.json_normalize(data)

with open('S8-6Challenger.json') as f:
    data = json.load(f)
    df6 = pd.json_normalize(data)

with open('S8-7Contender.json') as f:
    data = json.load(f)
    df7 = pd.json_normalize(data)

with open('S8-8Prospect.json') as f:
    data = json.load(f)
    df8 = pd.json_normalize(data)

with open('S8-9Amateur.json') as f:
    data = json.load(f)
    df9 = pd.json_normalize(data)

