from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys
from math import *

class BubbleCursor:

    defaultCol = Qt.yellow

    def __init__(self, listTargets):
        self.x = 0
        self.y = 0
        self.size = 0
        self.cercleX = 0
        self.cercleY = 0
        self.listTarget = listTargets
        self.closest = None

    def paint(self, qPainter):
        qPainter.setBrush(self.defaultCol)
        #bbox = QRect(QPoint(self.x-(self.size/2), self.y-(self.size/2)), QSize(self.size, self.size))
        bbox = QLine(self.x, self.y, self.cercleX, self.cercleY)
        pen = QPen()
        pen.setWidth(3)
        pen.setBrush(Qt.black)
        qPainter.setPen(pen)
        qPainter.drawLine(bbox)
        #qPainter.drawEllipse(bbox)

    def move(self, x, y):
        self.x = x
        self.y = y
        minDis = 999999

        for target in self.listTarget:
            currDis = sqrt(abs(self.x-(target.x+target.size/2)) * abs(self.x-(target.x+target.size/2)) + abs(self.y-(target.y+target.size/2)) * abs(self.y-(target.y+target.size/2)))
            if(currDis<minDis):
                minDis = currDis
            else:
                target.toSelect = False

        for target in self.listTarget:
            currDis = sqrt(abs(self.x-(target.x+target.size/2)) * abs(self.x-(target.x+target.size/2)) + abs(self.y-(target.y+target.size/2)) * abs(self.y-(target.y+target.size/2)))
            if(currDis == minDis):
                self.closest = target
                self.size = currDis
                self.cercleX = (target.x+target.size/2)
                self.cercleY = (target.y+target.size/2)
                target.toSelect = True
                break;
            else:
                target.toSelect = False
