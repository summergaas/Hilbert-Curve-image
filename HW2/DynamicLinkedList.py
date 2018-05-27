from HilbertCurveNode import HilbertCurveNode

class DynamicLinkedList():
    def __init__( self, head=None ):
        self.head = head
        #This will be a cyclical linkedlist, so head will serve as the head and the tail

    def add( self, node ) :
        if self.head == None :
            self.head = node
            self.head.prev = node
            self.head.next = node
        else :
            temp = self.head.prev
            temp.next = node
            node.next = self.head
            self.head.prev = node
            node.prev = temp

    def get_head(self):
        return self.head
 
#def main():
#    dl = DynamicLinkedList()
#    return dl

#dl = main() 

