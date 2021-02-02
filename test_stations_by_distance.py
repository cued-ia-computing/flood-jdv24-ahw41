from testingData import getFakeData
from floodsystem.geo import stations_by_distance


'''
Tests stations_by_distance on given testingData data (not subject to change).  If this has broken later on,
you likely did something that changed the coordinates of testingData.  Either go back and fix it
or find the new values to put in here.
'''
def test_stations_by_distance():
    stations = getFakeData()
    assert stations_by_distance(stations, (52.2053, 0.1218)) == [(stations[3], round(0.5344202805927869, 8)),
                                                                (stations[2], round(0.8362136220642843, 8)),
                                                                (stations[4], round(4.118936016701786, 8)),
                                                                (stations[0], round(6201.8298217394495, 8)),
                                                                (stations[1], round(12440.59397766243, 8))]
