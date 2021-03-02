def stations_level_over_threshold(stations, tol):
    risky_stations = []
    for station in stations:
        if station.relative_water_level() is not None:
            if station.relative_water_level() > tol:
                risky_stations.append((station, station.relative_water_level()))
    return risky_stations
