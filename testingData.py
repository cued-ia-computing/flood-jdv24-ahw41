class MonitoringStation:
    """This class represents a river level monitoring station"""

    def __init__(self, station_id, measure_id, label, coord, typical_range,
                 river, town):

        self.station_id = station_id
        self.measure_id = measure_id

        # Handle case of erroneous data where data system returns
        # '[label, label]' rather than 'label'
        self.name = label
        if isinstance(label, list):
            self.name = label[0]

        self.coord = coord
        self.typical_range = typical_range
        self.river = river
        self.town = town

        self.latest_level = None

    def __repr__(self):
        d = "Station name:     {}\n".format(self.name)
        d += "   id:            {}\n".format(self.station_id)
        d += "   measure id:    {}\n".format(self.measure_id)
        d += "   coordinate:    {}\n".format(self.coord)
        d += "   town:          {}\n".format(self.town)
        d += "   river:         {}\n".format(self.river)
        d += "   typical range: {}".format(self.typical_range)
        return d


def getFakeData():
    stations = []

    RoanokeRiver = MonitoringStation(station_id="station_id", measure_id="measure_id", label="Smith Park",
                                     coord=(37.2574, -79.9544), typical_range="typical_range",
                                     river="Roanoke River", town="Roanoke")
    NahuelHuapi = MonitoringStation(station_id="station_id", measure_id="measure_id", label="Mitre",
                                    coord=(-41.1314, -71.2933), typical_range="typical_range",
                                    river="Lago Nahuel Huapi", town="San Carlos de Bariloche")
    JesusLock = MonitoringStation(station_id="station_id", measure_id="measure_id", label="Jesus Lock",
                                  coord=(52.2128, 0.1209), typical_range="typical_range",
                                  river="River Cam", town="Cambridge")
    OrgasmBridge = MonitoringStation(station_id="station_id", measure_id="measure_id", label="Garret Hostel Bridge",
                                     coord=(52.2058, 0.1140), typical_range="typical_range",
                                     river="River Cam", town="Cambridge")
    ByronsPool = MonitoringStation(station_id="station_id", measure_id="measure_id", label="Byron's Pool",
                                   coord=(52.1712, 0.0982), typical_range="typical_range",
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
