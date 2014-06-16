from crop_class import *

class Potato(Crop):
    """A potato crop"""

    #constructor
    def __init__(self):
        #call parent class constructor with default values for potato
        #growth rate = 1; light need = 3; water need = 6
        super().__init__(1,3,6)
        self._type = "Potato"

if __name__ == "__main__":
    new_crop = Potato()
    manage_crop(new_crop)
