#!/usr/bin/env python
import os
from foscam import *

from Logger import *
logger = setupLogging(__name__)
logger.setLevel(INFO)


if __name__ == u"__main__":

    fc = FoscamCamera()

    print(u"\ntaking a few snapshots")
    for i in xrange(1, 3):
        data = fc.snapshot()

        with open("./snapshots/snapshot-%02d.jpg" % i, "wb") as f:
            f.write(data)
            sys.stdout.write("wrote snapshot %d%s" % (i, os.linesep))
            sys.stdout.flush()
