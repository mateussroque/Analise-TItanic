import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt


df = pd.read_csv('../data/titanic.csv')

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
st.title("Analise de dados titanic")

# GRAFICO EM BARRA NATIVO STREAMLIT
st.bar_chart(data.set_index('Sexo')['Quantidade'])

#grafico de pizza com todos os tripulantes
total = data['Quantidade'].sum()
data['Porcentagem'] = (data['Quantidade'] / total) * 100

labels = data["Sexo"]
sizes = data['Porcentagem']
explode = (0, 0.1, 0, 0) 
fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal') 
st.pyplot(fig1)


#grafico de pizza com somente tripulantes sobreviventes
data = pd.DataFrame({
    'Sexo': ['Mulheres sobreviventes', 'Homens sobreviventes'],
    'Quantidade': [
        resultado.loc['female', 'Sobreviventes'],
        resultado.loc['male', 'Sobreviventes'],
    ]
})
total = data['Quantidade'].sum()
data['Porcentagem'] = (data['Quantidade'] / total) * 100



labels = data["Sexo"]
sizes = data['Porcentagem']
explode = (0, 0.1) 
fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal') 
st.pyplot(fig1)



#grafico boxplot
plt.figure(figsize=(8, 6))

plt.boxplot(
    [df[df['Survived'] == 1]['Age'],
    df[df['Survived'] == 0]['Age']],
    labels=['Falecidos', 'Sobreviventes']
)
plt.ylabel('Idade')
plt.title('Box Plot das Idades de Falecidos e Sobreviventes no Titanic')
plt.grid(axis='y', linestyle='--', alpha=0.7)
st.pyplot(plt)