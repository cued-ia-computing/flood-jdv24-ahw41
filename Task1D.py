from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_with_station
from floodsystem.geo import stations_by_river

stations = build_station_list()
riversWithStation = rivers_with_station(stations)
print(len(riversWithStation), "stations. First 10 -", sorted(riversWithStation)[:10])
aire = []
cam = []
thames = []
for station in stations_by_river(stations)["River Aire"]:
    aire.append(station.name)
for station in stations_by_river(stations)["River Cam"]:
    cam.append(station.name)
for station in stations_by_river(stations)["River Thames"]:
    thames.append(station.name)
print(sorted(aire))
print(sorted(cam))
print(sorted(thames))
