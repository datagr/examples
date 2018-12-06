#!/usr/bin/env python
import sys
import os

from ecl.eclfile import EclFile

from res.enkf import RunpathList


def calc_volume(basename):
    init = EclFile("{}.INIT".format(basename))
    porv_kw = init["PORV"][0]
    return porv_kw.sum()


runpath_list = RunpathList(sys.argv[1])
runpath_list.load()

volume_list = []
for node in runpath_list:
    volume = calc_volume( os.path.join(node.runpath, node.basename) )
    volume_list.append((node.realization, volume))


print("Realization :     Volume")
print("------------------------")
for iens,volume in volume_list:
    print("        {:3d} : {:10}".format(iens, volume))
print("------------------------")
