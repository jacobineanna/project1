import pandas as pd
from json import loads, dumps
netflix = pd.read_csv("netflix.csv")
import pyodbc


def start():
    jaar = netflix.head(100)
    result = jaar.to_json(orient="records")
    parsed = loads(result)
    print(jaar)
    return dumps(parsed, indent=4)
    
def azure():
    connection_string = (
    "DRIVER={SQL Server};"        # Driver
    "SERVER=datadbserverdamen.database.windows.net;"         # Naam of IP van de server
    "DATABASE=sebasindebocht;"     # Naam van de database
    "UID=admindamen;"               # Gebruikersnaam
    "PWD=uiop7890UIOP&*();"               # Wachtwoord
)

# Maak verbinding met de database
    try:
        connection = pyodbc.connect(connection_string)
        print("Verbinding succesvol!")
    except pyodbc.Error as e:
        print("Fout bij verbinden:", e)

    cursor = connection.cursor()
    try:
    # Vervang 'jouw_tabel_naam' door de naam van je tabel
        cursor.execute("SELECT * FROM vissen")
    
    # Haal alle resultaten op
        rows = cursor.fetchall()

        for row in rows:
            print(row)
    except pyodbc.Error as e:
        print("Fout bij het uitvoeren van de query:", e)

    return "Azure doet het!"