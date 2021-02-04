from testingData import getFakeData
from floodsystem.geo import stations_by_river


def test_stations_by_river():
    stations = getFakeData()
    assert stations_by_river(stations) == {'Roanoke River': [stations[0]],
                                           'Lago Nahuel Huapi': [stations[1]],
                                           'River Cam': [stations[2], stations[3], stations[4]]}
