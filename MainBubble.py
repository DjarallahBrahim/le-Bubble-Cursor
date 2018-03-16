from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys
from BubbleWidget import *

    
def main(argv):
        print("Fonction main")
        print(argv)

        app = QApplication(argv)
        mWindow = QMainWindow()
        mBubbleWidget = BubbleWidget()
        mWindow.setCentralWidget(mBubbleWidget)
        mWindow.resize(1024,800)
        mWindow.show()
        app.exec_()


if __name__ == "__main__":
	main(sys.argv)
