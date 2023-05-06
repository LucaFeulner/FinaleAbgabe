
import pandas as pd
import plotly.graph_objects as go


#_______________________________________________________________________________________________________________________________________________________

#________________________________________________________Streudiagramm____________________________________________________________________________________
#_______________________________________________________________________________________________________________________________________________________


# Nur Daten der größten 20 Fluggesellschaften. --> größe wurde nach Anzahl der Flügen bestimmt
# X-Achse Tage im Januar
# Y-Achse Anzahl der Flüge

df = pd.read_csv("FinaleAbgabe/res/FinalesDatenset.csv")

#---------- Subdatensatz erstellen, das nur Daten der größten 20 Fluggesellschaften enthält
anzahl_fluege_fluggesellschaft = df.groupby("AIRPORT")["FLIGHT_NUMBER"].count().reset_index(name = "Anzahl Flüge")
anzahl_fluege_fluggesellschaft = anzahl_fluege_fluggesellschaft.sort_values("Anzahl Flüge", ascending=False)
fluggesellschaften_top20 = anzahl_fluege_fluggesellschaft.head(20)
df_top20 = df[df["AIRPORT"].isin(fluggesellschaften_top20["AIRPORT"].tolist())]

anzahl_top20= df_top20.groupby(["AIRPORT", "DAY"])["FLIGHT_NUMBER"].count().reset_index(name="Anzahl Flüge")

daten = []

for i, flughaefen in enumerate(anzahl_top20["AIRPORT"].unique()):
    speicher = anzahl_top20[anzahl_top20["AIRPORT"]== flughaefen]
    punkt = go.Scatter(
        x = speicher["DAY"],
        y = speicher["Anzahl Flüge"],
        name = flughaefen,
        mode = "markers",
        marker = dict(
            size = speicher["Anzahl Flüge"]/40*2,
            sizemin = 3,
            line = dict(
                    width = 1,
                    color = "DarkSlateGrey"
            )
        )
    )
    daten.append(punkt)

layout = go.Layout(
    title = "Flugzahlen pro Flughafen und pro Tag",
    xaxis = dict(
            title =  "Tage im Januar"
                ),
    yaxis= dict(
            title = "Anzahl der Flüge"
                )
)

fig = go.Figure(data = daten,layout=layout)

fig.show()
