from numpy import *
import operator #运算符模块

def createDataSet():
    group = array([[1,1.1],[1,1],[0,0],[0,0.1]])
    lables = ['A','A','B','B']
    return group,lables
def classify0(inX,dataSet,labels,k):
    dataSetSize = dataSet.shape[0]#行数
    diffMat = tile(inX,(dataSetSize,1))-dataSet
    sqDiffMat = diffMat**2
    sqDistances = sqDiffMat.sum(axis=1)
    distances=sqDistances**0.5
    sorteDistIndicies = distances.argsort()
    classCount={}
    for i in range(k):
        voteIlabel= labels[sorteDistIndicies[i]]
        classCount[voteIlabel]=classCount.get(voteIlabel,0)+1
    sortedClassCount = sorted(classCount.iteritems(),key=operator.itemgetter(1),reverse=True)
    return sortedClassCount[0][0]



if __name__ == '__main__':
    group,lables=createDataSet()
    print(str(group.shape[0]))