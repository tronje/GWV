import random,time
#import cPickle as pickle
import copy

class MarkovNode(object):
    Nodes={}
    def __init__(self,name):
        MarkovNode.Nodes[name]=self
        self.name=name
        self._from=[]
        self._to=[]
        self._toProbability=[]
        self._toPUpdated=False
        pass
    def getNextRandom(self):
        if not self._toPUpdated:
            for item in self._to:
                self._toProbability.extend([item]*item.priority)
            self._toPUpdated=True
        return random.choice(self._toProbability)
    def allNext(self):
        return self._to
    def add_from(self,con):
        self._from.append(con)
    def add_to(self,con):
        self._to.append(con)
class MarkovConnection(object):
    def __init__(self,fromMN,toMN):
        self._from=fromMN
        self._to=toMN
        self.priority=1
        fromMN.add_to(self)
        toMN.add_from(self)
    def get_From(self):
        return self._from
    def get_To(self):
        return self._to

def gen_markovChain2(filename="ggcc-saetze.txt"):
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
    #for i in range(10):
        #print StartMN.getNextRandom().get_To().name

def gen_markovChain(filename="ggcc-saetze.txt"):
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
        if connections.has_key(w1+" "+w2):
            connections[w1+" "+w2].priority+=1
        else:
            MN1=MNdic[w1]
            MN2=MNdic[w2]
            connections[w1+" "+w2]=MarkovConnection(MN1,MN2)
        i+=1
    return StartMN

def gen_sentences(StartMarkovNode):
    MN=StartMarkovNode
    Text=""
    while not MN.name in (".","!","?"):
        Text+=" "+MN.name
        MN=MN.getNextRandom().get_To()
    Text+=MN.name
    return Text
def MarkovChain_as_sentence(seq):
    Text=""
    ignor=seq[0]
    for item in seq:
        if item != ignor:
            Text+=" "+item.name
        if Text[-1] in ".!?":
            return Text
def gen_sentences_chain(StartMarkovNode):
    MN=StartMarkovNode
    Text=[]
    while not MN.name in (".","!","?"):
        Text.append(MN)
        MN=MN.getNextRandom().get_To()
    Text.append(MN)
    return Text
def gen_complexMarkovChain(StartMarkovNode,deep=1):
    l=[]
    _cMC(StartMarkovNode,deep,l)
    return l
    pass
def _cMC(sMN,deep,fullMCList,priority=1,preChain=[],resultSize=1000):
    l=copy.copy(preChain)
    l.append(sMN)
    if deep<=0:
        fullMCList.append((priority,l))
        if len(fullMCList)>resultSize*2:
            fullMCList.sort()
            fullMCList=fullMCList[resultSize:]
        return
    for MNC in sMN.allNext():
        _cMC(MNC.get_To(),deep-1,fullMCList,priority*MNC.priority,l)
    #print len(fullMCList)
    

if __name__=="__main__":
    T1=time.time()
    S=gen_markovChain()
    T2=time.time()
    print("Generation Time:",T2-T1)
    L=gen_complexMarkovChain(S,4)
    print(len(L))
    print(L[0])
    while True:
        print(gen_sentences(S))
        raw_input()
