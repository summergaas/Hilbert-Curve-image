import math
from GaussianTree import GaussianTree
from GaussianTreeNode import GaussianTreeNode


def Reduce(gaussianPyramid, inputList, condensed, a):
    if a == 0:
        return gaussianPyramid
    i = 0
    j = 1
    k = 0
    while j< len(inputList):
        condensed.append([])
        m = 0
        n = 1
        while n < len(inputList):
            sum = inputList[i][m]+inputList[i][n]+inputList[j][m]+inputList[j][n]
            avg = sum/4
            condensed[k].append(avg)
            m = m+2
            n = n+2
        i = i+2
        j = j+2
        k = k+1
    gaussianPyramid.append(condensed)
    return Reduce(gaussianPyramid, condensed, [], a-1)

def convertFile(filename):
    result = []
    fileStream = open(filename, 'r')
    for line in fileStream:
        lineList = []
        line = line.replace('\n','')
        line = line.replace(',','')
        for l in line:
            i = int(l)
            lineList.append(i)
        result.append(lineList)
    return result

def getInput():
    input2 = input("Enter the file path for the Gaussian pyramid.")
    d = int(input2)
    return d

def getGaussian(filename):
    inputList = convertFile(filename)
    a = math.log(len(inputList), 2)
    a = int(a)
    gaussianPyramid = []
    gaussianPyramid.append(inputList)
    gaussianPyramid = Reduce(gaussianPyramid, inputList, [], a)
    return gaussianPyramid

def getGaussianTree(g):
    gt = GaussianTree()
    l = len(g)
    i = l-1
    j = 0
    k = 0
    root = GaussianTreeNode()
    root.set_data(g[i][j][k])
    root.set_pyramid_index([i, j, k])
    gt.set_root(root)
    Q = []
    Q.append(root)
    while len(Q)>0:
        parent = Q.pop()
        parent_pyramid_index = parent.get_pyramid_index()
        if parent_pyramid_index[0]>0:

            child1_pyramid_index = [(parent_pyramid_index[0]-1), (parent_pyramid_index[1]*2), (parent_pyramid_index[2]*2)]
            child1 = GaussianTreeNode()
            child1.set_data(g[child1_pyramid_index[0]][child1_pyramid_index[1]][child1_pyramid_index[2]])
            child1.set_pyramid_index(child1_pyramid_index)
            child1.set_parent(parent)
            parent.set_child1(child1)
            Q.append(child1)
        
            child2_pyramid_index = [(parent_pyramid_index[0]-1), (parent_pyramid_index[1]*2), ((parent_pyramid_index[2]*2)+1)]
            child2 = GaussianTreeNode()
            child2.set_data(g[child2_pyramid_index[0]][child2_pyramid_index[1]][child2_pyramid_index[2]])
            child2.set_pyramid_index(child2_pyramid_index)
            child2.set_parent(parent)
            parent.set_child2(child2)
            Q.append(child2)

            child3_pyramid_index = [(parent_pyramid_index[0]-1), ((parent_pyramid_index[1]*2)+1), (parent_pyramid_index[2]*2)]
            child3 = GaussianTreeNode()
            child3.set_data(g[child3_pyramid_index[0]][child3_pyramid_index[1]][child3_pyramid_index[2]])
            child3.set_pyramid_index(child3_pyramid_index)
            child3.set_parent(parent)
            parent.set_child3(child3)
            Q.append(child3)

            child4_pyramid_index = [(parent_pyramid_index[0]-1), ((parent_pyramid_index[1]*2)+1), ((parent_pyramid_index[2]*2)+1)]
            child4 = GaussianTreeNode()
            child4.set_data(g[child4_pyramid_index[0]][child4_pyramid_index[1]][child4_pyramid_index[2]])
            child4.set_pyramid_index(child4_pyramid_index)
            child4.set_parent(parent)
            parent.set_child4(child4)
            Q.append(child4)

        else:
            parent.set_child1(gt.get_leaf())
            parent.set_child2(gt.get_leaf())
            parent.set_child3(gt.get_leaf())
            parent.set_child4(gt.get_leaf())

    return gt
#makeChanges