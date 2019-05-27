from PyQt4.QtCore import *
from PyQt4.QtGui import *

class AutoGrowDialog(QDialog):
    """this call will ask the user how many days they want to auto grow the crop"""

    #constructor
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Auto Grow Days Selection")

        self.label_one = QLabel("Select the number of days for")
        self.label_two = QLabel("the crop to grow automatically")

        self.label_one.setAlignment(Qt.AlignCenter)
        self.label_two.setAlignment(Qt.AlignCenter)
        
        self.days_spinbox = QSpinBox()

        self.days_spinbox.setRange(1,30)

        self.days_spinbox.setSuffix(" Day(s)")

        self.days_spinbox.setValue(20)

        self.submit_button = QPushButton("Submit")

        self.dialog_layout = QVBoxLayout()
        self.dialog_layout.addWidget(self.label_one)
        self.dialog_layout.addWidget(self.label_two)
        self.dialog_layout.addWidget(self.days_spinbox)
        self.dialog_layout.addWidget(self.submit_button)

        self.setLayout(self.dialog_layout)

        #connection
        self.submit_button.clicked.connect(self.close)
        #self.days_spinbox.returnPressed.connect(self.close)

    def values(self):
        return int(self.days_spinbox.value())
