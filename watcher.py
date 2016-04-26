#!/usr/bin/env python
import os
from foscam import *
from Common import *

from Logger import *
logger = setupLogging(__name__)
logger.setLevel(INFO)


if __name__ == u"__main__":

    fc = FoscamCamera()

    print(u"moving up")
    fc.move_a_little(fc, fc.UP, fc.STOP_UP)

    print(u"moving down")
    fc.move_a_little(fc, fc.DOWN, fc.STOP_DOWN)

    print(u"moving left")
    fc.move_a_little(fc, fc.LEFT, fc.STOP_LEFT)

    print(u"moving right")
    fc.move_a_little(fc, fc.RIGHT, fc.STOP_RIGHT)



