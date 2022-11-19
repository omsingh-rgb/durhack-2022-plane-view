import os
from time import sleep
import ee
import private
import pydeck as pdk
from pydeck_earthengine_layers import EarthEngineTerrainLayer, EarthEngineLayer
from flight_data import get_flight_details

def main(flight_number:str) -> None:
    # Initialize the library.
    # try:
    #     ee.Initialize()
    # except:
    #     ee.Authenticate(auth_mode="notebook")
    #     ee.Initialize()


    MAPBOX_API_KEY = private.KEY

    # AWS Open Data Terrain Tiles
    TERRAIN_IMAGE = "https://s3.amazonaws.com/elevation-tiles-prod/terrarium/{z}/{x}/{y}.png"

    # Define how to parse elevation tiles
    ELEVATION_DECODER = {"rScaler": 256, "gScaler": 1, "bScaler": 1 / 256, "offset": -32768}

    SURFACE_IMAGE = f"https://api.mapbox.com/v4/mapbox.satellite/{{z}}/{{x}}/{{y}}@2x.png?access_token={MAPBOX_API_KEY}"

    terrain_layer = pdk.Layer(
        "TerrainLayer", elevation_decoder=ELEVATION_DECODER, texture=SURFACE_IMAGE, elevation_data=TERRAIN_IMAGE
    )


    view_state = pdk.ViewState(latitude=46.24, longitude=-122.18, zoom=11.5, bearing=140, pitch=60)
    view = pdk.View(type="MapView",controller=False)
    r: pdk.Deck = pdk.Deck([terrain_layer], initial_view_state=view_state, views=[view])
    r.to_html("test.html", open_browser=True)
    while True:
        try:
            data = get_flight_details(flight_number)
        except Exception as e:
            print(f"\t Error: {e}")
            continue
        view_state = pdk.ViewState(
        longitude=float(data["Longitude"]),
        latitude=float(data["Latitude"]),
        zoom=11.5,
        min_zoom=5,
        max_zoom=15,
        pitch=40.5,
        bearing=-27.36)
        r.view_state = view_state
        r = pdk.Deck([terrain_layer], initial_view_state=view_state, views=[view])
        r.to_html("test.html", open_browser=False, )

if __name__=="__main__":
    main("X32263")