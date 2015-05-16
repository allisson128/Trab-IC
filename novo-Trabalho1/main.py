import snap
import random


def bin2graph(lstbin, lstids, graph):

    SNAPIntVet = snap.TIntV()
    for i in range(0, len(lstids)):
        if lstbin[i] == 1:
            SNAPIntVet.Add(int(lstids[i]))
    return snap.GetSubGraph(graph, SNAPIntVet) 

def ffitness (Graph):
    return 2.*Graph.GetEdges()/((Graph.GetNodes()-1)*Graph.GetNodes())
    # return Graph.GetNodes() * 2.*Graph.GetEdges()/((Graph.GetNodes()-1)*Graph.GetNodes())

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
    
    populationSize = 300
    G = snap.TUNGraph.New() # Grafo Nao direcionado
    lstTotalIds = []
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
            lstTotalIds.append(v)
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
    # lstGrupoGrafo = [snap.TUNGraph.New() for g in range(0,6)] #6 grupos, onde cada grupo eh um subgrafo Gi

    # Population de Solucoes
    population = []

    # Lista de Listas com os nos dos grafos. 
    lstGrupos = [] # Serao 6 grupos, onde cada grupo serah uma sublista

    # Lista de Tuplas ( ID, Grau ) de todos os vertices do grafo G
    # lstIdGrau = lstTuplasIdGrau(G)

    # Mesma lista, ordenada por grau
    # lstIdGrauOrdenada = sorted(lstIdGrau, key=lambda grau: grau[1], reverse=True)

    ###### print lstIdGrauOrdenada
    # Lista para armazenar Vetor de Inteiros da biblioteca Snap, com os vertices de cada grupo 
    SNAPIntVet = []

    # Gera a Lista de Listas com os nos dos grafos. 
    # for i in range(0,6):
    #     lstGrupo.append([])
    #     SNAPIntVet.append(snap.TIntV())
    #     for j in range(0,20):
    #         lstGrupo[i].append( (lstIdGrauOrdenada[j + i * 20])[0] )
    #         SNAPIntVet[i].Add(  (lstIdGrauOrdenada[j + i * 20])[0] )
    #         # lstGrupo[i].AddNode((lstIdGrauOrdenada[j + i*20])[0])

    # Gera a Population aleatoria
    for i in range(0,populationSize):
        population.append([])
        for j in range(0,len(lstTotalIds)):
            population[i].append( random.randint(0,1) )

    #############################################################  
    #                                              --->Fim      #  
    #                                              |            #
    #Iteracao entre todas as fases do AG: Ini--->Aval->Sel->Rec #  
    #                                              ^         |  #  
    #                                              |___Mut___|  #  
    #############################################################  

    flag = 0 #indica se saiu do loop com fracasso

    for it in range(0,1): #Limite de 20 iteracoes

        #########################################################
        #                   FASE de Avaliacao                   #
        #     Verfica se a funcao fitness eh maior ou igual ao  #
        # resultado esperado. Se Sim, retorna o grafo, se nao   #
        # continua para as demais fases.                        #
        #########################################################
        
        # Mostra as Listas com os nos de cada grupo (subgrafo) e sua densidade
        # showEachGroup(lstGrupoGrafo)


        vetnotas = []
        for i in range(0,populationSize):
            vetnotas.append( ffitness( bin2graph(population[i], lstTotalIds, G) ) )

        print vetnotas
        maior = max(vetnotas)
        indiceMaior = vetnotas.index(maior)

        ########### Grafo de Maior Densidade ####################
        # maior = segundoMaior = 0
        # indiceMaior = indiceSegundoMaior = 0
        # count = 0
        # for g in lstGrupoGrafo:
        #     nota = ffitness(g) 
        #     if nota > maior :
        #         segundoMaior = maior
        #         maior = nota
        #         indiceMaior = indiceSegundoMaior = count
        #     elif nota > segundoMaior:
        #         segundoMaior = nota
        #         indiceSegundoMaior = count
        #     count = count + 1

        ##### print maior, indiceMaior, segundoMaior, indiceSegundoMaior

        ########### Grafo de Menor Densidade ####################
        # menor = segundoMenor = 2
        # indiceMenor = indiceSegundoMenor = 0
        # count = 0
        # for g in lstGrupoGrafo:
        #     nota = ffitness(g) 
        #     if nota < menor :
        #         segundoMenor = menor
        #         menor = nota
        #         indiceMenor = indiceSegundoMenor = count
                
        #     elif nota < segundoMenor:
        #         segundoMenor = nota
        #         indiceSegundoMenor = count
        #     count = count + 1

        ##### print menor, indiceMenor, segundoMenor, indiceSegundoMenor

        ########################################################
        #               Condicoes de Parada                    #
        ########################################################
        if maior == 1:
            print 'GOAL'
            flag = 1
            break
        elif it > 20 and maior > .9:
            print ''
            print 'Resultado Aceitavel na iteracao ', it
            print 'Subgrafo correspondente: '
            print lstTotalIds[indiceMaior]
            print 'Densidade do grafo', maior, ' no indice ', indiceMaior
            flag = 1
            break

        #########################################################
        #                   FASE de Selecao                     #
        #     Verfica se a funcao fitness eh maior ou igual ao  #
        # resultado esperado. Se Sim, retorna o grafo, se nao   #
        # continua para as demais fases.                        #
        #########################################################

        # Ranqueamento, em ordem Decrescente de Grau
        lista = []
        novaLstGrupo = []
        for g in lstGrupoGrafo:
            for h in g.Nodes():
                lista.append( (h.GetId(), G.GetNI(h.GetId()).GetDeg()) )
        ##### print lista

        
        lstIdGrauOrdenada = sorted(lista, key=lambda grau: grau[1], reverse=True)
        # print lstIdGrauOrdenada
        # Lista para armazenar Vetor de Inteiros da biblioteca Snap, com os vertices de cada grupo 
        lstGrupo = [] 
        SNAPIntVet = []

        # Gera a Lista de Listas com os nos dos grafos. 
        for i in range(0,6):
            lstGrupo.append([])
            SNAPIntVet.append(snap.TIntV())
            for j in range(0,20):
                lstGrupo[i].append( (lstIdGrauOrdenada[j + i * 20])[0] )
                SNAPIntVet[i].Add(  (lstIdGrauOrdenada[j + i * 20])[0] )
                # lstGrupo[i].AddNode((lstIdGrauOrdenada[j + i*20])[0])
        #print lstGrupo

        # Transforma as listas em Grafos, preservando ate as arestas originais
        for i in range(0,6):
            lstGrupoGrafo[i] = snap.GetSubGraph(G, SNAPIntVet[i])

        #showEachGroup(lstGrupoGrafo)

        #########################################################
        #             FASE de Recombinacao (cruzamento)         #
        #    Usando ponto fixo na metade do grafo, de 2 em 2    #
        #########################################################
        
        count = 0
        for g in lstGrupo:
            if count % 2 == 0:
                A = g[0:10]
                B = g[10:20]
            else :
                C = g[0:10]
                D = g[10:20]
                #print ''
                novaLstGrupo.append( A+D )
                novaLstGrupo.append( C+B )

            count = count + 1
            
        # print ''
        # print novaLstGrupo

        #########################################################
        #                     FASE de Mutacao                   #
        #                                                       #
        #########################################################

        primeiroGrupo = random.randint(0, 5)
        segundoGrupo = random.randint(0, 5)
        primeiroElemento = random.randint(0, 19)
        segundoElemento = random.randint(0, 19)
        
        # print ''
        # print primeiroGrupo, segundoGrupo, primeiroElemento, segundoElemento
        # print ''
        temp = novaLstGrupo[primeiroGrupo][primeiroElemento]
        novaLstGrupo[primeiroGrupo][primeiroElemento] = novaLstGrupo[segundoGrupo][segundoElemento]
        novaLstGrupo[segundoGrupo][segundoElemento] = temp
            

        # Lista para armazenar Vetor de Inteiros da biblioteca Snap, com os vertices de cada grupo 
        SNAPIntVet = []
        lstGrupo = []
        # Gera a Lista de Listas com os nos dos grafos. 
        for i in range(0,6):
            lstGrupo.append([])
            SNAPIntVet.append(snap.TIntV())
            for j in range(0,20):
                lstGrupo[i].append( novaLstGrupo[i][j] )
                SNAPIntVet[i].Add(  novaLstGrupo[i][j] )
                # lstGrupo[i].AddNode((lstIdGrauOrdenada[j + i*20])[0])

        # Transforma as listas em Grafos, preservando ate as arestas originais
        #lstGrupoGrafo = []
        for i in range(0,6):
            lstGrupoGrafo[i] = snap.GetSubGraph(G, SNAPIntVet[i])

        # Mostra as Listas com os nos de cada grupo (subgrafo) e sua densidade
        
    if not flag :
        print ''
        print 'Resultado na iteracao ', it
        print 'Subgrafo correspondente: '
        print lstGrupo[indiceMaior]
        print 'Densidade do maior grafo atingido: ', maior


main()

