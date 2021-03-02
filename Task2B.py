from floodsystem.geo import rivers_by_station_number
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_level_over_threshold

stations = build_station_list()
update_water_levels(stations)
#stations = zip(stations,[x.name for x in stations])
#stations = sorted(stations, key = lambda x: x[1])
#stations = [x[0] for x in stations]
stationLevels = []
for station in stations_level_over_threshold(stations, 0.8):
    stationLevels.append((station[0].name, station[1]))
stationLevels = sorted(stationLevels, key = lambda x: x[1], reverse=True)
for station in stationLevels:
    print(station[0], station[1])