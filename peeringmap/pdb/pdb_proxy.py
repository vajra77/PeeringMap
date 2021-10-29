import requests
import json

from .pdb_network import PDBNetwork
from .pdb_facility import PDBFacility

PDB_URLS = {
    'net': 'https://peeringdb.com/api/net/',
    'fac': 'https://peeringdb.com/api/fac/',
}


class PDBProxy:

    def __init__(self):
        pass

    @classmethod
    def get_network(self, nid) -> PDBNetwork:
        url = PDB_URLS['net'] + str(nid)
        response = requests.get(url)
        net = PDBNetwork.make_from_json(response.json())
        return net

    @classmethod
    def get_facilities(self, net: PDBNetwork) -> list:
        result = []
        base_url = PDB_URLS['fac']
        for fac_id in net.facilities:
            url = base_url + str(fac_id)
            response = requests.get(url)
            fac = PDBFacility.make_from_json(response.json())
            result.append(fac)
        return result





