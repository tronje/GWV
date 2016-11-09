import Queue
from help import *

#TODO: not tested
def search(field,start=(0,0),queue=Queue.Queue()):
    '''
    search path with circle detection
    :param field:
    :param start:
    :param queue:
    :return: Node()
    '''
    moves=move_matrix()
    root=Node(start)
    Q=queue
    Q.put(root)
    run=True
    while run:
        try:
            N=Q.get_nowait()
            if field.isTarget(N.xy):
                return N
            l=N.get_next(moves)
            for nextN in l:
                if (not field.isBlocked(nextN)) and (not N.isIn(nextN)):
                    Q.put(Node(nextN,N))
        except:
            run=False
    return None

def searchAll(field,start=(0,0),queue=Queue.Queue()):
    '''
    search all paths with circle detection
    :param field:
    :param start:
    :param queue:
    :return: [Node(),...]
    '''
    moves=move_matrix()
    root=Node(start)
    Q=queue
    Q.put(root)
    L=[]
    run=True
    while run:
        try:
            N=Q.get_nowait()
            if field.isTarget(N.xy):
                L.append(N)
            l=N.get_next(moves)
            for nextN in l:
                if (not field.isBlocked(nextN)) and (not N.isIn(nextN)):
                    Q.put(Node(nextN,N))
        except:
            run=False
    return L

def dfs(field,start):
    search(field,start,Queue.LifoQueue())
def bfs(field,start):
    search(field,start,Queue.Queue())
def dfsAll(field,start):
    searchAll(field,start,Queue.LifoQueue())
def bfsAll(field,start):
    searchAll(field,start,Queue.Queue())