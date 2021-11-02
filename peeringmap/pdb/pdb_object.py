from abc import ABCMeta, abstractmethod


PDB_URLS = {
    'net': 'https://peeringdb.com/api/net/',
    'fac': 'https://peeringdb.com/api/fac/',
    'ix': 'https://peeringdb.com/api/ix/',
    'ixlan': 'https://peeringdb.com/api/ixlan/'
}

class PDBObject(metaclass=ABCMeta):

    def __init__(self, id, tag):
        self._id = id
        self._tag = tag
        self._retrieved = False
        self._data = {}

    @property
    def id(self):
        return self._id

    @property
    def base_url(self):
        return PDB_URLS[self._tag]

    @property
    def retrieved(self):
        return self._retrieved

    @property
    def data(self):
        return self._data

    def retrieve(self):
        try:
            self._data = self._retrieve()
        except:
            self._retrieved = False
        self._retrieved = True

    @abstractmethod
    def _retrieve(self):
        pass



