from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_within_radius


def run():
    stations = build_station_list()
    closeStations = stations_within_radius(stations, (52.2053, 0.1218), 10)
    names = []
    for station in closeStations:
        names.append(station.name)
    print(sorted(names))


if __name__ == "__main__":
    print("*** Task 1C: CUED Part IA Flood Warning System ***")
    run()
