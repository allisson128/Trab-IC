import snap

# Cria grafo Nao direcionado:
G1 = snap.TUNGraph.New()

# Le Vertices e insere no grafo:
with open('vert.dat') as file:
    for line in file:
        v = line.rstrip('\n')
        G1.AddNode(int(v))
        print v 

# Le Arestas:
with open('edge.dat') as file:
    data = file.read()
    print data
print lines


# G1.AddNode(1)
# G1.AddNode(5)
# G1.AddNode(32)

# G1.AddEdge(1,5)
# G1.AddEdge(5,1)
# G1.AddEdge(5,32)

print "G1: Nodes %d, Edges %d" % (G1.GetNodes(), G1.GetEdges())

# for NI in G1.Nodes():
#     print "node id %d with out-degree %d and in-degree %d" % (NI.GetId(), NI.GetOutDeg(), NI.GetInDeg())
