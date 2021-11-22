import requests
from .pdb_object import PDBObject
from .pdb_facility import PDBFacility
from .pdb_ix import PDBIx


class PDBNetwork(PDBObject):

    def __init__(self, asn):
        super().__init__(self._asn_to_id(asn), 'net')
        self._private_facilities = []
        self._ixp_facilities = {}
        self.retrieve()

    @property
    def name(self):
        return self._data['name']

    @property
    def asn(self):
        return self._data['asn']

    @property
    def locations(self):
        all_locations = []
        for pri in self.private_facilities():
            all_locations.append(pri.location)
        return all_locations

    @property
    def ixplocations(self):
        ixp_locations = []
        for ixp in self.ixp_facilities():
            ixp_locations.append(ixp.location)
        return ixp_locations

    def private_facilities(self):
        if len(self._private_facilities) == 0:
            for fac in self._data['netfac_set']:
                facility = PDBFacility(fac['fac_id'])
                self._private_facilities.append(facility)
        return self._private_facilities.copy()

    def ixp_facilities(self):
        if len(self._ixp_facilities) == 0:
            for lan in self._data['netixlan_set']:
                if not lan['ix_id'] in self._ixp_facilities.keys():
                    ix = PDBIx(lan['ix_id'])
                    self._ixp_facilities[ix.id] = ix
        return self._ixp_facilities.values()

    def _retrieve(self):
        url = self.base_url + str(self._id)
        response = requests.get(url)
        json = response.json()
        data = json['data'][0]
        return data

    @staticmethod
    def _asn_to_id(asn):
        url = 'https://peeringdb.com/api/net?asn=' + str(asn)
        response = requests.get(url).json()
        data = response['data'][0]
        return data['id']
