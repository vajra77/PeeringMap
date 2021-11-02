import requests
from .geo_location import GeoLocation


class GeoIpHelper:

    def __init__(self):
        pass

    @classmethod
    def locate(cls, name, prefix) -> GeoLocation:
        url = 'https://ipmap.ripe.net/api/v1/locate/' + prefix[:-3]
        try:
            response = requests.get(url).json()
            obj = response['locations'][0]
            lat = obj['latitude']
            lon = obj['longitude']
        except Exception as e:
            return GeoLocation.make_invalid(name)
        else:
            if (lat and lon):
                return GeoLocation(name, lat, lon)
            else:
                return GeoLocation.make_invalid(name)