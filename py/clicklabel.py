from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

class ClickLabel(QLabel):
    clicked = pyqtSignal()
    def mouseReleaseEvent(self, QMouseEvent):
        if QMouseEvent.button() == Qt.LeftButton:
            self.clicked.emit()