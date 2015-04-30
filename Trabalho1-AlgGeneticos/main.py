import snap

def ffitness (Graph):
    return 2.*Graph.GetEdges()/((Graph.GetNodes()-1)*Graph.GetNodes())

def main():
    # Cria grafo Nao direcionado:
    G = snap.TUNGraph.New()

    # Le Vertices e insere no grafo:
    with open('vert.dat') as file:
        for line in file:
            v = line.rstrip('\n')
            G.AddNode(int(v))
            # print v 

    # Le e grava Arestas no grafo:
    lines = [line.strip() for line in open('edge.dat')]
    #print lines
    for e in lines:
        dupla = e.split()
        G.AddEdge(int(dupla[0]), int(dupla[1]))
        #print dupla


    print "G: Nodes %d, Edges %d" % (G.GetNodes(), G.GetEdges())
    print ffitness(G)

    ####################################################
    #FASE: Selecao -> 6 grupos dos melhores 20 elementos (nos)

    # Lista de grafos, onde cada um sera um dos grupos:
    lstGrupo = [snap.TUNGraph.New() for g in range(0,6)] #6 grupos, onde cada grupo eh um subgrafo Gi
        
    # Lista de Tuplas ( ID, Grau ) de todos os vertices
    lstIdGrau = [(NI.GetId(),NI.GetDeg()) for NI in G.Nodes()]
    # Mesma lista, ordenada por grau
    lstIdGrauOrdenada = sorted(lstIdGrau, key=lambda grau: grau[1])

    # Popula os 20 grupos com os melhores elementos (em ordem decrescente de grau)
    for i in range(0,6):
        for j in range(0,20):
            lstGrupo[i].AddNode((lstIdGrauOrdenada[j + i*20])[0])
        
    # Listas com os nos de cada grupo
    for g in lstGrupo:
        print [f.GetId() for f in g.Nodes()]

        
        
#        print "node id %d with degree %d" % (NI.GetId(), NI.GetDeg())
    # for EI in G.Edges():
    #     print "edge (%d, %d)" % (EI.GetSrcNId(), EI.GetDstNId())
    # Graph = snap.GenRndGnm(snap.PNGraph, 50, 500)
    # nodes = snap.TIntV()
    # for N in Graph.GetNI(0).GetOutEdges():
    #     print N
    #      nodes.Add(N)
    #print nodes



main()

