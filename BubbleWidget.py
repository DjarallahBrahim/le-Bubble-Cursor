from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys

from Target import *
from BubbleCursor import *



class BubbleWidget(QWidget):



    def __init__(self, ):
        super().__init__()
        self.setMouseTracking(True)
        self.targets = []

        f = open("src_tp_bubble.csv")
        for line in f :
            x,y,size = line.split(",")
            self.targets.append(Target(int(x),int(y),int(size)))

        self.cursor = BubbleCursor(self.targets)


    def paintEvent(self, event):
        painter = QPainter(self)
        for target in self.targets:
            target.paint(painter)
        self.cursor.paint(painter)


    def mouseMoveEvent(self,event):
        pos = event.pos()
        self.cursor.move(pos.x(), pos.y())
        self.update()
