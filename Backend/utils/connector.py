import pyodbc
import pandas as pd 


class connection:
    connection = None


    def __init__(self):
        self.connect()
        # self.populate()

    def connect(self):
        connection_string = (
        "DRIVER={SQL Server};"        # Driver
        "SERVER=datadbserverdamen.database.windows.net;"         # Naam of IP van de server
        "DATABASE=sebasindebocht;"     # Naam van de database
        "UID=admindamen;"               # Gebruikersnaam
        "PWD=uiop7890UIOP&*();"               # Wachtwoord
        )
        try:
            self.connection = pyodbc.connect(connection_string)
            print("Verbinding succesvol!")
        except pyodbc.Error as e:
            print("Fout bij verbinden:", e)

    def populate(self):

        # extract
        # dit laad de csv in een dataframe
        df = pd.read_csv("./HBO_Max.csv")
        
        try:
            cursor = self.connection.cursor()

            # dit verwijderd niet de database maar de inhoud ervan
            cursor.execute("TRUNCATE TABLE dbo.HBO_Max;")
            for i, row in df.iterrows():
                print(row)
                cursor.execute("INSERT INTO dbo.HBO_Max (title, type, genres, releaseYear, imdbId, imdbAverageRating, imdbNumVotes, availableCountries) VALUES(?,?,?,?,?,?,?,?)",
                                row["title"], row["type"], row["genres"], row["releaseYear"], row["imdbId"], row["imdbAverageRating"], row["imdbNumVotes"], row["availableCountries"])
                
                
        except Exception as e:
            print(e)
            print(f'Exception at populate: {e}')


    def get_all(self):
        #  this should return all rows in the db

        # lege array om de rows in te doen
        data = []
        try:
            cursor = self.connection.cursor()

            # we maken hier de query die alle rows ophaalt van de tabel HBO_Max 
            cursor.execute("SELECT * FROM HBO_Max ;")
            rows = cursor.fetchall()

            # Omdat pyodbc beetje ruwe is moeten we het nog omzetten naar een standaard array 
            for row in rows:
                data.append([x for x in row])

            # deze code is alleen als er iets hierboven fout gaat dat de server niet helemaal crashed
        except Exception as e:
            print(f'Get all went kinda wrong: {e}')
        

        return data


