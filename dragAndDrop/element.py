import sys 

from PyQt5.QtCore import Qt, QObject, pyqtSignal,QMimeData
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

class Element(QWidget):
    def __init__(self):
        super(Element, self).__init__()
        self.elementLayout = QVBoxLayout(self)
        for i in range(5):
            elementLabel = QLabel("element "+str(i))
            elementLabelDraggable = DraggableLabel(elementLabel,'dragAndDrop\\aquadopp.bmp')
            self.elementLayout.addWidget(elementLabel)

        self.setLayout(self.elementLayout)
        self.resize(400, 201)

class DraggableLabel(QLabel):
    def __init__(self,parent,image):
        super(QLabel,self).__init__(parent)
        self.setPixmap(QPixmap(image))    
        self.show()
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.drag_start_position = event.pos()

    def mouseMoveEvent(self, event):
        if not (event.buttons() & Qt.LeftButton):
            return
        if (event.pos() - self.drag_start_position).manhattanLength() < QApplication.startDragDistance():
            return
        drag = QDrag(self)
        mimedata = QMimeData()
        mimedata.setText(self.text())
        mimedata.setImageData(self.pixmap().toImage())

        drag.setMimeData(mimedata)
        pixmap = QPixmap(self.size())
        painter = QPainter(pixmap)
        painter.drawPixmap(self.rect(), self.grab())
        painter.end()
        drag.setPixmap(pixmap)
        drag.setHotSpot(event.pos())
        drag.exec_(Qt.CopyAction | Qt.MoveAction)

