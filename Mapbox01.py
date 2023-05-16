import plotly.graph_objects as go
import pandas as pd
from urllib.request import urlopen
import json





#---------- Die JASON Datei wurde von GIT geladen 
url_staaten = "https://raw.githubusercontent.com/PublicaMundi/MappingAPI/master/data/geojson/us-states.json"
token = 'pk.eyJ1IjoibHVjYWYyMDAyIiwiYSI6ImNsZm1sdmg2bTBkMG8zeG5wbmNkMmRmeXcifQ.6tnXcyV6b870rKIE023_pw'



#----------Jasondaten in die Variable geo_data laden
with urlopen(url_staaten) as response:
    geo_data = json.load(response)

#----------Namen der einzelen Staaten raussuchen um diese dann mit dem Datenset zu verbinden
for feature in geo_data['features']:
    feature['id'] = feature['properties']['name']


df = pd.read_csv("FinaleAbgabe/res/FinalesDatenset.csv")
flughafen_top15 = df.groupby("AIRPORT")["FLIGHT_NUMBER"].count()
flughafen_top15 = flughafen_top15.nlargest(15).index
df_top15 = df[df["AIRPORT"].isin(flughafen_top15)]
standort_flughafen = df_top15.drop_duplicates(subset="AIRPORT", keep="first", inplace=False, ignore_index=False)
standort_flughafen = df_top15[["AIRPORT", "ORIGIN_AIRPORT_LAT", "ORIGIN_AIRPORT_LON"]]

flugroute = df.groupby(["ORIGIN_AIRPORT", "DESTINATION_AIRPORT", "ORIGIN_AIRPORT_LAT", "ORIGIN_AIRPORT_LON", "DESTINATION_AIRPORT_LAT", "DESTINATION_AIRPORT_LON"])["FLIGHT_NUMBER"].count().reset_index(name="Flugroute").drop_duplicates(subset=["Flugroute"])
flugroute_top10 = flugroute.nlargest(15, "Flugroute")



fig = go.Figure()

df_staaten_zaehlen  = df.groupby("State").count()

#----------Jasondatei auf die Map bringen


staaten_weiß = go.Choroplethmapbox(
                    geojson = geo_data,
                    locations=  df_staaten_zaehlen.index,
                    z = df_staaten_zaehlen["FLIGHT_NUMBER"],
                    marker_opacity=0.2,
                    marker_line_width=1,
                    visible=False,
                    colorscale= [[0, '#ffffff'], [0.5, '#ffffff'], [1.0, 'rgb(255, 255, 255)']],
                    showscale = True
                     )

route = flugroute_top10
# print(route)
# for i in range(10):
#     test = route.iloc[i]
#     lat = test["DESTINATION_AIRPORT_LAT"]
#     long = test["DESTINATION_AIRPORT_LON"]
#     print("LAT:" + str(lat) + " LONG:" + str(long))
    
for i in range(15):
    test = route.iloc[i]
    fig.add_trace(go.Scattermapbox(
        mode = "markers+lines",
        lat = [test["ORIGIN_AIRPORT_LAT"], test["DESTINATION_AIRPORT_LAT"]],
        lon = [test["ORIGIN_AIRPORT_LON"], test["DESTINATION_AIRPORT_LON"]],
        marker = {"size": 10},
        name = (test["ORIGIN_AIRPORT"] + "-->" + test["DESTINATION_AIRPORT"])


    ))





    



fig.add_trace(staaten_weiß)



fig.update_layout(
                    title = "Top 15 Flugrouten",
                    xaxis = dict(
                                title = "Tag"
                                ),
                    mapbox_accesstoken = token,
                    mapbox_style = "light",
                    mapbox_zoom = 2.8,
                    mapbox_center={"lat": 37.090240, "lon": -95.712891}
    )



fig.update_layout(margin={"r": 70, "t": 70, "l": 70, "b": 70})


#fig.show()