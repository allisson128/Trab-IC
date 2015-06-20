import matplotlib.pyplot as plt

# Definicao dos Angulos ------------

# Angulo de 30 graus = 0.52 Radianos
# Angulo de 60 graus = 1.05 Radianos
angulo30graus = 0.52
angulo60graus = 1.05

# Angulos

anguloMuitoPositivo= (angulo30graus, angulo60graus)

anguloPositivo = (0.0, angulo30graus)

anguloEquilibrado = (-angulo30graus,angulo30graus)

anguloNegativo = (-angulo30graus, 0.0)

anuguloMuitoNegativo = (-angulo60graus,-angulo30graus)

# Limites Angulos

angulos = [-60, -30, 0.0, 30, 60]

muitoPositivo = [0,0,0,0,1]

Positivo = [0,0,0,1,0]

Equilibrado = [0,0,1,0,0]

Negativo = [0,1,0,0,0]

MuitoNegativo = [1,0,0,0,0]


# Velocidade Angular

velocidadeAngularPositiva = ( 0.0, angulo30graus) 

velocidadeAngularEquilibrada = (-angulo30graus, 0.0, angulo30graus)

velocidadeAngularNegativa = (-angulo30graus, 0.0)

# Limites Velocidade Angular

velocidade = [-angulo30graus, 0.0, angulo30graus]

vPositiva = [0,0,1]

vEquilibrada = [0,1,0]

vNegativa = [1,0,0]

# Distancia

distanciaPositiva = (0.0, 7.0)
distanciaCentralizada = (-7.0, 0.0, 7.0)
distanciaNegativa = (-7.0, 0.0)

# Limites Distancia

distancia = [-7, 0.0, 7]

dPositiva = [0,0,1]
dCentralizada = [0,1,0]
dNegativa = [1,0,0]

# Graficos

plt.plot(distancia, dNegativa,'blue')
#plt.plot(angulos, Positivo,'blue')
plt.ylabel("Negativa")
plt.xlabel("Distancia")

plt.show()

main()
