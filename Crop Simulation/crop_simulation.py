import sys

from PyQt4.QtCore import *
from PyQt3.QtGui import *

from radio_button_widget_class import *

class CropWindow(QMainWIndow):
    """this class creates a main window to observe the growth of a simulation"""

    #constructor
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Crop Simulatio")

    def create_select_crop_layout(self):
        self.crop_radio_buttons = RadioButtonWidget("Crop Simulation", "Please select a crop",("Wheat","Potato"))
        self.instatioate_button = QPushButton("Create a crop")

        self.initial_layout = QVBoxLayout()
        self.initial_layout.addWidget(self.crop_radio_buttons)
        self.initial_layout.addWidget(self.instantiate_button)

        self.select_crop_widget = QWidget()
        self.select_crop_idget.setLayout(self.initial_layout)

    

def main():
    crop_simulation = QApplicationnnn(sys.argv)
    crop_window = CropWindow()
    crop_window.show()
    crop_window.raise_()
    crop_simulation.exec()

if __name__ == "__main__":
    main()
