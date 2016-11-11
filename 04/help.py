def move_matrix(x=4):
    m=[(-1,0),(0,-1),(1,0),(0,1),(-1,-1),(-1,1),(1,-1),(1,1)]
    return m[0:4]
MoveMatrixMAP={(-1,0):"Left",(0,-1):"Down",(1,0):"Right",(0,1):"Up",(-1,-1):"",(-1,1):"",(1,-1):"",(1,1):""}
def direc(FROM,TO,MAP=MoveMatrixMAP):
    d=tuple(map(lambda a,b: a-b, TO.xy,FROM.xy))
    if d in MAP.keys():
        return MAP[d]
    return str(d)

class Node(object):
    def __init__(self,xy=(0,0),root=None):
        self.xy=tuple(xy)
        self.root=root
        self.effect=None
    def get_next(self,xyOffsets=[]):
        l=[]
        for xyo in xyOffsets:
            l.append(tuple(map(lambda a,b:a+b,self.xy,xyo)))
        return l
    def isIn(self,xy):
        if tuple(xy)==self.xy:
            return True
        elif self.root==None:
            return False
        else:
            return self.root.isIn(xy)