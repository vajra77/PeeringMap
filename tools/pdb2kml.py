import sys,getopt
import simplekml
from peeringmap.peeringmap import get_network_facilities


def usage():
    print("Usage: pdb2kml.py -p <peeringdb-id> -f <kml-filename>")

def main():

    try:
        opts, args = getopt.getopt(sys.argv[1:], "p:f:", ["peeringdb-id=","filename="])

    except getopt.GetoptError as err:
        # print help information and exit:
        print(err)  # will print something like "option -a not recognized"
        usage()
        sys.exit(2)

    pdb_id = None
    filename = None

    for o, a in opts:
        if o in ("-p", "--peeringdb-id"):
            pdb_id = int(a)
        elif o in ("-f", "--filename"):
            filename = a
        else:
            assert False, "unhandled option"

    if not (pdb_id and filename):
        print("Error: insufficient arguments", file=sys.stderr)
        usage()
        sys.exit(2)

    facilities = get_network_facilities(pdb_id)
    kml = simplekml.Kml()

    for fac in facilities:
        kml.newpoint(name=fac['name'], coords=[(fac['longitude'], fac['latitude'])])

    kml.save(filename)


if __name__ == "__main__":
    main()