#!/usr/bin/env python
import argparse
from input import processInputFile


parser = argparse.ArgumentParser()
parser.add_argument("inputfile")
args = parser.parse_args()
fleet, rides = processInputFile(args.inputfile)

print('Fleet:', fleet)
print('Rides:', rides)
