from peeringmap import PDBProxy, PDBFacility


def test_connection():
    net = PDBProxy.get_network(4761)
    print(net.name)

def test_facilities():
    net = PDBProxy.get_network(3838)
    facilities = PDBProxy.get_facilities(net)

    for fac in facilities:
        print("FAC: {} [{}, {}]".format(fac.name, fac.latitude, fac.longitude))