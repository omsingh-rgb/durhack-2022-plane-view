
from flight_data import get_flight_details
import cesiumpy

def main():
    v = cesiumpy.Viewer()
    v.entities.add(cesiumpy.Box(dimensions=(40e4, 30e4, 50e4), material=cesiumpy.color.RED, position=(-120, 40, 0)))

if __name__=="__main__":
    pass

