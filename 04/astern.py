import Queue
from help import *

class QElement(object):
    fieldDimension=50*50
    def __init__(self,xy=(0,0),t=(0,0)):
        self.xy=xy
        self.target=t
        self.val=abs(xy[0]-z[0])+abs(xy[1]-z[1])
        self.toVal=None
        self.root=None
        pass
    def __cmp__(self,obj):
        if obj==None:
            return 1
        elif type(obj)==QElement:
            v1=self.getVal()
            v2=obj.getVal()
            if v1<v2:
                return -1
            elif v1>v2:
                return 1
            else:
                return 0
        else:
            return -1
        pass
    def getVal(self):
        v=self.val
        if self.toVal==None:
            v+=QElement.fieldDimension
        else:
            v+=self.toVal
        return v

def astern(field,start=(0,0),target=(0,0)):#TODO: rebuild
    MATRIX=set()
    moves=move_matrix()
    Q=Queue.PriorityQueue()
    qe=QElement(start,target)
    Q.put(qe)
    MATRIX.add(start)
    run=True
    while run:
        try:
            qe=Q.get_nowait()
            for m in moves:
                xy=map(lambda a,b:a+b, qe.xy,m)
                if xy[0]==target[0] and xy[1]==target[1]:
                    nqe=QElement(xy,target)
                    nqe.root=qe
                    return nqe
                elif (not isBlocked(xy,env)) and (not tuple(xy) in MATRIX):
                    nqe=QElement(xy,target)
                    nqe.root=qe
                    Q.put(nqe)
                    MATRIX.add(tuple(nqe))
        except:
            run=False
    return None