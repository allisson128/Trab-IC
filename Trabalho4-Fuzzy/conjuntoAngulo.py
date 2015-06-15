import matplotlib.pyplot as plt

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


# Limites

angulos = [-60, -30, 0.0, 30, 60]

muitoPositivo = [0,0,0,0,1]

Positivo = [0,0,0,1,0]

Equilibrado = [0,0,1,0,0]

Negativo = [0,1,0,0,0]

MuitoNegativo = [1,0,0,0,0]

plt.plot(angulos, MuitoNegativo,'gray')
#plt.plot(angulos, Positivo,'blue')
plt.ylabel("MuitoNegativo")
plt.xlabel("Graus")

plt.show()

main()
