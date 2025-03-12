import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data/titanic.csv')

plt.figure(figsize=(8, 6))

plt.boxplot(
    [df[df['Survived'] == 1]['Age'],
    df[df['Survived'] == 0]['Age']],
    labels=['Falecidos', 'Sobreviventes']
)
plt.ylabel('Idade')
plt.title('Box Plot das Idades de Falecidos e Sobreviventes no Titanic')
plt.grid(axis='y')
plt.show()
