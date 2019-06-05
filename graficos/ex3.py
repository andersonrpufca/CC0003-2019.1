# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

labels = 'Pré-usinagem', 'Tratamento térmico', 'Fundição', 'Usinagem', 'Tratamento superficial'
sizes = [9, 12, 10, 45, 13]
y_pos = np.arange(len(sizes))

# Criando as barras
plt.bar(y_pos, sizes,color=['black', 'red', 'green', 'blue', 'cyan'])

# Criando os nomes das barras
plt.xticks(y_pos, labels)

# Mostrando o gráfico
plt.show()



labelsB = 'EUL',  'PES', 'EFA', 'EDD', 'ELDR', 'EPP', 'UEN', 'Outros'
sizesB = [39, 200, 42, 15, 67, 276, 27, 66]
y_posB = np.arange(len(sizesB))

plt.bar(y_posB, sizesB,color=['cyan', 'blue', 'green', 'red', 'black'])

plt.xticks(y_posB, labelsB)

plt.show()