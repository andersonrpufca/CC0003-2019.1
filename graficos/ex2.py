# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt

#Dados do grafico
labels = 'Pré-usinagem', 'Tratamento térmico', 'Fundição', 'Usinagem', 'Tratamento superficial'
sizes = [9, 12, 10, 45, 13]

# Plot
plt.pie(sizes, labels=labels,autopct='%1.1f%%', shadow=True, startangle=55)

plt.axis('equal')
plt.show()

labelsB = 'EUL',  'PES', 'EFA', 'EDD', 'ELDR', 'EPP', 'UEN', 'Outros'
sizesB = [39, 200, 42, 15, 67, 276, 27, 66]

plt.pie(sizesB, labels=labelsB, autopct='%1.1f%%', shadow=True, startangle=0)
