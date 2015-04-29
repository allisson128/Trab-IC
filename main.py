import snap

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
#    print dupla
    G1.AddEdge(int(dupla[0]), int(dupla[1]))

print "G1: Nodes %d, Edges %d" % (G1.GetNodes(), G1.GetEdges())

# for NI in G1.Nodes():
#     print "node id %d with out-degree %d and in-degree %d" % (NI.GetId(), NI.GetOutDeg(), NI.GetInDeg())
