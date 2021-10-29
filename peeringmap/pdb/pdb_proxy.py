import requests
import json

from .pdb_network import PDBNetwork
from .pdb_facility import PDBFacility

PDB_URLS = {
    'asn': 'https://peeringdb.com/api/net?asn=',
    'net': 'https://peeringdb.com/api/net/',
    'fac': 'https://peeringdb.com/api/fac/',
}


class PDBProxy:

    def __init__(self):
        pass

    @classmethod
    def get_network(self, asn) -> PDBNetwork:
        nid = self._get_id_from_asn(asn)
        if nid > 0:
            url = PDB_URLS['net'] + str(nid)
            response = requests.get(url)
            net = PDBNetwork.make_from_json(response.json())
            return net
        else:
            raise ValueError("Unable to resolve ASN")

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

    @staticmethod
    def _get_id_from_asn(asn):
        url = PDB_URLS['asn'] + str(asn)
        response = requests.get(url)
        data = response.json()
        net = data['data'][0]
        return net['id']





