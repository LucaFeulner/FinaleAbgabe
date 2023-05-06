import plotly.graph_objects as go
import pandas as pd

#_______________________________________________________________________________________________________________________________________________________

#________________________________________________________Liniendiagramm____________________________________________________________________________________
#_______________________________________________________________________________________________________________________________________________________

# Wie viele Flüge gab es im Januar in den 10 größten Flughäfen
# X-Achse 01.01.2015-31.01.15
# Y-Achse zusammengezählter Wert


#----------Fertiges Datenset was in Datensets.py bearbeitet wurde einlesen
df = pd.read_csv("FinaleAbgabe/res/FinalesDatenset.csv")

fluege_pro_airline = df.groupby("AIRLINE")["FLIGHT_NUMBER"].count()
fluggesellschaften_top10 = fluege_pro_airline.nlargest(10).index

df_top10 = df[df["AIRLINE"].isin(fluggesellschaften_top10)]
#----------Aus den Zeilen DAY die einstellig sind mit 0 ergänzen, dann Zeilen(DAY; MONTH, YEAR) zusammenfügen zu Datum
df_top10['DAY'] = df_top10['DAY'].map(str).apply(lambda x: x.zfill(2))
df_top10["DATUM"]=df_top10["DAY"].map(str) + "-" + df_top10["MONTH"].map(str)+"-" + df_top10["YEAR"].map(str)


farben = ["#143d59", "#e71989", "#b8df10", "#f6b60d", "#5e057e", "#a2eacb", "#761137", "#514644", "#0f4d19", "#104c91"]
farben_zaehler = 0


fig = go.Figure()

#----------Zählen, wie viele Flüge es pro Tag je Fluggesellschaft gab
anzahl_fluege_fluggesellschaften = df_top10.sort_values(by="DAY").groupby(["AIRLINE", "DATUM"])["FLIGHT_NUMBER"].count().reset_index()

for fluggesellschaft in anzahl_fluege_fluggesellschaften["AIRLINE"].unique():
    fig.add_trace(go.Scatter(
                            x = anzahl_fluege_fluggesellschaften[anzahl_fluege_fluggesellschaften["AIRLINE"] == fluggesellschaft ]["DATUM"],
                            y =anzahl_fluege_fluggesellschaften[anzahl_fluege_fluggesellschaften["AIRLINE"] == fluggesellschaft]["FLIGHT_NUMBER"],
                            name = fluggesellschaft,
                            line_color = farben[farben_zaehler]

                            
                            )
                )
    farben_zaehler = farben_zaehler +  1

fig.update_layout(  title="Anzahl der Flüge pro Tag der zehn größten Flughäfen im Januar 2015",
                    xaxis = dict(
                                tickvals = anzahl_fluege_fluggesellschaften['DATUM'].unique(),
                                gridcolor = "lightgray",
                                title = "Tage im Januar",
                                ),
                    yaxis = dict( 
                                title = "Anzahl der Flüge",
                                gridcolor = "lightgray"
                                ),
                    plot_bgcolor = "white"
                    )

#fig.show()