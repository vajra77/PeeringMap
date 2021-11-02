

_LAT_INVALID = _LON_INVALID = -1

class GeoLocation:

    def __init__(self, name, lat, lon):
        self._name = name
        self._latitude = lat
        self._longitude = lon

    @property
    def name(self):
        return self._name

    @property
    def is_valid(self):
        if (self._latitude and self._longitude):
            return (self._latitude != _LAT_INVALID and self._longitude != _LON_INVALID)
        else:
            return False

    @property
    def latitude(self):
        return self._latitude

    @property
    def longitude(self):
        return self._longitude

    @classmethod
    def make_invalid(cls,name):
        return cls(name, _LAT_INVALID, _LON_INVALID)

