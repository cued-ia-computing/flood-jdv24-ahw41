from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_with_station
from floodsystem.geo import stations_by_river


def run():
    stations = build_station_list()
    riversWithStation = rivers_with_station(stations)
    print(len(riversWithStation), "stations. First 10 -", sorted(riversWithStation)[:10])

    for river in ["River Aire", "River Cam", "River Thames"]:
        arr = []
        for station in stations_by_river(stations)[river]:
            arr.append(station.name)
        print(sorted(arr))


if __name__ == "__main__":
    print("*** Task 1D: CUED Part IA Flood Warning System ***")
    run()
