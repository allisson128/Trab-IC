import pygame
#import math
from math import *


# DEFINICAO DAS VARIAVEIS

# Definicao dos Angulos ----------------------------

# Angulo de 30 graus = 0.52 Radianos
# Angulo de 60 graus = 1.05 Radianos
angulo30graus = 0.52
angulo60graus = 1.05

anguloMuitoPositivo = (angulo30graus, angulo60graus)

anguloPositivo = (0.0, angulo30graus)

anguloEquilibrado = (-angulo30graus,angulo30graus)

anguloNegativo = (-angulo30graus, 0.0)

anuguloMuitoNegativo = (-angulo60graus,-angulo30graus)

# Definicao da Velocidade Angular --------------------------

velocidadeAngularPositiva = ( 0.0, angulo30graus) 
velocidadeAngularEquilibrada = (-angulo30graus, 0.0, angulo30graus)
velocidadeAngularNegativa = (-angulo30graus, 0.0)

# Definicao da Distancia -----------------------------------

distanciaPositiva = (0.0, 7.0)
distanciaCentralizada = (-7.0, 0.0, 7.0)
distanciaNegativa = (-7.0, 0.0)

# Definicao da Forca Angular -------------------------------

forcaMuitoPositiva = (80.0, 150.0)

forcaPositiva = (0.0, 80.0 , 150.0)

forcaEquilibrada = (-80.0, 0.0 , 80.0)

forcaNegativa = (-150.0, -80.0 , 0.0)

forcaMuitoNegativa = (-150.0 , -80.0 )

# Fuzzificao das variaveis de ambiente

def anguloFuzzificacao(angulo):

        # Variaveis de controle que define o quanto a qual conjunto este pertence
        aMPos = aPos = aEq = aNeg = aMNeg =  0.0

        #Participacao do angulo a em ser um anguloMuitoPositivo
        if ( angulo >= anguloMPos[1] ):
                aMPos = 1.0

        elif ( anguloMPos[0] < angulo <= anguloMPos[1] ):
                aMPos = ( angulo - anguloMPos[0] ) / ( anguloMPos[1] - anguloMPos[0] ) 

        #Participacao do angulo a em ser um anguloPositivo
        if ( angulo == anguloPos[1] ):
                aPos = 1.0

        elif ( anguloPos[0] < angulo <= anguloPos[1] ):
                aPos = ( angulo - anguloPos[0] ) / ( anguloPos[1] - anguloPos[0] )

        elif ( anguloPos[1] <= angulo < anguloPos[2] ):
                aPos = ( angulo - anguloPos[2] ) / ( anguloPos[1] - anguloPos[2] )


        #Participacao do angulo a em ser um anguloEquilibrado
        if ( angulo == anguloEq[1] ):
                aEq = 1.0

        elif ( anguloEq[0] < angulo <= anguloEq[1] ):
                aEq = ( angulo - anguloEq[0] ) / ( anguloEq[1] - anguloEq[0] )

        elif ( anguloEq[1] <= angulo < anguloEq[2] ):
                aEq = ( angulo - anguloEq[2] ) / ( anguloEq[1] - anguloEq[2] )


        #Participacao do angulo a em ser um anguloNegativo
        if ( angulo == anguloNeg[1] ):
                aNeg = 1.0

        elif ( anguloNeg[0] < angulo <= anguloNeg[1] ):
                aNeg = ( angulo - anguloNeg[0]) / (anguloNeg[1] - anguloNeg[0] )

        elif ( anguloNeg[1] <= angulo < anguloNeg[2] ):
                aNeg = ( angulo - anguloNeg[2] ) / ( anguloNeg[1] - anguloNeg[2] )


        #Participacao do angulo a em ser um anguloMuitoNegativo
        if ( angulo <= anguloMNeg[0] ):
                aMNeg = 1.0

        elif ( anguloMNeg[0] <= angulo < anguloMNeg[1] ):
                aMNeg = ( angulo - anguloMNeg[1] ) / ( anguloMNeg[0] - anguloMNeg[1] )
        

        
        return aMPos, aPos, aEq, aNeg, aMNeg 


