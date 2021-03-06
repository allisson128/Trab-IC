############################################
# Trabalho de Inteligencia Computacional
# PSO - Otimizacao por Enxame de Particulas
# Grupo: Allisson Garcia e Vitor Borges
# DATA: 06/06/2015
############################################

import sys
import random
import math
import time
import numpy as np
import pylab as pl
def cost(x1,x2): #Rosenbrock Function:
    
    inf = 5000

    # Teste de valores fora do dominio
    if x1 > 3 or x1 < -3:
        print 'fora dos LIMITES'
        sys.exit()
    if x2 > 3 or x2 < -3:
        print 'fora dos LIMITES'
        sys.exit()

    # Acima de 2, considerar um valor constante
    if x1 > 2 or x1 < -2:
        return inf
    if x2 > 2 or x2 < -2:
        return inf
    #return 100 * (x2 - x1**2) + (x1 - 1)**2
    return (1 - x1)**2 + 100 *(x2 - x1**2)**2



def main(argv):

    ini = time.time()

    # Restricoes de implementacao:
    tolerancia = 0.001
    iteracoes = 10000
    inf = 500000 

    # Restricoes do enunciado:
    topologia = 1 #1 -> anel e 0 -> estrela
    S = 10              #numero de particulas
    X = velocmax = 0.2
    alfa = 0.5         # inercia
    
    rp = 1             # coef aceleracao melhor local
    rg = 1             # coef aceleracao melhor global
    fi_p = 0 # aleatorio # = random.uniform(0,1)
    fi_g = 0 # aleatorio # = random.uniform(0,1)
    # print 'fi_p = ', fi_p
    # print 'fi_g = ', fi_g
    dimensoes = 2
    minedge = -3.
    maxedge = 3.
    maxconstedge = 2.
    minconstedge = -2.
    x = []             #vetor (matriz) de posicoes
    v = []             #vetor (matriz) de velocidades
    p = []             #melhor solucao local de cada particula
    pcost = []
    g = [inf, inf]
    gcost = inf
    ghist = [] #historico do 'melhore global' do enxame

    anel = []
    anelcost = []

    for i in range(0, S):

        x.append([random.uniform(minconstedge,maxconstedge), 
                  random.uniform(minconstedge,maxconstedge)])
        p.append(x[i])
        anel.append(p[i])
        pcost.append(cost(x[i][0], x[i][1]))
        anelcost.append(pcost[i])

        if cost(p[i][0], p[i][1]) < gcost:
            g[0] = p[i][0]
            g[1] = p[i][1]
            gcost = cost(g[0], g[1])
            # ghist.append(gcost)
        # print 'xi'
        # print x[i]
        # print cost(x[i][0], x[i][1])

        if velocmax == 0:
            v.append([random.uniform(-abs(maxedge-minedge), 
                                      abs(maxedge-minedge)),
                      random.uniform(-abs(maxedge-minedge), 
                                      abs(maxedge-minedge))])
        else:
            v.append([random.uniform(-1 * velocmax, 
                                          velocmax),
                      random.uniform(-1 * velocmax, 
                                          velocmax)])


    pl.ylabel('Eixo y')
    pl.xlabel('Eixo x')
    pl.axis([-3,3,-3,3])
    pl.plot([x[i][0] for i in range(0,S)],[x[i][1] for i in range(0,S)], 'ro')
    pl.show()


    it = 0
    while gcost > tolerancia and it < iteracoes:

        for i in range(0,S):

            if fi_p == 0 and fi_g == 0:
                fi_p = random.uniform(0,1)
                fi_g = random.uniform(0,1)

            for d in range(0, dimensoes):

                if topologia == 1: #anel
                    v[i][d] = X * (alfa * v[i][d] + rp * fi_p * (p[i][d] - x[i][d]) + rg * fi_g * (anel[i][d] - x[i][d]) )
                else: #global
                    v[i][d] = X * (alfa * v[i][d] + rp * fi_p * (p[i][d] - x[i][d]) + rg * fi_g * (g[d] - x[i][d]) )
                # if v[i][d] > velocmax:
                #     v[i][d] = velocmax
                    #print 'Velocidade MAX ultrapassada'
                x[i][d] = x[i][d] + v[i][d]

            if cost(x[i][0], x[i][1]) < pcost[i]:
                p[i][0] = x[i][0]
                p[i][1] = x[i][1]
                pcost[i] = cost(p[i][0], p[i][1])

                if cost(p[i][0], p[i][1]) < gcost:
                    g[0] = p[i][0]
                    g[1] = p[i][1]
                    gcost = cost(g[0], g[1])
                    ghist.append(gcost)
                if topologia == 1: #anel
                    for j in range(0,S):
                        indicemenor = (S+j+1)%S
                        if pcost[(S+j)%S] < pcost[indicemenor]:
                            indicemenor = (S+j)%S
                        if pcost[(S+j-1)%S] < pcost[indicemenor]:
                            indicemenor = (S+j-1)%S
                        anel[j] = p[indicemenor]
                        anelcost[j] = pcost[indicemenor]
                    
        it = it + 1

    print 'global'
    print g, cost(g[0], g[1])

    #print  argv
    fim = time.time()
    tempo = fim - ini
    # print 'tempo = ', tempo
    ## print [p[i][0] for i in range(0,S)]
    # print 'passo = ', (tempo)/(len(ghist)-1)
    # print np.arange(0,tempo,(tempo)/(len(ghist)-1))
    # print np.arange(0,tempo,(len(ghist)-1))
    # print 'ghist', len(ghist)

    pl.ylabel('Eixo y')
    pl.xlabel('Eixo x')
    # pl.axis([-3,3,-3,3])
    print [p[i][0] for i in range(0,S)]
    print [p[i][1] for i in range(0,S)]
    pl.plot([p[i][0] for i in range(0,S)],[p[i][1] for i in range(0,S)], 'ro')
    pl.show()


    pl.ylabel('Funcao custo')
    pl.xlabel('Iteracoes')
    pl.plot(ghist)

    pl.show()
main(sys.argv)
