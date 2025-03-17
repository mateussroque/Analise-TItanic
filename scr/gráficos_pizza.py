import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('data/titanic.csv')


resultado = df.groupby(['Sex', 'Survived']).size().unstack(fill_value=0)


resultado.columns = ['Falecidos', 'Sobreviventes']


data = pd.DataFrame({
    'Sexo': ['Mulheres', 'Homens', 'Mulheres falecidas', 'Homens falecidos'],
    'Quantidade': [
        resultado.loc['female', 'Sobreviventes'],
        resultado.loc['male', 'Sobreviventes'],
        resultado.loc['female', 'Falecidos'],
        resultado.loc['male', 'Falecidos'],
    ]
})


data.plot(x='Sexo', y='Quantidade', kind='bar')

plt.xlabel('Sexo')
plt.ylabel('Quantidade')
plt.title('Quantidade de Homens e Mulheres no Titanic')
plt.show()

df = pd.read_csv('titanic.csv')


resultado = df.groupby(['Sex', 'Survived']).size().unstack(fill_value=0)


resultado.columns = ['Falecidos', 'Sobreviventes']


data = pd.DataFrame({
    'Sexo': ['Mulheres sobreviventes', 'Homens sobreviventes', 'Mulheres falecidas', 'Homens falecidos'],
    'Quantidade': [
        resultado.loc['female', 'Sobreviventes'],
        resultado.loc['male', 'Sobreviventes'],
        resultado.loc['female', 'Falecidos'],
        resultado.loc['male', 'Falecidos'],
    ]
})

total = data['Quantidade'].sum()

data['Porcentagem'] = (data['Quantidade'] / total) * 100

data.plot.pie(y='Porcentagem', labels=data['Sexo'], autopct='%1.1f%%', startangle=90)

plt.ylabel('')
plt.title('Porcentagem de Homens e Mulheres no Titanic')
plt.show()

df = pd.read_csv('titanic.csv')


resultado = df.groupby(['Sex', 'Survived']).size().unstack(fill_value=0)


resultado.columns = ['Falecidos', 'Sobreviventes']


data = pd.DataFrame({
    'Sexo': ['Mulheres sobreviventes', 'Homens sobreviventes'],
    'Quantidade': [
        resultado.loc['female', 'Sobreviventes'],
        resultado.loc['male', 'Sobreviventes'],
    ]
})

total = data['Quantidade'].sum()

data['Porcentagem'] = (data['Quantidade'] / total) * 100

data.plot.pie(y='Porcentagem', labels=data['Sexo'], autopct='%1.1f%%', startangle=90)

plt.ylabel('')
plt.title('Porcentagem de Homens e Mulheres no Titanic')
plt.show()