def velocidadeAFuzzificacao(velocidade):

        # Variaveis de controle que define o quanto a qual conjunto este pertence
        vPos = vEq = vNeg = 0.0

        if ( velocidade >= velocidadeAngularPos[1] ):
                vPos = 1.0

        elif ( velocidadeAngularPos[0] < velocidade <= velocidadeAngularPos[1] ):
                vPos = ( velocidade - velocidadeAngularPos[0] ) / ( velocidadeAngularPos[1] - velocidadeAngularPos[0] )

        if ( velocidade == velocidadeAngularEq[1] ):
                vEq = 1.0

        elif ( velocidadeAngularEq[0] < velocidade <= velocidadeAngularEq[1] ):
                vEq = ( velocidade - velocidadeAngularEq[0] ) / ( velocidadeAngularEq[1] - velocidadeAngularEq[0] )

        elif ( velocidadeAngularEq[1] <= velocidade < velocidadeAngularEq[2] ):
                vEq = ( velocidade - velocidadeAngularEq[2] ) / ( velocidadeAngularEq[1] - velocidadeAngularEq[2] )

        if ( velocidade <= velocidadeAngularNeg[0] ):
                vNeg = 1.0

        elif ( velocidadeAngularNeg[0] <= velocidade < velocidadeAngularNeg[1] ):
                vNeg = ( velocidade - velocidadeAngularNeg[1] ) / ( velocidadeAngularNeg[0] - velocidadeAngularNeg[1] ) 

   
        return vPos, vEq, vNeg


def distanciaFuzzificacao(distancia):

        # Variaveis de controle que define o quanto a qual conjunto este pertence
        dPos = dEq = dNeg =  0.0

        if ( distancia >= distanciaPos[1] ):
                dPos = 1.0

        elif ( distanciaPos[0] < distancia <= distanciaPos[1] ):
                dPos = ( distancia - distanciaPos[0] ) / ( distanciaPos[1] - distanciaPos[0] ) 

        if ( distancia == distanciaCentralizada[1] ):
                dEq = 1.0

        elif ( distanciaCentralizada[0] < distancia <= distanciaCentralizada[1] ):
                dEq = ( distancia - distanciaCentralizada[0] ) / ( distanciaCentralizada[1] - distanciaCentralizada[0] )

        elif ( distanciaCentralizada[1] <= distancia < distanciaCentralizada[2] ):
                dEq = ( distancia - distanciaCentralizada[2] ) / ( distanciaCentralizada[1] - distanciaCentralizada[2] )

        if ( distancia <= distanciaNeg[0] ):
                dNeg = 1.0

        elif ( distanciaNeg[0] <= distancia < distanciaNeg[1] ):
                dNeg = ( distancia - distanciaNeg[1] ) / ( distanciaNeg[0] - distanciaNeg[1] )
        
        return dPos, dEq, dNeg


# Inferencia --------------------------

def inferir(aMPos, aPos, aEq, aNeg, aMNeg, vPos, vEq, vNeg, dPos, dEq, dNeg):
	    fMPos = 0.0
	    fPos = 0.0
	    fEq = 0.0
	    fNeg = 0.0
	    fMNeg = 0.0
        fMPos = max(min(aMPos, vEq),min(aMPos, vNeg),min(aMPos,vPos)) 
		fPos = max(min(aPos, vEq), min(aPos, vPos), min(aMPos, vNeg))
		Eq = max(min(aNeg, vPos), min(aEq, vNeg), min(aEq, vEq), min(aEq, vPos), min(aPos, vNeg))
		fNeg = max(min(aMNeg, vPos),min(aNeg, vNeg), min(aNeg, vEq))
		fMNeg = max( min(aMNeg, vNeg), min(aMNeg, vEq) , min(aMNeg, vPos))
		return  fMPos, fPos, fEq, fNeg, fMNeg 

