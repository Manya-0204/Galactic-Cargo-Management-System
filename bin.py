# class Bin:
#     def __init__(self, bin_id, capacity):
#         pass

#     def add_object(self, object):
#         # Implement logic to add an object to this bin
#         pass

#     def remove_object(self, object_id):
#         # Implement logic to remove an object by ID
#         pass

from avl import AVLTree
from object import Object  
    
class Bin:
    def __init__(self, bin_id, capacity):
        self.bin_id = bin_id
        self.capacity = capacity
        self.remaining_capacity=capacity
        self.objects = AVLTree() 
        
        
    def compare_object_by_id(self,obj1,obj2):
        return obj1.object_id - obj2.object_id

    def add_object(self,object):
        if self.remaining_capacity >= object.size:
           
            self.objects.insert(object.object_id,object.size)
            self.remaining_capacity -= object.size
            
       
    def remove_object(self,object_id):
        object=self.objects.search(object_id)
        if object:
            self.objects.delete_value(object_id)
        self.remaining_capacity += object.size 
   
