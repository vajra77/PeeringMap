import requests
from .pdb_object import PDBObject


class PDBIxLan(PDBObject):

    def __init__(self, id):
        super().__init__(id, 'ixlan')
        self.retrieve()

    @property
    def prefixes(self):
        result = []
        for pfx in self._data['ixpfx_set']:
            result.append(pfx['prefix'])
        return result

    def _retrieve(self):
        url = self.base_url + str(self._id)
        response = requests.get(url).json()
        data = response['data'][0]
        return data

