import pandas as pd
from json import loads, dumps

def start():
    file_path = 'meat_consumption_worldwide.csv'  
    df = pd.read_csv(file_path)
    df = df.head(20)
    print(df)
    result = df.to_json(orient="records")
    parsed = loads(result)
    return dumps(parsed, indent=4) 