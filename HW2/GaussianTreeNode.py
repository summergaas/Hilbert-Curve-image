class GaussianTreeNode():
    def __init__( self, data=None, pyramid_index=None, child1=None, child2=None, child3=None, child4=None, parent=None):
        self.data = data
        self.pyramid_index = pyramid_index
        self.child1 = child1
        self.child2 = child2
        self.child3 =  child3
        self.child4 = child4
        self.parent = parent

    def get_data(self):
        return self.data

    def set_data(self, new_data):
        self.data = new_data

    def get_pyramid_index(self):
        return self.pyramid_index

    def set_pyramid_index(self, new_pyramid_index):
        self.pyramid_index = new_pyramid_index

    def get_child1(self):
        return self.child1

    def set_child1(self, new_child1):
        self.child1 = new_child1

    def get_child2(self):
        return self.child2

    def set_child2(self, new_child2):
        self.child2 = new_child2

    def get_child3(self):
        return self.child3

    def set_child3(self, new_child3):
        self.child3 = new_child3

    def get_child4(self):
        return self.child4

    def set_child4(self, new_child4):
        self.child4 = new_child4

    def get_parent(self):
        return self.parent

    def set_parent(self, new_parent):
        self.parent = new_parent


    