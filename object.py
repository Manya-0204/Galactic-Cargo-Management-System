# from enum import Enum

# class Color(Enum):
#     BLUE = 1
#     YELLOW = 2
#     RED = 3
#     GREEN = 4
    

# class Object:
#     def __init__(self, object_id, size, color):
#         pass

from enum import Enum

class Color(Enum):
    BLUE = 1
    YELLOW = 2
    RED = 3
    GREEN = 4
    

class Object:
    def __init__(self, object_id, size, color):
        self.obj_id = object_id
        self.obj_size = size
        self.obj_color = color
        pass



