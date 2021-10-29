# PeeringMap

A simple package to query PeeringDB for Network/Facility geographical information

## Package functions

Package `peeringmap.peeringmap` provides the following functions:

- `get_network_facilities(asn)`: returns a list of facilities (points of presence) for the network operator identified by `asn` AS number. Results are given in the form of a Python dict: `{ 'name': , 'latitude': , 'longitude': }`

## Available tools
In the `tools/` directory you will find some useful tools to deal with IRR resources:

- **pdb2kml.py**: produces a KML file of Points of Presence (facilities) for the given AS number. Usage: `pdb2kml.py -a <as number> -f <kml-filename>`

## Setup

### Requirements
This tools requires Python 3.8 and the following packages:

- [simplekml](https://simplekml.readthedocs.io/en/latest/)

### Install
From the root directory:

`pip install -e .` 

