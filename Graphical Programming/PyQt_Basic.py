import sys

from PyQt4.QtGui import *
from PyQt4.QtCore import *

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Hello World")
        self.stacked_layout = QStackedLayout()
        self.stacked_widget = QWidget()
        
        self.stacked_widget.setLayout(self.stacked_layout)

        #call methods
        self.create_main_layout()
        self.create_hello_layout()

        self.setCentralWidget(self.stacked_widget)

        self.stacked_layout.setCurrentIndex(0)
        self.submit_button.setFocus()

    def create_main_layout(self):
        #components
        self.text_box = QLineEdit()
        self.text_box.setPlaceholderText("Enter your name:")
        self.submit_button = QPushButton("Submit")
        #create layout
        self.layout = QVBoxLayout()
        #add widgets to layout
        self.layout.addWidget(self.text_box)
        self.layout.addWidget(self.submit_button)
        #create widget to hold widget
        self.initial_widget = QWidget()
        #add the layout to the widget
        self.initial_widget.setLayout(self.layout)
        #add layout to stacked layout
        self.stacked_layout.addWidget(self.initial_widget)
        #connections
        self.submit_button.clicked.connect(self.next_layout)
        self.text_box.returnPressed.connect(self.next_layout)

    def create_hello_layout(self):
        #components
        self.label = QLabel()
        self.back_button = QPushButton("Back")
        #create layout
        self.hello_layout = QVBoxLayout()
        #add widget to layout
        self.hello_layout.addWidget(self.label)
        self.hello_layout.addWidget(self.back_button)
        #create widget to hold widget
        self.hello_widget = QWidget()
        self.hello_widget.setLayout(self.hello_layout)

        self.stacked_layout.addWidget(self.hello_widget)

        self.back_button.clicked.connect(self.previous_layout)
        

    def next_layout(self):
        self.stacked_layout.setCurrentIndex(1)
        name = self.text_box.text()
        self.label.setText("Hello {0}!".format(name))

    def previous_layout(self):
        self.stacked_layout.setCurrentIndex(0)
        self.text_box.clear()
    

if __name__ == "__main__":
    application = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    window.raise_()
    application.exec_()
