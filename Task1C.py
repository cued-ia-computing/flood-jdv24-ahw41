from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_within_radius
stations = build_station_list()
closeStations = stations_within_radius(stations, (52.2053, 0.1218), 10)
names = []
for station in closeStations:
    names.append(station.name)
print(sorted(names))
