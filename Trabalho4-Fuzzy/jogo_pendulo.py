import pygame
import math
from math import *

M=10
m=10
g=9.81
l=0.5
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


def controleManual(f,alpha,x):
    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT]:
        if f>0:
		return 0
        return f*1.01-3
    if key[pygame.K_RIGHT]:
        if f<0:
		return 0
        return f*1.01 + 3
    return f
    

def controleNaive(f,alpha,x):
	return f -7*alpha


class Game(object):

    def main(self, screen, controle, angulo_inicial=0.0):
        clock = pygame.time.Clock()
        image = pygame.image.load('ball.gif')
        image = pygame.transform.scale(image, (50, 50))
        base = pygame.image.load('base.png')

        raio = 200.0
        base_x = 454
        base_y = 450

        dt=0.01
	samp=10
	count=0
	Vars=[]
	T=[]
	f = 0.0
	X=[angulo_inicial,0,0,0]

        while 1 and abs(X[0])<1.25:
            clock.tick(100)
            base_x+=X[2]*0.10
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    return
	
	    
	    f = controle(f,X[0],base_x)

            X=RK4_pend(X,f,dt)
	    
	    x = - math.sin(X[0])*raio
            y = math.cos(X[0])*raio

            print X[0],f#,x,y
            screen.fill((200, 200, 200))
	    pygame.draw.line(screen,pygame.Color("black"),(base_x + 50,base_y),(base_x + 50 + x , base_y - y +25),4)
            screen.blit(image, (base_x + 25 + x , base_y - y))
            screen.blit(base, (base_x,base_y))
            pygame.display.flip()


if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((1000, 480))

    # Use controleNaive ou controleManual ou implemente um melhor
    Game().main(screen,controleManual,angulo_inicial=0.05)

