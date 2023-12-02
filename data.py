#@title Imports
import json
import requests
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier




url = "https://ballchasing.com/api/groups/9amateur-zmcevpgmnn/"
headers = {'Authorization': '8wjl1G9d8V8Ymfju7hH8K57aKNUiNhYe5oOYOxNr'}

response = requests.get(url, headers=headers)
data = json.loads(response.text)

with open('S8-1Premier.json') as f:
    data = json.load(f)
    df1 = pd.json_normalize(data['players'])

with open('S8-2Master.json') as f:
    data = json.load(f)
    df2 = pd.json_normalize(data['players'])

with open('S8-3Elite.json') as f:
    data = json.load(f)
    df3 = pd.json_normalize(data['players'])

with open('S8-4Veteran.json') as f:
    data = json.load(f)
    df4 = pd.json_normalize(data['players'])

with open('S8-5Rival.json') as f:
    data = json.load(f)
    df5 = pd.json_normalize(data['players'])

with open('S8-6Challenger.json') as f:
    data = json.load(f)
    df6 = pd.json_normalize(data['players'])

with open('S8-7Contender.json') as f:
    data = json.load(f)
    df7 = pd.json_normalize(data['players'])

with open('S8-8Prospect.json') as f:
    data = json.load(f)
    df8 = pd.json_normalize(data['players'])

with open('S8-9Amateur.json') as f:
    data = json.load(f)
    df9 = pd.json_normalize(data['players'])

df1['rank'] = 1
df2['rank'] = 2
df3['rank'] = 3
df4['rank'] = 4
df5['rank'] = 5
df6['rank'] = 6
df7['rank'] = 7
df8['rank'] = 8
df9['rank'] = 9

df = pd.concat([df1, df2, df3, df4, df5, df6, df7, df8, df9])

# Drop the 'teams' column
df = df.drop('id', axis=1)
df = df.drop('platform', axis=1)
df = df.drop('name', axis=1)
df = df.drop('team', axis=1)

X = df.drop('rank', axis=1)
y = df['rank']

# Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Scale the data
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

model = KNeighborsClassifier(n_neighbors=i)
model.fit(X_train, y_train)
print(f'{i}: {model.score(X_test, y_test)}')

# Create and train the model
model = KNeighborsClassifier(n_neighbors=i)
model.fit(X_train, y_train)

# Check the accuracy of the model
accuracy = model.score(X_test, y_test)
print(f'Accuracy: {accuracy * 100}%')

    