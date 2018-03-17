from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys
import time
from math import *

class BubbleCursor:

    defaultCol = Qt.yellow

    def __init__(self, listTargets):
        self.x = 0
        self.y = 0
        self.size = 0
        self.cercleCenterX = 0
        self.cercleCenterY = 0
        self.cercleX = 0
        self.cercleY = 0
        self.cercleSize = 0
        self.listTarget = listTargets
        self.closest = None

    def paint(self, qPainter):
        qPainter.setBrush(self.defaultCol)
        pen = QPen()
        #bbox = QRect(QPoint(self.x-(self.size/2), self.y-(self.size/2)), QSize(self.size, self.size))


        bbox = QRect(QPoint(self.cercleCenterX-((self.cercleSize*3)/2), self.cercleCenterY-((self.cercleSize*3)/2)), QSize(self.cercleSize, self.cercleSize)*3)
        pen.setWidth(0)
        pen.setBrush(QColor(0, 0, 0))
        qPainter.setPen(pen)
        qPainter.setBrush(QColor("#e6005c"))
        qPainter.drawEllipse(bbox)

        #bbox = QRect(QPoint(self.cercleCenterX-((self.cercleSize*2.2)/2), self.cercleCenterY-((self.cercleSize*2.2)/2)), QSize(self.cercleSize, self.cercleSize)*2.2)
        #qPainter.setBrush(QColor(102, 153, 153, 100))
        #qPainter.drawEllipse(bbox)

        bbox = QLine(self.x, self.y, self.cercleCenterX, self.cercleCenterY)
        pen.setWidth(2)
        pen.setBrush(QColor("#669999"))
        qPainter.setPen(pen)
        qPainter.drawLine(bbox)

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
                self.cercleCenterX = (target.x+target.size/2)
                self.cercleCenterY = (target.y+target.size/2)
                self.cercleX = (target.x)
                self.cercleY = (target.y)
                self.cercleSize = target.size
                target.toSelect = True
                break;
            else:
                target.toSelect = False
