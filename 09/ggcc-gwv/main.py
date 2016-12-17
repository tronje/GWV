from markov import *

if __name__=="__main__":
    print("Start generation of Markov Chain ...")
    T1=time.time()
    S=gen_markovModel()
    T2=time.time()
    print("Generation Time:",T2-T1)
    while True:
        print(gen_sentence(S))
        input()
