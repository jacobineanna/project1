import pandas as pd
netflix = pd.read_csv("netflix.csv")




def start():
    jaar = netflix["releaseYear"].tolist()

    return jaar

