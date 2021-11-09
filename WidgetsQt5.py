import sys
from PyQt5.QtWidgets import (
    QMainWindow, QApplication,
    QLabel, QCheckBox, QComboBox, QLineEdit,QLineEdit, 
    QSpinBox, QDoubleSpinBox, QSlider,QVBoxLayout,QWidget
)
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("My App")
        layout = QVBoxLayout()

        label = QLabel("Hello")
        font = label.font()
        font.setPointSize(30)
        label.setFont(font)
        label.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)

        checkBox = QCheckBox() 
        checkBox.setText("check")
        checkBox.setCheckState(Qt.Checked)
        checkBox.stateChanged.connect(self.show_state)

        comboBox = QComboBox()
        comboBox.addItems(["One","Two","Three"])
        comboBox.currentIndexChanged.connect( self.index_changed )
        comboBox.currentTextChanged.connect( self.text_changed )

        layout.addWidget(label)
        layout.addWidget(checkBox)
        layout.addWidget(comboBox)

        widget = QWidget()
        widget.setLayout(layout)

        self.setCentralWidget(widget)

    def show_state(self, s):
        print(s == Qt.Checked)
        print(s)

    def index_changed(self, i): # i is an int
        print(i)

    def text_changed(self, s): # s is a str
        print(s)

app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec()