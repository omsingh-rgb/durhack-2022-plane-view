import ee
import private
import matplotlib.pyplot as plt
import pydeck as pdk
from pydeck_earthengine_layers import EarthEngineTerrainLayer

def main():
    # Initialize the library.
    try:
        ee.Initialize()
    except:
        ee.Authenticate(auth_mode="notebook")
        ee.Initialize()

    image = ee.Image('USGS/NED').select('elevation')
    terrain = ee.Image('USGS/NED').select('elevation')
    vis_params = {
        "min": 0,
        "max": 4000,
        "palette": ['006633', 'E5FFCC', '662A00', 'D8D8D8', 'F5F5F5'],
    }
    ee_layer = EarthEngineTerrainLayer(image, terrain, vis_params, id="EETerrainLayer")
    view_state = pdk.ViewState(
        latitude=36.15, longitude=-111.96, zoom=10.5, bearing=-66.16, pitch=60
    )

    r = pdk.Deck(layers=[ee_layer], initial_view_state=view_state)

    r.to_html("test.html", open_browser=True)

if __name__=="__main__":
    main()