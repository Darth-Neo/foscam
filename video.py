#!/usr/bin/env python
import os
import ConfigParser
from foscam import *
from Logger import *

logger = setupLogging(__name__)
logger.setLevel(INFO)

if __name__ == u"__main__":
    timeFrames = 10.0

    fc = FoscamCamera()

    print(u"playing a little video (10 seconds worth)")
    counter = Counter()
    fc.startVideo(dummy_videoframe_handler, counter)
    time.sleep(timeFrames)

    print
    print(u"stopping video")
    fc.stopVideo()

    nframes = counter.count() - 1

    print(u"%d frames in ~%d secs for ~ %3.2f fps" % (nframes, timeFrames, (nframes / timeFrames)))

    print(u"done!")
