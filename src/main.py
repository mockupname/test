import sys
import time
from version import __version__

with open("executed_{}.txt".format(time.time()), "w+") as file:
    file.write("version: {}\n".format(__version__))
    file.write("argv len: {}\n\n".format(len(sys.argv)))
    file.write("\n".join(sys.argv))
