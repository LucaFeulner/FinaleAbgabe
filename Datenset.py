import pandas as pd

#_______________________________________________________________________________________________________________________________________________________

#________________________________________________________Datenasätze____________________________________________________________________________________
#_______________________________________________________________________________________________________________________________________________________


# Diese Datei benutze ich um alle Datensets seperat in einer Datei zu haben
# Aus dem Datenset wird (Zeile 20 ) nur der Januar genommen, da es sonst zu groß ist


#-------------------------Datensets einlesen-------------------------


# Aus dem Datenset wurde nur der Januar genommen, da es sonst zu groß ist


# df1 = pd.read_csv("FinaleAbgabe/res/AbgabeDatenset.csv")
#df1 = df1[df1["MONTH"] == 1]
# df_flughafen_namen = pd.read_csv("FinaleAbgabe/res/airports.csv", sep=";")
# df_fluggesellschaft_namen = pd.read_csv("FinaleAbgabe/res/airlines.csv", sep=",")

#----------Spalte umnennen  da  sonst zwei mal die selbe spalte existiert
# df_fluggesellschaft_namen =df_fluggesellschaft_namen.rename(columns={"AIRLINE":"AIRLINE_NAME"})

#----------Die drei Datensets  zun einem zusammenfügen
# df2 = pd.merge(df1, df_flughafen_namen[['IATA_CODE', 'STATE', "AIRPORT"]], left_on='ORIGIN_AIRPORT', right_on='IATA_CODE', how='left')
# df3 = pd.merge(df2, df_fluggesellschaft_namen[['IATA_CODE', "AIRLINE_NAME"]], left_on="AIRLINE", right_on="IATA_CODE", how="left")

#----------Entferne die Spalte "IATA_CODE"
# df3.drop('IATA_CODE_x', axis=1, inplace=True)
# df3.drop('IATA_CODE_y', axis=1, inplace=True)

#----------Staatennamen für Mapbox einfügen wegen der jason Datei
#df_staaten_namen = pd.read_csv("FinaleAbgabe/res/staates.csv", sep=",")

#df = pd.merge(df3, df_staaten_namen[['Postal', 'State']], left_on='STATE', right_on='Postal', how='left')
#----------Spalte mit den abkürzungen doppelt also raus
#df.drop('Postal', axis=1, inplace=True)

#df.to_csv("FinaleAbgabe/res/FinalesDatenset.csv")