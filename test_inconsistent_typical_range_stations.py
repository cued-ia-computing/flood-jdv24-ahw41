from floodsystem.station import inconsistent_typical_range_stations
from testingData import getFakeData


def test_inconsistent_typical_range_stations():
    stations = getFakeData()
    assert inconsistent_typical_range_stations(stations) == ['Garret Hostel Bridge']
