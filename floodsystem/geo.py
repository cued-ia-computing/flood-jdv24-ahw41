# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from .utils import sorted_by_key  # noqa

# 2/2/2021 implementing distance function


def haversine(coord1: object, coord2: object):
    # Spherical distance function
    import math

    # Coordinates in decimal degrees (e.g. 2.89078, 12.79797)
    lat1, lon1 = coord1
    lat2, lon2 = coord2

    R = 6371000  # radius of Earth in meters
    phi_1 = math.radians(lat1)
    phi_2 = math.radians(lat2)

    delta_phi = math.radians(lat2 - lat1)
    delta_lambda = math.radians(lon2 - lon1)

    a = math.sin(delta_phi / 2.0) ** 2 + math.cos(phi_1) * math.cos(phi_2) * math.sin(delta_lambda / 2.0) ** 2

    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    meters = R * c  # output distance in meters
    km = meters / 1000.0  # output distance in kilometers

    return km


def stations_by_distance(stations, p):
    # returns stations by distancee and their distance as a list
    distanceList = []
    # stations is a list of MonitoringStation objects and p a tuple of floats for the coordinate p
    for station in stations:
        distanceList.append((station, round(haversine(p, station.coord), 8)))
    return(sorted_by_key(distanceList, 1))


def stations_within_radius(stations, centre, r):
    # List of stations within a given radius of a point
    stationList = []
    for station in stations:
        if haversine(station.coord, centre) < r:
            stationList.append(station)
    return(stationList)


def rivers_with_station(stations):
    # A function that returns rivers with stations
    rivers = set()
    for station in stations:
        rivers.add(station.river)
    return(rivers)


def stations_by_river(stations):
    # Returns river dictionary
    riverDict = {}
    for station in stations:
        if station.river not in riverDict:
            riverDict[station.river] = []
        riverDict[station.river].append(station)
    return(riverDict)


def rivers_by_station_number(stations, N):
    # Given stations and N, returns a tuple of N rivers and their number of stations
    riverStations = stations_by_river(stations)
    riverCounts = []
    for river in rivers_with_station(stations):
        riverCounts.append((len(riverStations[river]), river))
    return [(x[1], x[0]) for x in sorted(riverCounts, reverse=True)[:N]]
