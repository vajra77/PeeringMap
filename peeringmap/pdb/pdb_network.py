import requests
import json

class PDBNetwork:

    def __init__(self, id, name, asn, faclist):
        self._id = id
        self._name = name
        self._asn = asn
        self._facilities = faclist

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @property
    def asn(self):
        return self._asn

    @property
    def facilities(self):
        return self._facilities

    @classmethod
    def make_from_json(cls, data):
        obj = data['data'][0]
        id = obj['id']
        name = obj['name']
        asn = obj['asn']
        faclist = []
        for fac in obj['netfac_set']:
            faclist.append(fac['fac_id'])
        return cls(id, name, asn, faclist)

