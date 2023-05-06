import plotly.graph_objects as go
import pandas as pd

#_______________________________________________________________________________________________________________________________________________________

#________________________________________________________Liniendiagramm____________________________________________________________________________________
#_______________________________________________________________________________________________________________________________________________________

# Wie viele Flüge gab es im Januar in den 10 größten Flughäfen
# X-Achse 01.01.2015-31.01.15
# Y-Achse zusammengezählter Wert


#----------Fertiges Datenset was in Datensets.py bearbeitet wurde einlesen
df = pd.read_csv("FinaleAbgabe/res/FertigesDatenset.csv")

fluege_pro_airline = df.groupby("AIRLINE")["FLIGHT_NUMBER"].count()
fluggesellschaften_top10 = fluege_pro_airline.nlargest(10).index

datenset_zehn = df[df["AIRLINE"].isin(fluggesellschaften_top10)]