def calcPontos(y,a,b,c):
	x1 = y*(b-a) + a
	x2 = c - y*(c-b)
	return x1, x2

def area(b1, b2, h):
	return (b1)*h/2

#def forcaDefuzzificar( fMPos, fPos, fEq, fNeg, fMNeg ):
#    DifFMPos = abs(forcaMPos[1] - forcaMPos[0])
	#DifFPos = abs(forcaPos[2] - forcaPos[0])
	#DifEq = abs(forcaEq[2] - forcaEq[0])
	#DifFNeg = abs(forcaNeg[0] - forcaNeg[2])
	#DifFMNeg = abs(forcaPos[0] - forcaPos[1])
	#xFMPos, yFMPos = calcPontos(fMPos, forcaMPos[0], forcaMPos[1], forcaMPos[1])
	#areaFMPos = area(DifFMPos, abs(xFMPos - yFMPos), fMPos)
	#xFPos, yFPos = calcPontos( fPos, forcaPos[0], forcaPos[2], forcaPos[2]  )
	#areaFPos = area(DifFPos, abs(xFPos - yFPos), fPos)
	#FEq, yFEq = calcPontos( fEq, forcaEq[0], forcaEq[2], forcaEq[2]  )
	#areaFEq = area(DifEq, abs(xFEq - yFEq), fEq)
	#xFNeg, yFNeg = calcPontos( fNeg, forcaNeg[2], forcaNeg[0], forcaNeg[0]  )
	#areaFNeg = area(DifFNeg, abs(xFNeg - yFNeg), fNeg)
	#xFMNeg, yFMNeg = calcPontos( fMNeg, forcaMNeg[1], forcaMNeg[0], forcaMNeg[0]  )
	#areaFMNeg = area(DifFMNeg, abs(xFMNeg - yFMNeg), fMNeg)
	#mFMPos = (xFMPos + yFMPos + forcaMPos[0] +forcaMPos[1])/4
	#mFPos  = (xFPos + yFPos + forcaPos[0] +forcaPos[2])/4
	#mFEq   = (xFEq + yFEq + forcaEq[2] +forcaEq[1])/4
	#mFNeg = (xFNeg + yFNeg + forcaNeg[0] +forcaNeg[2])/4
	#cmFMNeg = (xFMNeg + yFMNeg + forcaMNeg[0] +forcaMNeg[1])/4
	#cm = ((areaFMPos * cmFMPos) + (areaFPos * cmFMPos) + (areaFEq * cmFEq) + (areaFNeg * cmFNeg) + (areaFMNeg * cmFMNeg)) / (areaFMPos + areaFPos + areaFEq + areaFNeg + areaFMNeg ) 
	#eturn cm

# Sistema Pendulo Invertido ##################

M=10
m=10
g=9.81
l=1.5
PI=3.14159

ml=m*l
MMm=M+m

