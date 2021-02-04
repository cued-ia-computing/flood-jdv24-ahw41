from testingData import getFakeData
from floodsystem.geo import stations_within_radius


def test_stations_within_radius():
    stations = getFakeData()
    assert stations_within_radius(stations, (52.2053, 0.1218), 10) == [stations[2], stations[3], stations[4]]
