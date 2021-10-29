

class PDBFacility:

    def __init__(self, id, name, lat, lon):
        self._id = id
        self._name = name
        self._latitude = lat
        self._longitude = lon

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @property
    def longitude(self):
        return self._longitude

    @property
    def latitude(self):
        return self._latitude

    @classmethod
    def make_from_json(cls, data):
        obj = data['data'][0]
        id = obj['id']
        name = obj['name']
        lat = obj['latitude']
        lon = obj['longitude']
        return cls(id, name, lat, lon)