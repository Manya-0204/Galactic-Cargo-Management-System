# from node import Node

# def comp_1(node_1, node_2):
#     pass

# class AVLTree:
#     def __init__(self, compare_function=comp_1):
#         self.root = None
#         self.size = 0
#         self.comparator = compare_function

from node import Node

    
def compare_1(value_1, value_2):
    if value_1> value_2:  
        return 1
    elif value_2>value_1 :
        return -1
    else :
        return 0
    

def compare_2(value_1, value_2):

    if value_1[0]> value_2[0]:  
        return 1
    elif value_2[0]>value_1[0] :
        return -1
    else :
        if value_1[1]< value_2[1]:  
            return 1
        if value_1[1]>value_2[1] :
            return -1
        else:
            return 0
    
class AVLTree:
    
   
    def __init__(self,compare_function=compare_1):
        self.root = None
        self.comparator = compare_function 
        self.size=0

    def comp_1(self,value_1, value_2):
        if value_1> value_2:  
            return 1
        elif value_2>value_1 :
            return -1
        else :
            return 0
 
       
    def comp_2(value_1, value_2):
  
        if value_1[0]> value_2[0]:  
            return 1
        elif value_2[0]>value_1[0] :
            return -1
        else :
            if value_1[1]< value_2[1]:  
                return 1
            if value_1[1]>value_2[1] :
             return -1
            else:
                return 0
   
        
    def height(self, node):
        return node.height if node else 0

    def balance(self, node):
        return self.height(node.left) - self.height(node.right)

    def _rotate_left(self, node):
        new_root = node.right
        node.right = new_root.left
        new_root.left = node
        node.height = 1 + max(self.height(node.left), self.height(node.right))
        new_root.height = 1 + max(self.height(new_root.left), self.height(new_root.right))
        return new_root

    def _rotate_right(self, node):
        new_root = node.left
        node.left = new_root.right
        new_root.right = node
        node.height = 1 + max(self.height(node.left), self.height(node.right))
        new_root.height = 1 + max(self.height(new_root.left), self.height(new_root.right))
        return new_root
   
    def min_value_node(self,node):
        while node.left:
            node = node.left
            
        return node
           
        
    def insert(self, node,key,value):
        if not node:
            self.size+=1
            return Node(key,value)

        # if key < root.key:
        if self.comparator(key,node.key) <0:
            node.left = self.insert(node.left,key,value)
        
        else:
            node.right = self.insert(node.right, key,value)
        node.height = 1 + max(self.height(node.left), self.height(node.right))
        return self.Balance_tree(node)


    def Balance_tree(self,node) :
        balance = self.balance(node)
        # Balancing the AVL Tree
        if balance > 1 and self.height(node.left.left)>=self.height(node.left.right):
            return self._rotate_right(node)

        if balance < -1 and self.height(node.right.right)>=self.height(node.right.left):
            return self._rotate_left(node)

        if balance > 1 and self.height(node.left.left)<self.height(node.left.right):
            node.left = self._rotate_left(node.left)
            return self._rotate_right(node)

        if balance < -1 and self.height(node.right.right)<self.height(node.right.left):
            node.right = self._rotate_right(node.right)
            return self._rotate_left(node)
        
        return node

    def delete(self, node, key):
        if not node:
            return node

        if self.comparator(key,node.key)<0:
            node.left = self.delete(node.left, key)
        elif self.comparator(key,node.key)>0:
            node.right = self.delete(node.right, key)
        else:
            if node.left is None:
                self.size-=1
                return node.right
            elif node.right is None:
                self.size-=1
                return node.left
            
            temp = self.min_value_node(node.right)
            node.key=temp.key
            node.value=temp.value
            node.right = self.delete(node.right,temp.key)


        node.height = 1 + max(self.height(node.left), self.height(node.right))
        return self.Balance_tree(node)
        
        
        
    def search(self,key):
        node=self.root
        while node is not None:
            if self.comparator(key,node.key)==0:
                return node
            elif self.comparator(key,node.key)<0:
                node=node.left
            else:
                node=node.right
        return node

    def insert_value(self,key,value):
        self.root = self.insert(self.root, key,value)

    def delete_value(self, key):
        self.root = self.delete(self.root, key)

    
    def object_list_inorder(self,root):
        if root is None:
            return []
        obj=self.object_list_inorder(root.left)+ [root.key] + self.object_list_inorder(root.right) 
        return obj
    
   
