import sys
import time

with open("executed_{}.txt".format(time.time()), "w+") as file:
    file.write("argv len: {}\n\n".format(len(sys.argv)))
    file.write("\n".join(sys.argv))
