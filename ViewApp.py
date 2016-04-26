#!/usr/bin/env python
from PyQt4.QtGui import *
from PyQt4.QtCore import *
import sys
from foscam import *

ImageReadyEventId = 1382


class ImageReadyEvent(QEvent):

    def __init__(self, image):
        QEvent.__init__(self, ImageReadyEventId)
        self._image = image

    def image(self):
        return self._image


def videoCallback(frame, userdata=None):
    ire = ImageReadyEvent(frame)
    qApp.postEvent(userdata, ire)


class ViewFoscam(QWidget):

    def __init__(self, qApp, *args, **kw):
        super(ViewFoscam, self).__init__()

        apply(QWidget.__init__, (self,)+args, kw)

        self.fc = FoscamCamera()

        bup = QPushButton('Up', self)
        bdn = QPushButton('Down', self)
        ble = QPushButton('Left', self)
        bri = QPushButton('Right', self)
        play = QPushButton('Play', self)
        stop = QPushButton('Stop', self)

        hbox = QHBoxLayout(self)
        self.setLayout(hbox)

        frame = QWidget(self)
        grid = QGridLayout(frame)
        frame.setLayout(grid)

        grid.addWidget(bup, 0, 1)
        grid.addWidget(bdn, 2, 1)
        grid.addWidget(ble, 1, 0)
        grid.addWidget(bri, 1, 2)
        grid.addWidget(play, 7, 1)
        grid.addWidget(stop, 8, 1)

        hbox.addWidget(frame)

        self.image_label = QLabel('Hello', self)
        self.image_label.resize(640, 480)
        hbox.addWidget(self.image_label)

        buttons = [bup, bdn, ble, bri]
        downs = [self.up, self.down, self.left, self.right]
        for i in range(len(buttons)):
            buttons[i].pressed.connect(downs[i])
            buttons[i].released.connect(self.stop)

        play.clicked.connect(self.playVideo)
        stop.clicked.connect(self.stopVideo)

        qApp.lastWindowClosed.connect(self.stopVideo)

        self.direction = 0

    def up(self):
        self.direction = self.fc.UP
        self.fc.move(self.direction)

    def down(self):
        self.direction = self.fc.DOWN
        self.fc.move(self.direction)

    def left(self):
        self.direction = self.fc.LEFT
        self.fc.move(self.direction)

    def right(self):
        self.direction = self.fc.RIGHT
        self.fc.move(self.direction)

    def stop(self):
        self.fc.move(self.direction + 1)

    def playVideo(self):
        self.fc.startVideo(videoCallback, self)

    def stopVideo(self):
        self.fc.stopVideo()

    def event(self, e):
        if e.type() == ImageReadyEventId:
            data = e.image()
            im = Image.open(StringIO(data))
            self.qim = QImage(im.tostring(), im.size[0], im.size[1], QImage.Format_RGB888)
            self.pm = QPixmap.fromImage(self.qim)
            self.image_label.setPixmap(self.pm)
            self.image_label.update()
            return 1

        return QWidget.event(self, e)


if __name__ == '__main__':

    qApp = QApplication(sys.argv)
    mw = ViewFoscam(qApp)
    mw.resize(720, 480)
    mw.show()
    qApp.exec_()
