import snap
import matplotlib.pyplot as plt

individuos = [1,2,3,4,5,6]

round0 = [0.85,0.69,0.46,0.23,0.18,0.17]

round1 = [0.73,0.86,0.32,0.30,0.15,0.14]

round2 = []

round3 = []

#plt.plot(individuos, round0,'purple')
#plt.ylabel("Funcao Fitness")
#plt.xlabel("Individuos")
#plt.title("Antes de Iniciar o Alg Genetico")
#plt.show()

plt.plot(individuos, round1,'purple')
plt.ylabel("Funcao Fitness")
plt.xlabel("Individuos")
plt.title("Round 1 do Alg Genetico")
plt.show()


main()

