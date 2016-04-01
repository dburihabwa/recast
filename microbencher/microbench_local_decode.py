#! /usr/bin/env python
""" A script that decodes 1000 times a piece of data """
import os
import sys
import time

from pyeclib.ec_iface import ECDriver

from custom_drivers import ECStripingDriver
from custom_drivers import PylonghairDriver

def print_usage():
    """Prints the usage message"""
    print "Usage:", sys.argv[0], " size"
    print ""
    print "Benchmark pyeclib erasure coding libraries"
    print ""
    print "Arguments:"
    print "\tsize       Size of the payload to decode in bytes"

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print_usage()
        sys.exit(0)
    SIZE = int(sys.argv[1])
    DATA = os.urandom(SIZE)
    REQUESTS = 1000

    # Load driver
    EC_K = int(os.environ.get("EC_K", 10))
    EC_M = int(os.environ.get("EC_M", 4))
    EC_TYPE = os.environ.get("EC_TYPE", "liberasure_rs_vand")
    DRIVER = None
    if EC_TYPE == "pylonghair":
        DRIVER = PylonghairDriver(k=EC_K, m=EC_M, ec_type=EC_TYPE)
    elif EC_TYPE == "striping":
        DRIVER = ECStripingDriver(k=EC_K, m=0, hd=None)
    else:
        DRIVER = ECDriver(k=EC_K, m=EC_M, ec_type=EC_TYPE)

    # Start benchmark
    print "About to decode ", REQUESTS, " payloads of size ", SIZE, " bytes (",\
    (DRIVER.ec_type if hasattr(DRIVER, "ec_type") else EC_TYPE), ", k =", DRIVER.k, \
    ", m =", DRIVER.m, ")"
    ENCODED = DRIVER.encode(DATA)
    for i in range(REQUESTS):
        start = time.clock()
        DRIVER.decode(ENCODED)
        end = time.clock()
        elasped = (end - start) * 1000
        print elasped
