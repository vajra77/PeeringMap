import requests
from .pdb_object import PDBObject
from peeringmap.geoip import GeoLocation, GeoLocatable


class PDBFacility(PDBObject, GeoLocatable):

    def __init__(self, id):
        super().__init__(id, 'fac')
        self.retrieve()

    @property
    def location(self):
        loc = GeoLocation(
            self._data['name'],
            self._data['latitude'],
            self._data['longitude']
        )
        return loc

    @property
    def name(self):
        return self._data['name']

    def _retrieve(self):
        url = self.base_url + str(self._id)
        response = requests.get(url)
        json = response.json()
        data = json['data'][0]
        return data