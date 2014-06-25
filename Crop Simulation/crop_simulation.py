import sys

from PyQt4.QtCore import *
from PyQt4.QtGui import *

from radio_button_widget_class import *
from wheat_class import *
from potato_class import *

class CropWindow(QMainWindow):
    """this class creates a main window to observe the growth of a simulation"""

    #constructor
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Crop Simulation")#set window title
        self.create_select_crop_layout()
               
        #create stacked layout/widget
        self.stacked_layout = QStackedLayout()
        self.stacked_layout.addWidget(self.select_crop_widget)

        #assign stacked layout to stacked widget
        self.central_widget = QWidget()
        self.central_widget.setLayout(self.stacked_layout)

        #create the central widget to hold the layouts 
        self.setCentralWidget(self.central_widget)

##        #call methods
##        self.create_select_crop_layout()
##        self.create_view_crop_layout()
##
##
##        #set the starting layout to create_select_crop_layout method
##        self.stacked_layout.setCurrentIndex(0)


    def create_select_crop_layout(self):
        #this is the initial layout of the window - to select the crop type
        self.crop_radio_buttons = RadioButtonWidget("Crop Simulation", "Please select a crop",("Wheat","Potato"))
        self.instantiate_button = QPushButton("Create a crop")

        #create layouit to hold the widgets
        self.initial_layout = QVBoxLayout()
        self.initial_layout.addWidget(self.crop_radio_buttons)
        self.initial_layout.addWidget(self.instantiate_button)

        self.select_crop_widget = QWidget()
        self.select_crop_widget.setLayout(self.initial_layout)

        #add connection
        self.instantiate_button.clicked.connect(self.instantiate_crop)

    def create_view_crop_layout(self,crop_type):
        #this is the second layer of the window - view the crop growth

        self.growth_label = QLabel("Growth")
        self.days_label = QLabel("Days Growing")
        self.status_label = QLabel("Crop Status")

        self.growth_line_edit = QLineEdit()
        self.days_line_edit = QLineEdit()
        self.status_line_edit = QLineEdit()

        self.manual_grow_button = QPushButton("Manually Grow")
        self.auto_grow_button = QPushButton("Automatically Grow")

        self.grow_grid = QGridLayout()
        self.status_grid = QGridLayout()

        #add label widget to status layout
        self.status_grid.addWidget(self.growth_label,0,0)
        self.status_grid.addWidget(self.days_label,1,0)
        self.status_grid.addWidget(self.status_label,2,0)

        #add line edit widgets to status layout
        self.status_grid.addWidget(self.growth_line_edit,0,1)
        self.status_grid.addWidget(self.days_line_edit,1,1)
        self.status_grid.addWidget(self.status_line_edit,2,1)

        #add widgets/layouts to the grow layout
        self.grow_grid.addWidget(self.status_grid,0,1)
        self.grow_grid.addWidget(self.manual_grow_button,1,0)
        self.grow_grid.addWidget(self.auto_grow_button,1,1)

        #create a widget to hold layout
        self.view_crop_widget = QWidget()
        self.view_crop_widget.setLayout(self.grow_grid)
        


    def instantiate_crop(self):
        crop_type = self.crop_radio_buttons.selected_button() #get the radio button that was selected
        if crop_type == 1:
            self.simulated_crop = Wheat()
            
        elif crop_type == 2:
            self.simulated_crop = Potato()
        print(self.simulated_crop)
        

    

def main():
    crop_simulation = QApplication(sys.argv)
    crop_window = CropWindow()
    crop_window.show()
    crop_window.raise_()
    crop_simulation.exec_()

if __name__ == "__main__":
    main()
