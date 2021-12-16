import sys 

from PyQt5.QtCore import Qt, QObject, pyqtSignal,QMimeData
from PyQt5.QtGui import QDrag
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

class Element(QWidget):
    def __init__(self):
        super(Element, self).__init__()
        self.elementLayout = QVBoxLayout(self)
        for i in range(5):
            elementLabel = QLabel("element "+str(i))
            elementLabel.setDragEnable(True)
            self.elementLayout.addWidget(elementLabel)

        self.setLayout(self.elementLayout)
        self.resize(400, 201)

class DraggableElement(QLabel):
    def __init__