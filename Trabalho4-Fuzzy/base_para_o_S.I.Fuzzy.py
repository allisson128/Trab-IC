import pygame
import math
from math import *

# DEFINICAO DAS VARIAVEIS

# Definicao dos Angulos ------------

# Angulo de 30 graus = 0.52 Radianos
# Angulo de 60 graus = 1.05 Radianos
angulo30graus = 0.52
angulo60graus = 1.05

anguloMuitoPositivo= (angulo30graus, angulo60graus)

anguloPositivo = (0.0, angulo30graus)

anguloEquilibrado = (-angulo30graus,angulo30graus)

anguloNegativo = (-angulo30graus, 0.0)

anuguloMuitoNegativo = (-angulo60graus,-angulo30graus)

#




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
	tempoMaximo = 10
	dt = 0.01
	#-----------------------------------------------

	samp=10
	count=0
	Vars=[]
	T=[]
	angulo_inicial = 0.0
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
                f =  controleManual(f)

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
    Game().main(screen)


