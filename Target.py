from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys

class Target():
    defaultCol = Qt.blue
    highlightCol = Qt.green
    toSelectCol = Qt.red

    def __init__(self, x, y, size):
        self.x = x
        self.y = y
        self.size = size
        self.toSelect = False
        self.highlighted = False
        #painter = QPainter()
        #painter.setBrush(self.defaultCol)
        #self.paint(painter)

    def paint(self, qPainter):
        if(self.toSelect):
            qPainter.setBrush(self.toSelectCol)

        elif(self.highlighted):
            qPainter.setBrush(self.highlightCol)

        else:
            qPainter.setBrush(self.defaultCol)
        
        bbox = QRect(QPoint(self.x, self.y), QSize(self.size, self.size))
        qPainter.drawEllipse(bbox)
