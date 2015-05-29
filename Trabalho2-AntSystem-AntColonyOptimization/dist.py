import snap

# Lista de Tuplas ( ID, Grau ) de todos os vertices do grafo G
def lstTuplasIdGrau(graph):
    return [(NI.GetId(),NI.GetDeg()) for NI in graph.Nodes()]

#Retorna o menor caminho entre dois vertices
def find_shortest_path(graph, start, end, path=[]):
    path = path + [start]
    
    if start == end:
        return path

    if not graph.has_key(start):
        return None
    
    shortest = None
    
    for node in graph[start]:
        
        if node not in path:
            newpath = find_shortest_path(graph, node, end, path)
            if newpath:
                if not shortest or len(newpath) < len(shortest):
                    shortest = newpath
                    #print shortest
                    return shortest

def main():
    
    G = snap.TUNGraph.New() # Grafo Nao direcionado

    ##########################################################
    #                                                        #
    # FASE de Inicializacao do grafo G a partir dos arquivos #
    #                                                        #
    ##########################################################

    # Le Vertices e os insere no grafo:
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

    #Cria um grafo em forma de dicionario para facilitar a implementacao do menor caminho
    listaAdjacencia = []
    graph = {}

    for NI in G.Nodes():
        print "Vertice (%d)" % (NI.GetId())
        
        for Id in NI.GetOutEdges():
            print "edge (%d)" % (Id)
            listaAdjacencia.append(Id)
                        
        a = int(NI.GetId())
        graph.update({a:listaAdjacencia})
        listaAdjacencia = [ ]

    print graph

    path2 = find_shortest_path(graph,493,494)
    
    dist = len(path2)-1
    
    print dist
    print path2

    f = open('dist', 'w')

    for i in graph:
        for j in graph:
            path2 = find_shortest_path(graph,i,j)
            print path2
            dist = len(path2)-1
            print dist
            path2 = []  
            value = dist
            s = str(value)
            f.write(s)
            f.write(' ')
        f.write('\n')
        f.close()


#    for x in graph:
#        path2 = find_shortest_path(graph,x,x+1)
#        print path2
main()