from GaussianTreeNode import GaussianTreeNode

class GaussianTree():
    def __init__( self, root=None, leaf=None ):
        self.root = root
        self.leaf = leaf
        self.leaf = GaussianTreeNode()
        
    def set_root(self, new_root):
        self.root = new_root
          
    def get_root(self):
        return self.root

    def get_leaf(self):
        return self.leaf



