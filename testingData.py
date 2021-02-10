from floodsystem.station import MonitoringStation


def getFakeData():
    stations = []

    RoanokeRiver = MonitoringStation(station_id="station_id", measure_id="measure_id", label="Smith Park",
                                     coord=(37.2574, -79.9544), typical_range=(1, 2),
                                     river="Roanoke River", town="Roanoke")
    NahuelHuapi = MonitoringStation(station_id="station_id", measure_id="measure_id", label="Mitre",
                                    coord=(-41.1314, -71.2933), typical_range=(2, 3),
                                    river="Lago Nahuel Huapi", town="San Carlos de Bariloche")
    JesusLock = MonitoringStation(station_id="station_id", measure_id="measure_id", label="Jesus Lock",
                                  coord=(52.2128, 0.1209), typical_range=(3, 4),
                                  river="River Cam", town="Cambridge")
    OrgasmBridge = MonitoringStation(station_id="station_id", measure_id="measure_id", label="Garret Hostel Bridge",
                                     coord=(52.2058, 0.1140), typical_range=(5, 4),
                                     river="River Cam", town="Cambridge")
    ByronsPool = MonitoringStation(station_id="station_id", measure_id="measure_id", label="Byron's Pool",
                                   coord=(52.1712, 0.0982), typical_range=(5, 6),
                                   river="River Cam", town="Cambridge")

    stations.append(RoanokeRiver)
    stations.append(NahuelHuapi)
    stations.append(JesusLock)
    stations.append(OrgasmBridge)
    stations.append(ByronsPool)
    return stations


'''
print(stations)

def getFakeData():
    print(stations)
    return stations
print(stations)
print(getFakeData())
print(type(stations))
'''
