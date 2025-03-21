import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

st.set_page_config(layout="wide")

st.title("Análise Completa dos Dados do Titanic")  
st.write("Aqui você encontrará uma análise detalhada sobre os passageiros do Titanic, incluindo gráficos e estatísticas.") 

df = pd.read_csv('../../data/titanic.csv')

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

#grafico de barras

bar_chart = plt.figure(figsize=(12, 3))
plt.bar(data['Sexo'], data['Quantidade'], color=['lightblue', 'lightcoral'])
plt.title('Quantidade de Sobreviventes por Sexo', fontsize=14)
plt.xlabel('Sexo', fontsize=10)
plt.ylabel('Quantidade',fontsize=10)
plt.xticks(rotation=0) 



#grafico de pizza com todos os tripulantes
total = data['Quantidade'].sum()
data['Porcentagem'] = (data['Quantidade'] / total) * 100

labels = data["Sexo"]
sizes = data['Porcentagem']
explode = (0, 0.1, 0, 0) 
fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal') 
ax1.legend(labels, fontsize=12, loc='lower right')


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
fig2, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.legend(labels, fontsize=12, loc='lower right') 
ax1.axis('equal') 



#grafico boxplot
boxplot_chart = plt.figure(figsize=(8, 9))

plt.boxplot(
    [df[df['Survived'] == 1]['Age'],
     df[df['Survived'] == 0]['Age']],
    tick_labels=['Falecidos', 'Sobreviventes'] 
)
plt.ylabel('Idade', fontsize=18)
plt.title('Box Plot das Idades de Falecidos e Sobreviventes no Titanic', fontsize=24)
plt.grid(axis='y', linestyle='--', alpha=0.7)


selected_option = st.selectbox("Selecione os graficos para exibição", ["Graficos de pizza e Boxplot", "Grafico em barras"])
if selected_option == "Grafico em barras":
    col4 = st.columns(1)[0]
    with col4:
        st.pyplot(bar_chart)
    
else:
    col1, col2, col3 = st.columns(3)
    with col1:
        st.pyplot(fig1)
    
    with col2: 
        st.pyplot(fig2)

    with col3:
        st.pyplot(boxplot_chart)