import private
import pydeck as pdk
from flight_data import get_flight_details, get_bearing


def showFlight(flight_number:str) -> None:
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


    view_state = pdk.ViewState(latitude=46.24, longitude=-122.18, zoom=11.5, bearing=140, pitch=75)
    view = pdk.View(type="MapView",controller=False)
    r: pdk.Deck = pdk.Deck([terrain_layer], initial_view_state=view_state, views=[view])
    html = r.to_html(as_string = True)

    html = addOverlay(html, 0, 43, 0, 20)
    with open("./node-app/routes/index.html", "w") as file: 
        file.write(html)

    #r.to_html("./node-app/routes/index.html", open_browser=True)
    prev_data = None
    bearing = 0

    
    while True:
        try:
            data = get_flight_details(flight_number)
            if prev_data is None:
                prev_data = data
            l_previous = [float(prev_data["Latitude"]), float(prev_data["Longitude"])]
            l_current = [float(data["Latitude"]), float(data["Longitude"])]
            bearing = get_bearing(l_current[0], l_current[1],l_previous[0], l_previous[1])

        except Exception as e:
            print(f"\t Error: {e}")
            continue
        view_state = pdk.ViewState(
        longitude=float(data["Longitude"]),
        latitude=float(data["Latitude"]),
        zoom=11.5,
        min_zoom=5,
        max_zoom=15,
        pitch=70,
        bearing=bearing)
        r.view_state = view_state
        r = pdk.Deck([terrain_layer], initial_view_state=view_state, views=[view],)
        html = r.to_html(as_string = True)

        html = addOverlay(html, data["Altitude"], data["Longitude"], data["Latitude"], bearing)
        with open("./node-app/routes/index.html", "w") as file: 
            file.write(html)
        #r.to_html("./node-app/routes/index.html", open_browser=False, 


def addOverlay(html, altitude, longitude, latitude, bearing):

    segments = html.split("<body>")

    toadd = f""" 
        <div style= 'position: fixed;
                     width: 100%;
                     height: 100%;
                     top: 0;
                     left: 0;
                     right: 0;
                     bottom: 0;
                     z-index: 2;'> 
            <h1 style='color: white;
                       font-family: courier, monospace'>Longitude : {longitude}</h1>
            <h1 style='color: white;
                       font-family: courier, monospace'>Latitude  : {latitude}</h1>
            <h1 style='color: white;
                       font-family: courier, monospace'>Altitude  : {altitude}</h1>
            <img src='image.png' style='position:absolute;
                                        bottom:30px;
                                        right:30px;
                                        width:100px;
                                        height:120px; 
                                        transform: rotate({-bearing}deg);'>
        
        </div>
    
    """

    segments[1] = toadd + segments[1]
    return '<body>'.join(segments)
