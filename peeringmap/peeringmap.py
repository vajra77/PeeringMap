from .pdb import PDBNetwork, PDBFacility


def get_network_facilities(asn):
     net = PDBNetwork(asn)
     result = []
     for loc in net.locations:
         if loc.is_valid:
            result.append({
                'name': loc.name,
                'latitude': loc.latitude,
                'longitude': loc.longitude
            })
     return result

