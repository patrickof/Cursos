import matplotlib.pyplot as plt

x1 = [1, 3, 5, 7, 9, 11]
y1 = [2, 3, 7, 2, 4, 6]

x2 = [2, 4, 6, 8, 10, 12]
y2 = [1, 3, 4, 3, 6, 5]

tam = [100, 200, 300, 400, 600, 700]
plt.title("Gráfico")
plt.xlabel("Eixo X")
plt.ylabel("Eixo Y")



#plt.bar(x1, y1, label = "Gráfico 1") ## Gráfico de barra
#plt.bar(x2, y2, label = "Gráfico 2")

plt.plot(x1, y1, label = "Retas", color = "#000099", linestyle = "dashed") ## Gráfico de linha
plt.scatter(x1,y1, label = "Pontos", color = "g", marker = "1" , s = tam) # Gráfico de pontos


plt.legend() # Atribuir a legenda ao gráfico

plt.show() ## mostrar o gráfico


