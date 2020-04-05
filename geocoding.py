import googlemaps
import pandas as pd
from datetime import datetime

df = pd.read_csv("CSVPath")

gmaps = googlemaps.Client(key='Google Maps API Key')

df["LAT"] = None
df["LNG"] = None
df["PIN"] = None

for i in range(len(df)):
    geocode_result = gmaps.geocode(df.iat[i, 0])
    try:
        lat = geocode_result[0]["geometry"]["location"]["lat"]
        lng = geocode_result[0]["geometry"]["location"]["lng"]
        formatted_address = geocode_result[0]["formatted_address"]
        print(lat, lng, formatted_address)
        df.iat[i, df.columns.get_loc("LAT")] = lat
        df.iat[i, df.columns.get_loc("LNG")] = lng
        df.iat[i, df.columns.get_loc("PIN")] = formatted_address
        #temp = {'Latitude': lat, 'Longitude': lng, 'Address': formatted_address}
        #df = pd.DataFrame(temp)
        #df.to_csv(r'TestPath', index=False)
    except:
        lat = None
        lng = None
        formatted_address = None