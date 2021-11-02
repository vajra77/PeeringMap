import requests
from .pdb_object import PDBObject
from .pdb_ixlan import PDBIxLan
from peeringmap.geoip import GeoLocatable, GeoLocation, GeoIpHelper


class PDBIx(PDBObject, GeoLocatable):

    def __init__(self, id):
        super().__init__(id, 'ix')
        self.retrieve()

    @property
    def name(self):
        return self._data['name']

    @property
    def location(self) -> GeoLocation:
        for xl in self._data['ixlan_set']:
            ixlan = PDBIxLan(xl['id'])
            for pfx in ixlan.prefixes:
                location = GeoIpHelper.locate(self.name, pfx)
                if location.is_valid:
                    return location
        return GeoLocation.make_invalid(self.name)

    def _retrieve(self):
        url = self.base_url + str(self._id)
        response = requests.get(url).json()
        data = response['data'][0]
        return data