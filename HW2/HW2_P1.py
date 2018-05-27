from pandac.PandaModules import NodePath
from pandac.PandaModules import Point3
from pandac.PandaModules import Vec4
from pandac.PandaModules import LineSegs
from DynamicLinkedList import DynamicLinkedList
from HilbertCurveNode import HilbertCurveNode
import math

def map(prevHCN, newHCN, x):
    newPath = []
    oldPath = prevHCN.get_data()
    newStartPattern = newHCN.get_startPattern()
    newDirectionPattern = newHCN.get_directionPattern()
    newDepth = newHCN.get_depth()
    a =  x/(math.pow(2, newDepth-1))
    i = 0
    while i<len(oldPath):
        np = oldPath[i]
        if newStartPattern[i] == 0:
            #start with the bottom left
            np1 = (np[0]-a, np[1]-a, 0)
            newPath.append(np1)
            if newDirectionPattern[i] == 2:
                #move clockwise
                np2 = (np[0]-a, np[1]+a, 0)
                np3 = (np[0]+a, np[1]+a, 0)
                np4 = (np[0]+a, np[1]-a, 0)
                newPath.append(np2)
                newPath.append(np3)
                newPath.append(np4)
            else:
                #move counterclockwise
                np2 = (np[0]+a, np[1]-a, 0)
                np3 = (np[0]+a, np[1]+a, 0)
                np4 = (np[0]-a, np[1]+a, 0)
                newPath.append(np2)
                newPath.append(np3)
                newPath.append(np4)
        elif newStartPattern[i] == 1:
            #start with the top right
            np1 = (np[0]+a, np[1]+a, 0)
            newPath.append(np1)
            if newDirectionPattern[i] == 2:
                #move clockwise
                np2 = (np[0]+a, np[1]-a, 0)
                np3 = (np[0]-a, np[1]-a, 0)
                np4 = (np[0]-a, np[1]+a, 0)
                newPath.append(np2)
                newPath.append(np3)
                newPath.append(np4)
            else:
                #move counterclockwise
                np2 = (np[0]-a, np[1]+a, 0)
                np3 = (np[0]-a, np[1]-a, 0)
                np4 = (np[0]+a, np[1]-a, 0)
                newPath.append(np2)
                newPath.append(np3)
                newPath.append(np4)
        i = i+1
    return newPath

def pointsFinder(dl, newHCN, prevHCN, bounds):
    newPath = []
    oldPath = prevHCN.get_data()
    newStartPattern = []
    oldStartPattern = prevHCN.get_startPattern()
    newDirectionPattern = []
    oldDirectionPattern = prevHCN.get_directionPattern()
    sizeHC = float(abs(bounds[0][0] - bounds[2][0]))
    x = sizeHC/4
    if dl.head == prevHCN:
        #NodePath of the first Hilbert Curve
        np1 = (bounds[0][0]+x, bounds[0][1]+x, 0)
        np2 = (bounds[0][0]+x, bounds[0][1]+(3*x), 0)
        np3 = (bounds[0][0]+(3*x), bounds[0][1]+(3*x), 0)
        np4 = (bounds[0][0]+(3*x), bounds[0][1]+x, 0)
        newPath.append(np1)
        newPath.append(np2)
        newPath.append(np3)
        newPath.append(np4)
        #Direction around the center point that the first curve takes
        newStartPattern.append(0)
        newHCN.set_startPattern(newStartPattern)
        #A startPattern = 0 shows that this curve starts at the bottom left quadrant
        newDirectionPattern.append(2)
        newHCN.set_directionPattern(newDirectionPattern)
        #A directionPattern = 2 shows that this curve will move clockwise around the point
    else:
        #The newStartPattern will repeat the oldStartPattern 3 times
        #The startPattern is a sequence of 0's and 1's. 
        #0 signifies that we will start at the bottom left quadrant a given point
        #1 signifies that we will start at the bottom right quadrant of a given point
        i = 3
        while i>0:
            for d in oldStartPattern:
                newStartPattern.append(d)
            i = i-1
        #Then, the newStartPattern will inverse the oldStartPattern
        for d in oldStartPattern:
            if d == 0:
                newStartPattern.append(1)
            else:
                newStartPattern.append(0)
        newHCN.set_startPattern(newStartPattern)
        #NewStartPattern should be 4 times as long as oldStartPattern
        #NewStartPattern will help direct the new NodePath using the decision tree
        #The newDirectionPattern will be formed by taking the inverse of the oldDirectioinPattern,
        #repeating the oldDirectionPattern twice, and then adding the inverse again
        #2's preresent moving clockwise around a point. 3's represent moving counterclockwise.
        for d in oldDirectionPattern:
            if d == 2:
                newDirectionPattern.append(3)
            else:
                newDirectionPattern.append(2)
        i = 2
        while i>0:
            for d in oldDirectionPattern:
                newDirectionPattern.append(d)
            i = i-1
        for d in oldDirectionPattern:
            if d == 2:
                newDirectionPattern.append(3)
            else:
                newDirectionPattern.append(2)
        newHCN.set_directionPattern(newDirectionPattern)
        #Now that our patterns are set, we can use the decision tree to create our newPath
        newPath = map(prevHCN, newHCN, x)
        #x is the size of the bounded area divided by 4
    return newPath

