import snap

def ffitness (Graph):
    return 2.*Graph.GetEdges()/((Graph.GetNodes()-1)*Graph.GetNodes())

# Lista de Tuplas ( ID, Grau ) de todos os vertices do grafo G
def lstTuplasIdGrau(graph):
    return [(NI.GetId(),NI.GetDeg()) for NI in graph.Nodes()]

# Recebe uma lista de n grafos e os mostra na tela, com sua densidade
def showEachGroup(listaDeGrafos):
    for g in listaDeGrafos:
        print [f.GetId() for f in g.Nodes()], ffitness(g)

def lstDensidadeGrafos(listaDeGrafos):
    return [ffitness(g) for g in listaDeGrafos]
        

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
    print ffitness(G)


    ########################################################
    #                                                      #
    # Divisao do Grafo em 6 Grupos, para aplicacao de Rank #
    #                                                      #
    ########################################################
    #   Cada grupo tera 20 elementos (vertices). Portanto  #
    # selecionando um total de 120 elementos, dentre os 224#
    ########################################################

    # Lista de grafos, onde cada um sera um dos grupos:
    lstGrupoGrafo = [snap.TUNGraph.New() for g in range(0,6)] #6 grupos, onde cada grupo eh um subgrafo Gi
    # Lista de Listas com os nos dos grafos. 
    lstGrupo = [] # Serao 6 grupos, onde cada grupo serah uma sublista
    # Lista de Tuplas ( ID, Grau ) de todos os vertices do grafo G
    lstIdGrau = lstTuplasIdGrau(G)
    # Mesma lista, ordenada por grau
    lstIdGrauOrdenada = sorted(lstIdGrau, key=lambda grau: grau[1])
    # Lista para armazenar Vetor de Inteiros da biblioteca Snap, com os vertices de cada grupo 
    SNAPIntVet = []

    # Gera a Lista de Listas com os nos dos grafos. 
    for i in range(0,6):
        lstGrupo.append([])
        SNAPIntVet.append(snap.TIntV())
        for j in range(0,20):
            lstGrupo[i].append( (lstIdGrauOrdenada[j + i * 20])[0] )
            SNAPIntVet[i].Add(  (lstIdGrauOrdenada[j + i * 20])[0] )
            # lstGrupo[i].AddNode((lstIdGrauOrdenada[j + i*20])[0])

    # Transforma as listas em Grafos, preservando ate as arestas originais
    for i in range(0,6):
        lstGrupoGrafo[i] = snap.GetSubGraph(G, SNAPIntVet[i])

    # Mostra as Listas com os nos de cada grupo (subgrafo) e sua densidade
    showEachGroup(lstGrupoGrafo)
    print max(lstDensidadeGrafos(lstGrupoGrafo), key=float)
    
    #############################################################  
    #                                              --->Fim      #  
    #                                              |            #
    #Iteracao entre todas as fases do AG: Ini--->Aval->Sel->Rec #  
    #                                              ^         |  #  
    #                                              |_________|  #  
    #############################################################  
    for it in range(0,20): #Limite de 20 iteracoes

        #########################################################
        #                   FASE de Avaliacao                   #
        #     Verfica se a funcao fitness eh maior ou igual ao  #
        # resultado esperado. Se Sim, retorna o grafo, se nao   #
        # continua para as demais fases.                        #
        #########################################################
        
        ########### Grafo de Maior Densidade ####################
        maior = segundoMaior = 0
        indiceMaior = indiceSegundoMaior = 0
        count = 0
        for g in lstGrupoGrafo:
            nota = ffitness(g) 
            if nota > maior :
                segundoMaior = maior
                maior = nota
                indiceMaior = indiceSegundoMaior = count
            elif nota > segundoMaior:
                segundoMaior = nota
                indiceSegundoMaior = count
            count = count + 1

        print maior, indiceMaior, segundoMaior, indiceSegundoMaior

        ########### Grafo de Menor Densidade ####################
        menor = segundoMenor = 2
        indiceMenor = indiceSegundoMenor = 0
        count = 0
        for g in lstGrupoGrafo:
            nota = ffitness(g) 
            if nota < menor :
                segundoMenor = menor
                menor = nota
                indiceMenor = indiceSegundoMenor = count
                
            elif nota < segundoMenor:
                segundoMenor = nota
                indiceSegundoMenor = count
            count = count + 1

        print menor, indiceMenor, segundoMenor, indiceSegundoMenor


        #########################################################
        #                   FASE de Selecao                     #
        #     Verfica se a funcao fitness eh maior ou igual ao  #
        # resultado esperado. Se Sim, retorna o grafo, se nao   #
        # continua para as demais fases.                        #
        #########################################################

        #########################################################
        #FASE 3: Selecao -> 6 grupos dos melhores 20 elementos (nos)
        
        
        
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

