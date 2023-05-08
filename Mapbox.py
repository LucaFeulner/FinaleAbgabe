import plotly.graph_objects as go
import pandas as pd
from urllib.request import urlopen
import json

#_______________________________________________________________________________________________________________________________________________________

#________________________________________________________Mapbox____________________________________________________________________________________
#_______________________________________________________________________________________________________________________________________________________


# Staaten der USA einfärben nach Anzahl der Flügen 
# Filter das Staaten farbig als auch in weiß zu sehen sind
# Die größten 20 Flughäfen auf sder karte markieren und die Anzahl der flüge nach größe und Farbe einzeichnen --> größe wurde wieder nach Anzahl der Flügen bestimmt

df = pd.read_csv("FinaleAbgabe/res/FinalesDatenset.csv")


fluege_pro_flughafen = df.groupby("AIRPORT")["FLIGHT_NUMBER"].count()
flughafen_top20 = fluege_pro_flughafen.nlargest(20).index
groeße= df.groupby("AIRPORT")["FLIGHT_NUMBER"].count().reset_index(name="fluege").sort_values("fluege")

df_20 = df[df["AIRPORT"].isin(flughafen_top20)]
anzahl_fluege_flughafen_top20 = df_20.groupby("AIRPORT")["FLIGHT_NUMBER"].count().reset_index()
#----------Koordinaten einmal pro Flughafen einfügen für x und y auf der Map
standort_flughfanen = pd.merge(groeße, (df_20[["AIRPORT", "ORIGIN_AIRPORT_LAT", "ORIGIN_AIRPORT_LON"]]), left_on="AIRPORT", right_on="AIRPORT", how= "right")
standort_flughfanen = standort_flughfanen

#---------- Die JASON Datei wurde von GIT geladen 
url_staaten = "https://raw.githubusercontent.com/PublicaMundi/MappingAPI/master/data/geojson/us-states.json"
token = 'pk.eyJ1IjoibHVjYWYyMDAyIiwiYSI6ImNsZm1sdmg2bTBkMG8zeG5wbmNkMmRmeXcifQ.6tnXcyV6b870rKIE023_pw'


#----------Jasondaten in die Variable geo_data laden
with urlopen(url_staaten) as response:
    geo_data = json.load(response)

#----------Namen der einzelen Staaten raussuchen um diese dann mit dem Datenset zu verbinden
for feature in geo_data['features']:
    feature['id'] = feature['properties']['name']


fig = go.Figure()

df_staaten_zaehlen  = df.groupby("State").count()

#----------Jasondatei auf die Map bringen
staaten_farbig = go.Choroplethmapbox(
                    geojson = geo_data,
                    locations=  df_staaten_zaehlen.index,
                    z =  df_staaten_zaehlen["FLIGHT_NUMBER"],
                    marker_opacity=0.6,
                    marker_line_width=1,
                    colorscale='GnBu',
                    colorbar= dict(
                                    title = "Anzahl Flüge Staaten",
                                    titleside ="top"
                    )

                    
    )

staaten_weiß = go.Choroplethmapbox(
                    geojson = geo_data,
                    locations=  df_staaten_zaehlen.index,
                    z = df_staaten_zaehlen["FLIGHT_NUMBER"],
                    marker_opacity=0.2,
                    marker_line_width=1,
                    visible=False,
                    colorscale= [[0, '#ffffff'], [0.5, '#ffffff'], [1.0, 'rgb(255, 255, 255)']],
                    showscale = False
                    

                    
    )

flughafen = go.Scattermapbox(
    lat = standort_flughfanen['ORIGIN_AIRPORT_LAT'],
    lon= standort_flughfanen['ORIGIN_AIRPORT_LON'],
    mode= "markers" ,
    marker=go.scattermapbox.Marker(
        size=standort_flughfanen["fluege"]/50,
        color=standort_flughfanen["fluege"],
        sizemode="area",
        showscale=True,
        colorbar = dict(
                        x = -0.2,
                        title = "Anzahl Flüge Flughafen"
        ),
        opacity= 0.7
        ),
    text=df_20['AIRPORT']   
)

fig.add_trace(staaten_farbig)
fig.add_trace(staaten_weiß)
fig.add_trace(flughafen)

fig.update_layout(
                    title = "Anzahl der Flüge nach Staaten(farbig) und Flughäfen",
                    xaxis = dict(
                                title = "Tag"
                                ),
                    mapbox_accesstoken = token,
                    mapbox_style = "light",
                    mapbox_zoom = 2.8,
                    mapbox_center={"lat": 37.090240, "lon": -95.712891}
    )

#----------Dropdownmenu einbauen


fig.update_layout(
    updatemenus = [
        dict(
            active = 0, 
            buttons = list([
                dict(label = "Staaten farbig",
                     method = "update",
                     args = [{"visible": [True, False, True]},
                             {"title": "Anzahl der Flüge nach Staaten(farbig) und den Top 20 Flughäfen"}
                             ]
                    
                        ),
                        

                dict(label = "Staaten ohne Farbe",
                     method = "update",
                     args = [{"visible": [False, True, True]},
                             {"title": "Anzahl der Flüge nach Staaten(SW) und den Top 20 Flughäfen"}
                             ],
                       )
                    
                    ]),
                xanchor = "left",
                x = 0,
                y= 1.05,
                yanchor = "top",
                
             )
        
    ],

    title_x = 0.5
)

fig.update_layout(margin={"r": 70, "t": 70, "l": 70, "b": 70})


#fig.show()