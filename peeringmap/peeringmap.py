from .pdb import PDBProxy, PDBNetwork, PDBFacility


def get_network_facilities(net_id):
    network = PDBProxy.get_network(net_id)
    facilities = PDBProxy.get_facilities(network)
    result = []
    for fac in facilities:
        result.append({
           'name': fac.name,
           'latitude': fac.latitude,
           'longitude': fac.longitude
        })
    return result

