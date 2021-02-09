from testingData import getFakeData
from floodsystem.geo import rivers_by_station_number


def test_rivers_by_station_number():
    arr = [('River Cam', 3), ('Roanoke River', 1), ('Lago Nahuel Huapi', 1)]
    assert rivers_by_station_number(getFakeData(), 4) == arr
