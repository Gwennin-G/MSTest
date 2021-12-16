import sys 

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QDrag,QPixmap,QPainter,QImage
from PyQt5.QtWidgets import (
    QApplication,
    QHBoxLayout,
    QLabel,
    QMainWindow,
    QPushButton,
    QStackedLayout,
    QVBoxLayout,
    QWidget,
)

from dragAndDrop.facadeTest import Facade
from dragAndDrop.element import DraggableLabel

class Mouillage(QWidget):
    def __init__(self):
        super(Mouillage, self).__init__()
        self.mouillageLayout = QVBoxLayout(self)
        self.mouillageLabel = QLabel("mouillage")
        self.mouillageLayout.addWidget(self.mouillageLabel)
        self.setLayout(self.mouillageLayout)
        self.resize(400, 201)
        self.setAcceptDrops(True)

    """def dragEnterEvent(self,e):
        e.accept()

    def dropEvent(self,e):
        dropLabel = QLabel(e.mimeData().text())
        self.mouillageLayout.addWidget(dropLabel)"""

    def dragEnterEvent(self,event):
        if event.mimeData().hasImage():
            print("event accepted")
            event.accept()
        else:
            print("event rejected")
            event.ignore()
    def dropEvent(self,event):
        if event.mimeData().hasImage():
            dropLabel = QLabel(event.mimeData().text())
            pixmap = QPixmap.fromImage(QImage(event.mimeData().imageData()))
            dropLabel.setPixmap(QPixmap.fromImage(QImage(event.mimeData().imageData())))
            self.mouillageLayout.addWidget(dropLabel)


    
