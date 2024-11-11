import pandas as pd

df = pd.read_excel('Нагрузка для чтения.csv', engine='openpyxl', header=[0, 1])


print(df.head())

json_data = df.to_json(orient='records', force_ascii=False)

with open('output.json', 'w', encoding='utf-8') as f:
    f.write(json_data)
    #appaa
