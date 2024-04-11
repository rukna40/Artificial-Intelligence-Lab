class Node:
    def __init__(self,data):
        self.left=None
        self.right=None
        self.data=data
        
    def insert(self,data):
        if self.data:
            if data<self.data:
                if self.left is None:
                    self.left=Node(data)
                else:
                    self.left.insert(data)
            elif data>self.data:
                if self.right is None:
                    self.right=Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data=data

    def inorder(self):
        if self.left:
            self.left.inorder()
        print( self.data)
        if self.right:
            self.right.inorder()
        
    def preorder(self):
        print( self.data)
        if self.left:
            self.left.inorder()
        if self.right:
            self.right.inorder()

    def postorder(self):
        if self.left:
            self.left.inorder()
        if self.right:
            self.right.inorder()
        print( self.data)

if __name__ == "__main__":
    root = Node(5)
    root.insert(3)
    root.insert(7)
    root.insert(2)
    root.insert(4)
    root.insert(6)
    root.insert(8)

    print("Inorder traversal:")
    root.inorder()

    print("\nPreorder traversal:")
    root.preorder()

    print("\nPostorder traversal:")
    root.postorder()