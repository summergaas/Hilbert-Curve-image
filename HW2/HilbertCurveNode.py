class HilbertCurveNode():
    def __init__( self, data=None, depth=None, startPattern=None, directionPattern = None, next=None, prev=None):
        self.data = data
        #Data is NodePath list points
        self.depth = depth
        self.startPattern = startPattern
        self.directionPattern = directionPattern
        #startPattern and directionPattern are used to direct the NodePath
        self.next = next
        self.prev = prev

    def get_data(self):
        return self.data

    def set_data(self, new_data):
        self.data = new_data
    
    def set_depth(self, new_depth):
        self.depth = new_depth

    def get_depth(self):
        return self.depth

    def set_startPattern(self, new_pattern):
        self.startPattern = new_pattern

    def get_startPattern(self):
        return self.startPattern

    def set_directionPattern(self, new_pattern):
        self.directionPattern = new_pattern

    def get_directionPattern(self):
        return self.directionPattern

    def get_next(self):
        return self.next

    def set_next(self, new_next):
        self.next = new_next

    def get_prev(self):
        return self.prev

    def set_prev(self, new_prev):
        self.prev = new_prev



#def main():
#    hcn = HilbertCurveNode()
#    return hcn

#hcn = main()
#hcn.set_data([])
#hcn.set_depth(0)
#n = hcn.get_depth()
#print(n)
