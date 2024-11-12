import pandas as pd
from json import loads, dumps
netflix = pd.read_csv("netflix.csv")


def start():
    jaar = netflix.head(100)
    result = jaar.to_json(orient="records")
    parsed = loads(result)
    print(jaar)
    return dumps(parsed, indent=4)
    