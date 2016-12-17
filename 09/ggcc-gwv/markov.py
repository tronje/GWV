#!/usr/bin/env python3
import random,time
import copy

class MarkovNode(object):
    '''
    A Markov Chain Node
    '''
    Nodes={}
    def __init__(self,name):
        '''
        :param name: The Identificator of the Node
        '''
        MarkovNode.Nodes[name]=self
        self.name=name
        self._from=[]
        self._to=[]
        self._toProbability=[]
        self._toPUpdated=False
        pass
    def __lt__(self,other):
        return 0
    def __gt__(self,other):
        return 0
    def __eq__(self,other):
        return 0
    def __le__(self,other):
        return 0
    def __ge__(self,other):
        return 0
    def __ne__(self,other):
        return 0
    def getNextRandom(self):
        '''
        Get the next Chain Connection Object on base of the Object.priority
        :return: MarkovConnection()
        '''
        if not self._toPUpdated:
            for item in self._to:
                self._toProbability.extend([item]*item.priority)
            self._toPUpdated=True
        return random.choice(self._toProbability)
    def allNext(self):
        '''
        Return a list of all following Connection Objects
        :return: [MarkovConnection,...]
        '''
        return self._to
    def add_from(self,con):
        self._from.append(con)
    def add_to(self,con):
        self._to.append(con)
class MarkovConnection(object):
    '''
    A Markov Connection Object to connect 2 MarkovNode Objects.
    '''
    def __init__(self,fromMN,toMN):
        '''
        Create a Object to connect fromMN to toMN
        :param fromMN: MarkovNode()
        :param toMN: MarkovNode()
        '''
        self._from=fromMN
        self._to=toMN
        self.priority=1
        fromMN.add_to(self)
        toMN.add_from(self)
    def __lt__(self,other):
        return self.priority<other.priority
    def __gt__(self,other):
        return self.priority>other.priority
    def __eq__(self,other):
        return self.priority==other.priority
    def __le__(self,other):
        return self.priority<=other.priority
    def __ge__(self,other):
        return self.priority>=other.priority
    def __ne__(self,other):
        return self.priority!=other.priority
    def get_From(self):
        '''
        Get the previous MarkovNode Object
        :return: MarkovNode()
        '''
        return self._from
    def get_To(self):
        '''
        Get the following MarkovNode Object
        :return: MarkovNode()
        '''
        return self._to

def gen_markovModel2(filename="ggcc-saetze.txt"):
    '''
    Obsolet
    :param filename:
    :return:
    '''
    F=""
    with open(filename,"r") as f:
        F=f.read()
        f.close()
    lines=F.split("<s> ")
    StartMN=MarkovNode("")
    wordSet=set()
    i=0
    T=time.time()
    for l in lines:
        i+=1
        if i%1000==0:
            print(i,time.time()-T)
            T=time.time()
        words=l.split(" ")
        preMN=StartMN
        for w in words:
            if w in wordSet:
                MN=MarkovNode.Nodes[w]
            else:
                MN=MarkovNode(w)
                wordSet.add(w)
            #todo
            conexist=False
            for con in preMN.allNext():
                if con.get_To().name==w:
                    con.priority+=1
                    conexist=True
            if not conexist:
                MarkovConnection(preMN,MN)
            preMN=MN
    return StartMN

def gen_markovModel(filename="ggcc-saetze.txt"):
    '''
    Generate a Markov Model from a given File
    :param filename: Path
    :return: MarkovNode() (A singe start Node)
    '''
    F=""
    with open(filename,"r",encoding="utf8") as f:
        F=f.read()
        f.close()
    F=F*3
    F=F.replace("\n","").replace("\r","")
    StartMN=MarkovNode("<s>")
    words=F.split(" ")
    wordSet=set(words)
    MNdic={}
    for item in wordSet:
        MNdic[item]=MarkovNode(item)
    MNdic["<s>"]=StartMN
    connections={}
    i=0
    wl=len(words)
    while i+1<wl:
        w1,w2=words[i:i+2]
        if connections.get(w1+" "+w2):
            connections[w1+" "+w2].priority+=1
        else:
            MN1=MNdic[w1]
            MN2=MNdic[w2]
            connections[w1+" "+w2]=MarkovConnection(MN1,MN2)
        i+=1
    return StartMN

def gen_sentence(StartMarkovNode):
    '''
    Generate a Markov Chain with exactly end of a sentenc (.,!,?)
    :param StartMarkovNode: MarkovNode() (The start Node)
    :return: str
    '''
    MN=StartMarkovNode
    Text=""
    while not MN.name in (".","!","?"):
        Text+=" "+MN.name
        MN=MN.getNextRandom().get_To()
    Text+=MN.name
    return Text
def MarkovChain_as_sentence(seq):
    '''
    Extrakt a sentence of an MarkovNode() List to a Node with name (.,!,?)
    :param seq: [MarkovNode(),...]
    :return: str
    '''
    Text=""
    ignor=seq[0]
    for item in seq:
        if item != ignor:
            Text+=" "+item.name
        if Text[-1] in ".!?":
            return Text
def gen_sentence_chain(StartMarkovNode):
    '''
    Like gen_sentence
    :param StartMarkovNode:
    :return: [MarkovNode(),...]
    '''
    MN=StartMarkovNode
    Text=[]
    while not MN.name in (".","!","?"):
        Text.append(MN)
        MN=MN.getNextRandom().get_To()
    Text.append(MN)
    return Text
def gen_MarkovChain(StartMarkovNode,size=1):
    '''
    Generate a Markov Chain
    :param StartMarkovNode: MarkovNode() (The start Node)
    :param size: int (length of the Chain
    :return: [MarkovNode(),...]
    '''
    MN = StartMarkovNode
    l = []
    while len(l)<size:
        l.append(MN)
        MN = MN.getNextRandom().get_To()
    l.append(MN)
    return l

def gen_complexMarkovChain(StartMarkovNode,deep=1,resultSize=1000000):
    l=[]
    _cMC(StartMarkovNode,deep,l,resultSize=resultSize)
    return l
    pass
def _cMC(sMN,deep,fullMCList,priority=1,preChain=[],resultSize=1000000):
    l=copy.copy(preChain)
    l.append(sMN)
    if deep<=0:
        fullMCList.append((priority,l))
        if len(fullMCList)>resultSize*2:
            fullMCList.sort()
            fullMCList=fullMCList[-resultSize:]
        return
    MNCs=copy.copy(sMN.allNext())
    MNCs.sort()
    for MNC in MNCs[-(resultSize*2):]:
        _cMC(MNC.get_To(),deep-1,fullMCList,priority*MNC.priority,l,resultSize)
    

if __name__=="__main__":
    T1=time.time()
    S=gen_markovModel()
    T2=time.time()
    print("Generation Time:",T2-T1)
    L=gen_complexMarkovChain(S,2,1000)
    print(len(L),L[0])
    while True:
        print(gen_sentence(S))
        input()
