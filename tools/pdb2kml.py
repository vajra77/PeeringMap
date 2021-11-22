import sys,getopt
import simplekml
from peeringmap.peeringmap import get_network_facilities, get_ixp_facilities


def usage():
    print("Usage: pdb2kml.py -a <as number> -f <kml-filename>")

def main():

    try:
        opts, args = getopt.getopt(sys.argv[1:], "a:f:", ["asn=", "filename="])

    except getopt.GetoptError as err:
        # print help information and exit:
        print(err)  # will print something like "option -a not recognized"
        usage()
        sys.exit(2)

    asn = None
    filename = None

    for o, a in opts:
        if o in ("-a", "--asn"):
            asn = a
        elif o in ("-f", "--filename"):
            filename = a
        else:
            assert False, "unhandled option"

    if not (asn and filename):
        print("Error: insufficient arguments", file=sys.stderr)
        usage()
        sys.exit(2)

    facilities = get_network_facilities(asn)
    ixpfacilities = get_ixp_facilities(asn)
    kml = simplekml.Kml()

    for fac in facilities:
        print (fac)
        pnt = kml.newpoint(name=fac['name'], coords=[(fac['longitude'], fac['latitude'])])
        pnt.style.iconstyle.color = simplekml.Color.red

    for ixpfac in ixpfacilities:
        print (ixpfac)
        pnt = kml.newpoint(name=ixpfac['name'], coords=[(ixpfac['longitude'], ixpfac['latitude'])])
        pnt.style.iconstyle.color = simplekml.Color.blue

    kml.save(filename)


if __name__ == "__main__":
    main()
