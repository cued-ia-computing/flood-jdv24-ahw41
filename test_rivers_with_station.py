from testingData import getFakeData
from floodsystem.geo import rivers_with_station


def test_rivers_with_station():
    stations = getFakeData()
    assert rivers_with_station(stations) == {'River Cam', 'Lago Nahuel Huapi', 'Roanoke River'}
