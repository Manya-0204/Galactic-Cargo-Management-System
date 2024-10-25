# from bin import Bin
# from avl import AVLTree
# from object import Object, Color
# from exceptions import NoBinFoundException

# class GCMS:
#     def __init__(self):
#         # Maintain all the Bins and Objects in GCMS
#         pass 

#     def add_bin(self, bin_id, capacity):
#         pass

#     def add_object(self, object_id, size, color):
#         raise NoBinFoundException

#     def delete_object(self, object_id):
#         # Implement logic to remove an object from its bin
#         pass

#     def bin_info(self, bin_id):
#         # returns a tuple with current capacity of the bin and the list of objects in the bin (int, list[int])
#         pass

#     def object_info(self, object_id):
#         # returns the bin_id in which the object is stored
#         pass

from node import Node
from bin import Bin
from object import  Object, Color
from avl import AVLTree
from exceptions import NoBinFoundException
from avl import compare_1,compare_2

class GCMS:
    def __init__(self):
        self.bin_id_tree = AVLTree() 
        self.capacity_tree=AVLTree()
        self.object_tree_binid=AVLTree()
        self.object_tree_size = AVLTree()
        self.lesser_id_tree = AVLTree(compare_2)
        
              
        
    def add_bin(self, bin_id, capacity):
        
        self.bin_id_tree.insert_value(bin_id,capacity)
        temp = AVLTree()
        self.capacity_tree.insert_value([capacity,bin_id],temp)
        self.lesser_id_tree.insert_value([capacity,bin_id],temp)

        
        
    def add_object(self, object_id, size, color):
   
        if color == Color.BLUE:
            chosen_bin = self.find_compact_bin_blue(self.capacity_tree.root,size)
            if chosen_bin.key[0]<size:
                raise NoBinFoundException
            
        elif color == Color.YELLOW:
            chosen_bin = self.find_compact_bin_yellow(self.lesser_id_tree.root,size)
            if chosen_bin.key[0]<size:
                raise NoBinFoundException
            
        elif color == Color.RED:
            chosen_bin = self.find_largest_bin_red(self.lesser_id_tree.root,size)
            if chosen_bin.key[0]<size:
                raise NoBinFoundException
         
        elif color == Color.GREEN:
            chosen_bin = self.find_largest_bin_green(self.capacity_tree.root,size)
            if chosen_bin.key[0]<size:
                raise NoBinFoundException
        
        
        
        if chosen_bin is None:
            return NoBinFoundException
        
        self.object_tree_binid.insert_value(object_id,chosen_bin.key[1])
        self.object_tree_size.insert_value(object_id,size)
        
        # Update the AVL tree 
        self.bin_id_tree.delete_value(chosen_bin.key[1])
        
        
        temp_object_tree = chosen_bin.value
        temp_object_tree.insert_value(object_id, size)
        c=temp_object_tree
        temp_key = chosen_bin.key
        a=temp_key[0]
        b=temp_key[1]
        self.capacity_tree.delete_value([temp_key[0],temp_key[1]])
        self.lesser_id_tree.delete_value([temp_key[0],temp_key[1]])
        
        temp_key[0] -= size
        
        
        self.bin_id_tree.insert_value(b,a-size)
       
        self.capacity_tree.insert_value(temp_key,c)
        self.lesser_id_tree.insert_value(temp_key,c)
  
    
        
    def find_compact_bin_blue(self,root,size):
        curr=root
        req_bin=curr
        while (curr!=None):
            if curr.key[0]>=size:
                req_bin=curr
                curr=curr.left
            else:
                curr=curr.right
        return req_bin
    def find_compact_bin_yellow(self,root,size):
        curr=root
        req_bin=curr
        while (curr!=None):
            if curr.key[0]>=size:
                req_bin=curr
                curr=curr.left
            else:
                curr=curr.right
                
        return req_bin
    
    def find_largest_bin_red(self,root,size):
        current=root
        while current.right :
            current=current.right
        return current
    def find_largest_bin_green(self,root,size):
        current=root
        while current.right:
                current=current.right
        return current  
        
        


    def delete_object(self, object_id):
        obj_node = self.object_tree_size.search(object_id)
        if obj_node==None:
            return None
        object_size = obj_node.value
        bin_node=self.object_tree_binid.search(object_id)
        
        bin_found=self.bin_id_tree.search(bin_node.value)
        fg=bin_found.key
        size_of_bin_containing_object = bin_found.value
        self.bin_id_tree.delete_value(bin_found.key)
        m = self.capacity_tree.search([size_of_bin_containing_object,fg])
        objtree=m.value
        objtree.delete_value(object_id)
        n= self.lesser_id_tree.search([size_of_bin_containing_object,fg])
        objtree1=n.value
        objtree1.delete_value(object_id)
        
        self.capacity_tree.delete_value([size_of_bin_containing_object,fg])
        self.lesser_id_tree.delete_value([size_of_bin_containing_object,fg])
        self.object_tree_binid.delete_value(object_id)
        self.object_tree_size.delete_value(object_id)
         
        size_of_bin_containing_object += object_size
        
        self.bin_id_tree.insert_value(fg,size_of_bin_containing_object)
        self.capacity_tree.insert_value([size_of_bin_containing_object,fg],objtree)
        self.lesser_id_tree.insert_value([size_of_bin_containing_object,fg],objtree1)
        
        

    def bin_info(self, bin_id):
        bin_node = self.bin_id_tree.search(bin_id)
        
        object_ofthebin_tree_node =self.capacity_tree.search([bin_node.value,bin_node.key])
        
        object_ofthebin_tree = object_ofthebin_tree_node.value
        
        objs_list = object_ofthebin_tree.object_list_inorder(object_ofthebin_tree.root)
        
        
        if bin_node:
            return (bin_node.value,objs_list)
        return None
            
    
    
        
    def object_info(self, object_id):
        bin_node = self.object_tree_binid.search(object_id)
        if bin_node is not None:
            return bin_node.value
        else:
            return None