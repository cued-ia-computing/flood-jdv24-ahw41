
from floodsystem.geo import haversine


def test_haversine():
    assert round(haversine((52.20753, 0.12182), (-41.13329, -71.30692)), 8) == round(12441.631379247152, 8)
