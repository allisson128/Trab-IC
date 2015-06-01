import snap
import random
import sys

def bin2graph(lstbin, lstids, graph):

    SNAPIntVet = snap.TIntV()
    for i in range(0, len(lstids)):
        if lstbin[i] == 1:
            SNAPIntVet.Add(int(lstids[i]))
    return snap.GetSubGraph(graph, SNAPIntVet) 

def ffitness (Graph):
    return 2.*Graph.GetEdges()/((Graph.GetNodes()-1)*Graph.GetNodes())

# def lstDensidadeGrafos(listaDeGrafos):
#     return [ffitness(g) for g in listaDeGrafos]

def main():
    

    ##########################################################
    # Variaveis de Configuracao
    ##########################################################
    #
    nroCandidatos = 800 #Populcao de solucoes candidatas
    grupoSize = 10
    pfixoflag = 1 #1 para um ponto fixo, caso contrario usara dois pontos fixos
    rank = True
    mutRate = 0.01 #percentual de vezes  que ocorre mutacao, em cima de nroCandidatos
    #
    ##########################################################

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

    # Le e grava Arestas no grafo:
    lines = [line.strip() for line in open('edge.dat')]
    for e in lines:
        dupla = e.split()
        G.AddEdge(int(dupla[0]), int(dupla[1]))

    # print "G: Nodes %d, Edges %d" % (G.GetNodes(), G.GetEdges())
    # print ffitness(G)

    ########################################################
    #                                                      #
    # Criacao de solucoes candidatas aleatorias            #
    #                                                      #
    ########################################################
    #   A var. 'nroCandidatos' indica a qtd de solucoes   #
    # candidatas (subgrafos) criados para iniciar o algor. #
    # Serao representadas por lista com 224 elementos (nro #
    # de nos) binarios. 1 caso o respectivo indice esteja  #
    # presente na solucao e 0 caso contrario.              #
    ########################################################

    lstCandidatos = []
    novosCandidatos = []
    lstGrupos = []
    grupo = []

    # Lista para armazenar Vetor de Inteiros da biblioteca Snap, com os vertices de cada grupo 
    SNAPIntVet = []

    # Gera a solucoes candidatas aleatorias
    for i in range(0,nroCandidatos):
        lstCandidatos.append([])
        for j in range(0,len(lstTotalIds)):
            lstCandidatos[i].append( random.randint(0,1) )

    #############################################################  
    #                                              --->Fim      #  
    #                                              |            #
    #Iteracao entre todas as fases do AG: Ini--->Aval->Sel->Rec #  
    #                                              ^         |  #  
    #                                              |___Mut___|  #  
    #############################################################  

    for it in range(0,100000): #Limite de 20 iteracoes

        #########################################################
        #                   FASE de Avaliacao                   #
        #     Verfica se a funcao fitness eh maior ou igual ao  #
        # resultado esperado. Se Sim, retorna o grafo, se nao   #
        # continua para as demais fases.                        #
        #########################################################
        
        # Mostra as Listas com os nos de cada grupo (subgrafo) e sua densidade
        # showEachGroup(lstGrupoGrafo)


        vetnotas = []
        for i in range(0,nroCandidatos):
            vetnotas.append( ffitness( bin2graph(lstCandidatos[i], lstTotalIds, G) ) )


        maior = max(vetnotas)
        print maior
        indiceMaior = vetnotas.index(maior)



        ########################################################
        #               Condicoes de Parada                    #
        ########################################################
        if maior == 1:
            print ''
            print 'GOAL'
            break

        elif it > 1500:
            break


        #########################################################
        #                   FASE de Selecao                     #
        #     Agrupa os elementos de 10 em 10 ate o valor total #
        # de candidatos ser atingido.                           #
        #########################################################



        novosCandidatos = []
        lstGrupos = []
        j = -1
        # grupoSize = 10 -> tamanho de cada grupo
        for i in range(0,nroCandidatos):
            if i % grupoSize == 0:
                j = j + 1
                lstGrupos.append([])
            lstGrupos[j].append(lstCandidatos[i])


        for grupo in lstGrupos:

            ########### Acha os dois piores ####################
            menor = segundoMenor = 1000
            indiceMenor = indiceSegundoMenor = 0
            count = 0
            for g in grupo:
                nota = ffitness(bin2graph(g,lstTotalIds, G))
                if nota < menor :
                    segundoMenor = menor
                    indiceSegundoMenor = indiceMenor
                    menor = nota
                    indiceMenor = count
            
                elif nota < segundoMenor:
                    segundoMenor = nota
                    indiceSegundoMenor = count
                count = count + 1


            ########### Acha os dois melhores ####################
            maior = segundoMaior = indiceMaior = indiceSegundoMaior = 0
            count = 0
            
            for g in grupo:
                nota = ffitness(bin2graph(g,lstTotalIds, G))
                if nota > maior :
                    segundoMaior = maior
                    indiceSegundoMaior = indiceMaior
                    maior = nota
                    indiceMaior = count
                elif nota > segundoMaior:
                    segundoMaior = nota
                    indiceSegundoMaior = count
                count = count + 1


            #########################################################
            #             FASE de Recombinacao (Cruzamento)         #
            #    Usando ponto fixo aletorio no grafo, de 2 em 2 elem#
            #########################################################

            k = -1
            l = grupoSize
            
            # Insere os novos candidatos recombinados  no novo Grupo 
            # eliminando os 2 piores elementos
            if rank:
                iteracoes = (grupoSize/2) - 1
            else:
                iteracoes = (grupoSize/2)

            for i in range(0,iteracoes):

                pfixoUm = random.randint(1,223)


                # Determina se o ponto fixo sera unico, ou nao
                if pfixoflag == 1:
                    pfixoDois = pfixoUm
                else:
                    pfixoDois = random.randint(1,223)

                k = k + 1
                if rank:
                    while k == indiceMenor or k == indiceSegundoMenor:
                        k = k + 1
                candidatoUm = grupo[k]

                l = l - 1
                if rank:
                    while l == indiceMenor or l == indiceSegundoMenor:
                        l = l - 1
                candidatoDois = grupo[l]

                novoCandidatoUm = []
                novoCandidatoDois = []

                for m in range(0,pfixoUm):
                    novoCandidatoUm.append(candidatoUm[m])
                    novoCandidatoDois.append(candidatoDois[m])

                for m in range(pfixoUm, pfixoDois):
                    novoCandidatoUm.append(candidatoDois[m])
                    novoCandidatoDois.append(candidatoUm[m])

                for m in range(pfixoDois, G.GetNodes()):
                    novoCandidatoUm.append(candidatoUm[m])
                    novoCandidatoDois.append(candidatoDois[m])

                novosCandidatos.append(novoCandidatoUm)
                novosCandidatos.append(novoCandidatoDois)
            novosCandidatos.append(grupo[indiceMaior])
            novosCandidatos.append(grupo[indiceSegundoMaior])

        random.shuffle(novosCandidatos)

        #########################################################
        #                     FASE de Mutacao                   #
        #                                                       #
        #########################################################
        for i in range(0,int(mutRate*nroCandidatos)):
            randA = random.randint(0, nroCandidatos-1)
            randB = random.randint(0, G.GetNodes()-1)
            
            valor = (novosCandidatos[randA])[randB]
            if valor == 0:
                novosCandidatos[randA][randB] = 1
            else:
                novosCandidatos[randA][randB] = 0
        #########################################################

        lstCandidatos = novosCandidatos


        
    # Cai aqui caso nao chegue nos valores desejados
    print ''
    print 'Resultado na iteracao ', it
    print 'Subgrafo correspondente: '
    print lstCandidatos[indiceMaior]
    print 'Densidade do grafo', maior, ' no indice ', indiceMaior

    labels = snap.TIntStrH()
    for NI in G.Nodes():
        labels[NI.GetId()] = str(NI.GetId())
    print 'Grafo.png'
    snap.DrawGViz(bin2graph(lstCandidatos[indiceMaior],lstTotalIds, G), snap.gvlDot, "grafo.png", "subgrafo de densidade = 1", labels)



main()

