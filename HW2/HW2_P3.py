from HW2_P1 import*
from HW2_P2 import*
from GaussianTree import GaussianTree
from GaussianTreeNode import GaussianTreeNode

def findSubHC(node):
     node_pyramid_index = node.get_pyramid_index()
     size = l*(node_pyramid_index[0]+1)
     upperY = 26 - (node_pyramid_index[1]*size)
     lowerY = upperY - size
     leftX = -26 + (node_pyramid_index[2]*size)
     rightX = leftX + size
     bounds = [(leftX, lowerY, 0), (leftX, upperY, 0), (rightX, upperY, 0), (rightX, lowerY, 0)]
     HC = createHilbertCurve(node.get_data(), bounds)
     return HC


def dynamicHilbertCurve(gt, l):
    dynamicHilbertCurveNodePath = []
    root = gt.get_root()
    Q = []
    Q.append(root)
    while len(Q)>0:
            current = Q.pop(0)
            child1 = current.get_child1()
            child2 =  current.get_child2()
            child3 = current.get_child3()
            child4 = current.get_child4()
            currentData = current.get_data()
            child1Data = child1.get_data()
            child2Data = child2.get_data()
            child3Data = child3.get_data()
            child4Data = child4.get_data()
            
            if currentData >= child1Data & currentData >= child2Data & currentData >= child3Data & currentData >= child4Data:
                HC = findSubHC(current)
                HC.insert(0, 0)
                for d in HC:
                    dynamicHilbertCurveNodePath.append(d)
            
            elif child1.get_child1().get_data() == None:
                HC1 = findSubHC(child1)
                HC1.insert(0, 0)
                HC2 = findSubHC(child2)
                HC2.insert(0, 0)
                HC3 = findSubHC(child3)
                HC3.insert(0, 0)                
                HC4 = findSubHC(child4)
                HC4.insert(0, 0)
                HC = HC1+HC2+HC3+HC4
                for d in HC:
                    dynamicHilbertCurveNodePath.append(d)

            else:
                Q.append(child1)
                Q.append(child2)
                Q.append(child3)
                Q.append(child4)
            
    segs = LineSegs()
    segs.setThickness(2.0)
    segs.setColor( Vec4(0, 2, 1, 1))
    i = 0
    while i<len(dynamicHilbertCurveNodePath):
        if dynamicHilbertCurveNodePath[i] == 0:
            i = i+1
            segs.moveTo(dynamicHilbertCurveNodePath[i])
        else:
            segs.drawTo(dynamicHilbertCurveNodePath[i])
        i = i+1
    return segs.create( )

def getInput():
    d = input("Please place a copy of the test file into the HW2-P3 subfolder and enter its name, using quotations.")
    return d

d = getInput()
g = getGaussian(d)
n = float(len(g[0]))
l = float(52/n)
#l is the size of each unit in the grid
gt = getGaussianTree(g)
import direct.directbase.DirectStart
render.attachNewNode( createBox(n))
render.attachNewNode( dynamicHilbertCurve(gt, l) )
base.disableMouse( )
base.camera.setPos( 0, 0, 100 )
base.camera.lookAt( 0, 0, 0 )
base.run( )

