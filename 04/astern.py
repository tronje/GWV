import Queue
from help import *

class QElement(Node):
    fieldDimension=50*50
    def __init__(self,xy=(0,0),t=(0,0),root=None):
        Node.__init__(self,xy)
        self.target=t
        self.val=abs(xy[0]-z[0])+abs(xy[1]-z[1])
        self.toVal=None
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

def astern(field,start=(0,0),target=(0,0)):
    moves=move_matrix()
    Q=Queue.PriorityQueue()
    qe=QElement(start,target)
    Q.put(qe)
    run=True
    while run:
        try:
            N=Q.get_nowait()
            if field.isTarget(N.xy):
                return N
            #Portal
            #TODO: Portal
            #Portal-end
            l = N.get_next(moves)
            for nextN in l:
                if (not field.isBlocked(nextN)) and (not N.isIn(nextN)):
                    nN=QElement(nextN,N.target, N)
                    Q.put(nN)
                    nN.effect=direc(N, nN)
        except:
            run=False
    return None