def recursiveHilbertHelper(dl, points, d, bounds):
    if d == 0:
        return points
    newHCN = HilbertCurveNode()
    dl.add(newHCN)
    newHCN.set_depth(newHCN.prev.get_depth() + 1)
    newHCNdata = pointsFinder(dl, newHCN, newHCN.prev, bounds)
    newHCN.set_data(newHCNdata)
    points = newHCNdata
    return recursiveHilbertHelper(dl, points, d-1, bounds)

def createHilbertCurve(d, bounds): 
    #bounds is the np that bounds the HC
    points = []
    dl = DynamicLinkedList()
    hcn = HilbertCurveNode()
    dl.add(hcn)
    hcn.set_data(points)
    hcn.set_depth(0)
    finalHCPoints = recursiveHilbertHelper(dl, points, d, bounds)
    return finalHCPoints

def createBox(n):
    boxpoints = []
    np1 = (-26, -26, 0)
    np2 = (-26, 26, 0)
    np3 = (26, 26, 0)
    np4 = (26, -26, 0)
    boxpoints.append(np1)
    boxpoints.append(np2)
    boxpoints.append(np3)
    boxpoints.append(np4)
    boxpoints.append(np1)
    boxsegs = LineSegs()
    boxsegs.setThickness(2.0)
    boxsegs.setColor( Vec4(0.002, 0.002, 0.002, 0.18))
    boxsegs.moveTo(boxpoints[0])
    for p in boxpoints[1:]: 
        boxsegs.drawTo(p)
    gridPoints=[]
    l = float(52/n)
    i = 1
    while i<(n):
        np= (-26, (-26+(l*i)), 0)
        np2= (26, (-26+(l*i)), 0)
        np3 = ((-26+(l*i)), -26, 0)
        np4 = ((-26+(l*i)), 26, 0)
        gridPoints.append((np, np2))
        gridPoints.append((np3, np4))
        i = i+1
    for p in gridPoints:
        boxsegs.moveTo(p[0])
        boxsegs.drawTo(p[1])
    return boxsegs.create( )

def HCtest():
#    bounds = [(-10, -16, 0), (-10, 11, 0), (17, 11, 0), (17, -16, 0)]
    bounds = [(0, -3, 0), (0, 16, 0), (19, 16, 0), (19, -3, 0)]
    finalHCPoints = createHilbertCurve(4, bounds)
    boxsegs = LineSegs()
    boxsegs.setThickness(2.0)
    boxsegs.setColor( Vec4(1, 1, 1, 1))
    boxsegs.moveTo(bounds[0])
    boxsegs.drawTo(bounds[1])
    boxsegs.drawTo(bounds[2])
    boxsegs.drawTo(bounds[3])
    boxsegs.drawTo(bounds[0])
    boxsegs.moveTo(finalHCPoints[0])
    for p in finalHCPoints[1:]: 
        boxsegs.drawTo(p)
    return boxsegs.create()

#import direct.directbase.DirectStart
#render.attachNewNode(HCtest())
#base.disableMouse( )
#base.camera.setPos( 0, 0, 100 )
#base.camera.lookAt( 0, 0, 0 )
#base.run( )