def RK4_pend(V,force,dt):

	h=dt/2	
	A=[]
	B=[]
	C=[]
	D=[]
	Vn=[0,0,0,0]
	f=force

	a0=V[0]
	x0=V[1]
	w0=V[2]
	v0=V[3]

	a=a0
	x=x0
	w=w0
	v=v0
	senA=math.sin(a)
	cosA=math.cos(a)
	dw0=(f+MMm*g*senA/cosA-ml*w*w*senA) / (MMm*l/cosA-ml*cosA)
	dv0=(f+ml*dw0*cosA-ml*w*w*senA) / MMm
	
	A=[w]
	A.append(v)
	A.append(dw0)
	A.append(dv0)

	a=a0+h*A[0]/2.
	x=x0+h*A[1]/2.
	w=w0+h*A[2]/2.
	v=v0+h*A[3]/2.
	senA=sin(a)
	cosA=cos(a)

	B=[w]
	B.append(v)
	dw=(f+MMm*g*senA/cosA-ml*w*w*senA) / (MMm*l/cosA-ml*cosA)
	B.append(dw)
	dv=(f+ml*dw*cosA-ml*w*w*senA) / MMm
	B.append(dv)

	a=a0+h*B[0]/2.
	x=x0+h*B[1]/2.
	w=w0+h*B[2]/2.
	v=v0+h*B[3]/2.
	senA=sin(a)
	cosA=cos(a)

	C=[w]
	C.append(v)
	dw=(f+MMm*g*senA/cosA-ml*w*w*senA) / (MMm*l/cosA-ml*cosA)
	C.append(dw)
	dv=(f+ml*dw*cosA-ml*w*w*senA) / MMm
	C.append(dv)

	a=a0+h*C[0]
	x=x0+h*C[1]
	w=w0+h*C[2]
	v=v0+h*C[3]
	senA=sin(a)
	cosA=cos(a)

	D=[a]
	D.append(x)
	dw=(f+MMm*g*senA/cosA-ml*w*w*senA) / (MMm*l/cosA-ml*cosA)
	D.append(dw)
	dv=(f+ml*dw*cosA-ml*w*w*senA) / MMm
	D.append(dv)

	for i in range(4):
		Vn[i] = V[i] + (h/6.0)*(A[i]+2.0*B[i]+2.0*C[i]+D[i]) 
	return Vn

def controleManual(f):
    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT]:
        f = f - 1
    if key[pygame.K_RIGHT]:
        f = f + 1
    return f

# Metodo para controle do pendulo invertido baseado em logica fuzzy
def FUZZYCONTROL(V,t):
	forca=0
	if( V[1] > 10 or V[1] < -10):
		print ("Bateuuu:", V[1])
	    aMPos, aPos, aEq, aNeg, aMNeg  = anguloFuzzificacao(V[0])
	dPos, dEq, dNeg  = distanciaFuzzificacao(V[1])
        vPos, vEq, vNeg = velocidadeAFuzzificacao(V[2])
        fMPos, fPos, fEq, fNeg, fMNeg = inferir(aMPos, aPos, aEq, aNeg, aMNeg, vPos, vEq, vNeg, dPos, dEq, dNeg)
        forca = forcaDefuzzificar( fMPos, fPos, fEq, fNeg, fMNeg )
	return forca    
    
class Game(object):
    def main(self, screen):
        clock = pygame.time.Clock()
        image = pygame.image.load('ball.gif')
        image = pygame.transform.scale(image, (50, 50))
        base = pygame.image.load('base.png')

        angulo = 0.0
        raio = 200.0

        center_x = 454
        center_y = 450

        dt=0.01

	#-----------------------------------------------
	# Definiciao de variaveis de controle do pendulo
	tempoInicial = 0.0
	#Tempo max em segundos para execucao do jogo
	tempoMaximo = 5
	dt = 0.01
	#-----------------------------------------------

	samp=10
	count=0
	Vars=[]
	T=[]
	#angulo_inicial = 0.0
	angulo_inicial = 0.05
	f = 0.0
	X=[angulo_inicial,0,0,0]

        while tempoInicial < tempoMaximo:
            clock.tick(200)
            center_x+=X[2]*0.10
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    return
                #f =  controleManual(f)
                # Utilização do FUZZY CONTROL para equilibrar o pendulo
                f = FUZZYCONTROL(x,t)

            X=RK4_pend(X,f,dt)
           
            x = math.cos(X[0])*raio
            y = math.sin(X[0])*raio

            print X[0],f,x,y
            screen.fill((200, 200, 200))
            screen.blit(image, (center_x+x + 25, center_y - y))
            screen.blit(base, (center_x,center_y))
            pygame.display.flip()
            
            tempoInicial = tempoInicial + dt

if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((1000, 480))
    #Game().main(screen)
    #Game().main(screen,controleManual,angulo_inicial=0.05)
    #Game().main(screen)


