from peeringmap import PDBNetwork


def test_connection():
    net = PDBNetwork(24796)
    assert net.retrieved

def test_facilities():
    net = PDBNetwork(24796)
    assert net.retrieved

    for loc in net.locations:
        print("Location: {} [{}, {}]".format(loc.name, loc.latitude, loc.longitude))