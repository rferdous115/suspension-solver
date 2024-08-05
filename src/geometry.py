# representing the 3D point in space
class Hardpoint:    
    # constructor. Automatically called when an instanc of a class is made.
    def __init__(self, name, x, y, z):
        # 'self' refers to the current instance of the class.
        self.name = name
        self.x = x
        self.y = y
        self.z = z

# handles collection of hardpoints
class Geometry:
    def __init__(self, hardpoints):
        self.hardpoints = hardpoints
        self.hardpoint_dict = {hp.name: hp for hp in hardpoints}