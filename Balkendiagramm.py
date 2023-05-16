import plotly.graph_objects as go
import pandas as pd
#_______________________________________________________________________________________________________________________________________________________

#________________________________________________________Balkendiagramm____________________________________________________________________________________
#_______________________________________________________________________________________________________________________________________________________

# Balkendiagramm durchschnittliche aufgeholte Zeit pro Flug
#X-Achse Kurzstreckenflüge bis <= 1.000, Mittelstrecke >1000 und <= 3000, Langstrecke > 3000.
#Y-Achse durchschnittliche Aufgeholte Zeit pro Flüge in Minuten
#Beim Drüber hovern soll die Airline angezeigt werden und an der Seite gibt es eine legende mit den Farben für kurz und langstrecke

# Fertiges Datenset was in Datensets.py bearbeitet wurde einlesen
df = pd.read_csv("FinaleAbgabe/res/FinalesDatenset.csv")

df["DELAY"] = df["SCHEDULED_TIME"]-df["ELAPSED_TIME"]
durchschn_verspaetung = df.groupby("AIRLINE")["DELAY"].mean()
fluggesellschaften_gruppiert = df["AIRLINE"].unique()

# Festlegen, ab welcher Distanz welche Art von Flug ist
kurzStrecke = df[df["DISTANCE"] <= 1000]
mittelStrecke = df[(df["DISTANCE"] <= 3000) & (df["DISTANCE"] > 1000)]
langStrecke = df[df["DISTANCE"] >3000]

# Berechnen der durchschnittlichen Verspätung pro Flug
kurzStrecke_durchschn_verspaetung = kurzStrecke.groupby("AIRLINE")["DELAY"].mean()
mittelStrecke_durchschn_verspaetung = mittelStrecke.groupby("AIRLINE")["DELAY"].mean()
langStrecke_durchschn_verspaetung = langStrecke.groupby("AIRLINE")["DELAY"].mean()

fig = go.Figure()

# Balken für die Kurzstrecke
balken1 = go.Bar(
    x = fluggesellschaften_gruppiert,
    y = kurzStrecke_durchschn_verspaetung,
    name = "Kurzstrecke",
    marker_color='rgb(118, 204, 122)'
)

# Balken für die Mittelstrecke
balken2 = go.Bar(
    x = fluggesellschaften_gruppiert,
    y = mittelStrecke_durchschn_verspaetung,
    name = "Mittelstrecke",
    marker_color= 'rgb(26, 118, 255)'

)

# Balken für die Langstrecke
balken3 = go.Bar(
    x = fluggesellschaften_gruppiert,
    y = langStrecke_durchschn_verspaetung,
    name = "Langstrecke",
    marker_color='rgb(55, 83, 109)',
    
)

# Style für das Balkendiagramm
layout = go.Layout(
    title = "Aufgeholte Zeit",
    xaxis_tickfont_size=14,
    xaxis_title = "Fluggesellschaften",
    yaxis=dict(
        title='Aufgeholte Zeit in Minuten',
        titlefont_size=16,
        tickfont_size=14,
    ),
    legend=dict(
        x=0,
        y=1.0,
        bgcolor='rgba(255, 255, 255, 0)',
        bordercolor='rgba(255, 255, 255, 0)'
    ),
    barmode='group', 
    bargap = 0.15, # Lücke zwischen den Balken der benachbarten Standortkoordinaten.
    bargroupgap=0.05 # Lücke zwischen Balken derselben Standortkoordinate.

)

fig.add_trace(balken1)
fig.add_trace(balken2)
fig.add_trace(balken3)

fig = go.Figure(data=[balken1,balken2, balken3], layout=layout)

fig.update_layout(
    updatemenus = [
        dict(
            active = 0, 
            buttons = list([
                dict(label = "Alle Flugarten",
                     method = "update",
                     args = [{"visible": [True, True, True]},
                             {"title": "Durchschnittliche aufgeholte Zeit pro Fluggesellschaft"}]),

                dict(label = "Kurzstrecke",
                     method = "update",
                     args = [{"visible": [True, False, False]},
                             {"title": "Durchschnittliche aufgeholte Zeit pro Fluggesellschaft nur Kurzstrecke"}],
                       ),
                dict(label = "Mittelstrecke",
                     method = "update",
                     args = [{"visible": [False, True, False]},
                             {"title": "Durchschnittliche aufgeholte Zeit pro Fluggesellschaft nur Mittelstrecke"}],
                       ),
                dict(label = "Langstrecke",
                     method = "update",
                     args = [{"visible": [False, False, True]},
                             {"title": "Durchschnittliche aufgeholte Zeit pro Fluggesellschaft nur Langstrecke"}],
                       )
        ])
             )
    ],
    title = "Durchschnittliche aufgeholte Zeit pro Fluggesellschaft",
                            xaxis_tickfont_size=14,
                            xaxis_title = "Fluggesellschaften",
                            yaxis=dict(
                                title='aufgeholte Zeit',
                                titlefont_size=16,
                                tickfont_size=14),
                            legend=dict(
                                x=0,
                                y=1.0,
                                bgcolor='rgba(255, 255, 255, 0)',
                                bordercolor='rgba(255, 255, 255, 0)'),
                                barmode='group', 
                                bargap = 0.15, # Lücke zwischen den Balken der benachbarten Standortkoordinaten.
                                bargroupgap=0.05 # Lücke zwischen Balken derselben Standortkoordinate.
)

#fig.show()