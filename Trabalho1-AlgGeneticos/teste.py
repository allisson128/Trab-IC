import snap
import matplotlib.pyplot as plt

def ffitness (Graph):
    return 2.*Graph.GetEdges()/((Graph.GetNodes()-1)*Graph.GetNodes())

def main():
    # Cria grafo Nao direcionado:
    G1 = snap.TUNGraph.New()

    # Le Vertices e insere no grafo:
    with open('vert.dat') as file:
        for line in file:
            v = line.rstrip('\n')
            G1.AddNode(int(v))
            # print v 

    # Le e grava Arestas no grafo:
    lines = [line.strip() for line in open('edge.dat')]
    #print lines
    for e in lines:
        dupla = e.split()
        G1.AddEdge(int(dupla[0]), int(dupla[1]))
        #print dupla


    print "G1: Nodes %d, Edges %d" % (G1.GetNodes(), G1.GetEdges())
    print ffitness(G1)

    lines = [(NI.GetId(),NI.GetDeg()) for NI in G1.Nodes()]
    lines = sorted(lines, key=lambda grau: grau[1])
    print lines
#        print "node id %d with degree %d" % (NI.GetId(), NI.GetDeg())
    # for EI in G1.Edges():
    #     print "edge (%d, %d)" % (EI.GetSrcNId(), EI.GetDstNId())
    # Graph = snap.GenRndGnm(snap.PNGraph, 50, 500)
    # nodes = snap.TIntV()
    # for N in Graph.GetNI(0).GetOutEdges():
    #     print N
    #      nodes.Add(N)
    #print nodes



main()

