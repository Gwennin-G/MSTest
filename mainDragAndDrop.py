import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication,
    QHBoxLayout,
    QLabel,
    QMainWindow,
    QPushButton,
    QStackedLayout,
    QVBoxLayout,
    QWidget,
    QDockWidget,
)

from dragAndDrop.element import Element
from dragAndDrop.mouillage import Mouillage

class mainWindowDAD(QMainWindow):
    def __init__(self):
        super(mainWindowDAD, self).__init__()
        self.mouillage = Mouillage()
        self.mouillageDockWidget = QDockWidget()
        self.mouillageDockWidget.setWidget(self.mouillage)
        self.addDockWidget(Qt.LeftDockWidgetArea,
                           self.mouillageDockWidget)

        self.element = Element()
        self.elementDockWidget = QDockWidget()
        self.elementDockWidget.setWidget(self.element)
        self.addDockWidget(Qt.LeftDockWidgetArea,
                           self.elementDockWidget)

app = QApplication(sys.argv)

window = mainWindowDAD()
window.show()

app.exec()