from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_by_distance

stations = build_station_list()
p = (52.2053,0.1218)

distancedStations = stations_by_distance(stations,p)
stationsTuples = []
for station in distancedStations:
    stationsTuples.append((station[0].name,station[0].town,station[1]))
print(stationsTuples[:10])
print(stationsTuples[-10:])
