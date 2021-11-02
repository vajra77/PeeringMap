from abc import ABCMeta, abstractmethod
from .geo_location import GeoLocation

class GeoLocatable(metaclass=ABCMeta):

    def __init__(self):
        pass

    @property
    @abstractmethod
    def location(self) -> GeoLocation:
        pass