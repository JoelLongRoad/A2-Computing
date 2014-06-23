import sys

from PyQt4.QtGui import *
from PyQt4.QtCore import *

class MainWindow(QMainWindow):

    #constructor
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Hello World")

        
        #instantiate stacked layout and stacked widget
        self.stacked_layout = QStackedLayout()
        self.stacked_widget = QStackedWidget()

        #call the layouts
        self.create_hello_layout()
        self.create_main_layout()

        #set the first initial layout
        self.stacked_layout.setCurrentIndex(0)

        #set the layout of the stacked widget by passing the stacked_layout into setLayout()
        self.stacked_widget.setLayout(self.stacked_layout)

        #create the central widget
        self.setCentralWidget(self.stacked_widget)

        #add widgets to the stacked layout
        self.stacked_layout.addWidget(self.hello_widget)

    def create_main_layout(self):
        #components
        self.text_box = QLineEdit("Enter your name")
        self.submit_button = QPushButton("Submit")
        #create layout
        self.layout = QVBoxLayout()
        #add widgets to layout
        self.layout.addWidget(self.text_box)
        self.layout.addWidget(self.submit_button)
        #create widget to hold widget
        self.widget = QWidget()
        #add the layout to the widget
        self.widget.setLayout(self.layout)
        #set central widget
        self.setCentralWidget(self.widget)
        #connections
        self.submit_button.clicked.connect(self.switch_layout)
        self.text_box.returnPressed.connect(self.switch_layout)

    def create_hello_layout(self):
        self.label = QLabel()
        self.back_button = QPushButton("Back")

        self.hello_layout = QVBoxLayout()

        self.hello_layout.addWidget(self.label)
        self.hello_layout.addWidget(self.back_button)

        #create widget to hold widgets
        self.hello_widget = QWidget()
        #add the layout to the widget
        self.hello_widget.setLayout(self.hello_layout)

        self.stacked_layout.addWidget(self.hello_widget)
        
        

    def switch_layout(self):
        self.stacked_layout.setCurrentIndex(1)
        name = self.text_box.text()
        self.label.setText("Hello {0}!".format(name))
        

if __name__ == "__main__":
    application = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    window.raise_()
    application.exec_()
