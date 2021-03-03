def stations_level_over_threshold(stations, tol):
    risky_stations = []
    for station in stations:
        if station.relative_water_level() is not None:
            if station.relative_water_level() > tol:
                risky_stations.append((station, station.relative_water_level()))
    return risky_stations


def stations_highest_rel_level(stations, N):
    # First, remove all stations with NoneType problems
    solidStations = []
    for station in stations:
        if station.relative_water_level() is not None:
            solidStations.append(station)
    stations = solidStations
    # Then, sort properly and return highest N
    sortedPairs = sorted([(station.relative_water_level(), station) for station in stations],
                         key=lambda x: x[0], reverse=True)
    stations = [station[1] for station in sortedPairs]
    return stations[:N]
