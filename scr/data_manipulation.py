# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1BE8oN7eFquoFvAR-2OOfCd7etjrI1ZJ0
"""



import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("data/titanic.csv")
df.head()
df["Survived"].plot

# geração de grafico de barras para comparar quantidade de homens e mulheres que foram e que faleceram


qtd_mulheres = len(df[df['Sex'] == 'female'])
qtd_homens = len(df[df['Sex'] == 'male'])

qtd_homens_falecidos= len( df[(df['Sex'] == 'male') & (df['Survived'] == 0)])
qtd_mulheres_falecidas = len(df[(df['Sex'] == 'female') & (df['Survived'] == 0)])

data = pd.DataFrame({
    'Sexo': ['Mulheres', 'Homens', 'Mulheres falecidas', 'Homens falecidos'],
    'Quantidade': [qtd_mulheres, qtd_homens, qtd_mulheres_falecidas, qtd_homens_falecidos]
})

data.plot(x = 'Sexo', y = 'Quantidade', kind='bar')

plt.xlabel('Sexo')
plt.ylabel('Quantidade')
plt.title('Quantidade de Homens e Mulheres no Titanic')
plt.show()



