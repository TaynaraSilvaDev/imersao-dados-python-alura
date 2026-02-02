# --------------------------------- AULA 01 --------------------------------------------
import pandas as pd

df = pd.read_csv("https://raw.githubusercontent.com/guilhermeonrails/data-jobs/refs/heads/main/salaries.csv")

# dentro do head pode colocar o valor de quantidade de linhas que você quer visualizar
# quando tá vazio, sempre aparece as 5 primeiras linhas
df.head()


df.info()

#dados descritivos - apenas numerico se sem expecificação
df.describe()

# tamanho da base
# nao tem parenteses pq nao é um método, nem função, mas sim, atributo
df.shape

linhas, colunas = df.shape[0], df.shape[1]

# var1 = linhas
print("linhas: ", linhas, "\ncolunas: ", colunas)


#Ver quais colunas tem na base
df.columns

# Dicionário de renomeação
novos_nomes = {
    'work_year': 'ano',
    'experience_level': 'senioridade',
    'employment_type': 'contrato',
    'job_title': 'cargo',
    'salary': 'salario',
    'salary_currency': 'moeda',
    'salary_in_usd': 'usd',
    'employee_residence': 'residencia',
    'remote_ratio': 'remoto',
    'company_location': 'empresa',
    'company_size': 'tamanho_empresa'
}

# Aplicando renomeação
df.rename(columns=novos_nomes, inplace=True)

# Verificando resultado
df.head()

# Conta os valores de determinada coluna / repetições
df["senioridade"].value_counts()

df["contrato"].value_counts()

df["remoto"].value_counts()

df["tamanho_empresa"].value_counts()

# Substituição dos significados para algo mais compreensível
senioridade = {
    'SE': 'senior',
    'MI': 'pleno',
    'EN': 'junior',
    'EX': 'executivo'
}

# no lugar do replace, pode ser usado o .map
df['senioridade'] = df['senioridade'].replace(senioridade)
df['senioridade'].value_counts()

contrato = {
    'FT': 'integral',
    'PT': 'parcial',
    'CT': 'contrato',
    'FL': 'freelancer'
}
df['contrato'] = df['contrato'].replace(contrato)
df['contrato'].value_counts()

tamanho_empresa = {
    'L': 'grande',
    'S': 'pequena',
    'M': 'media'
}
df['tamanho_empresa'] = df['tamanho_empresa'].replace(tamanho_empresa)
df['tamanho_empresa'].value_counts()

mapa_trabalho  = {
    0 : 'presencial',
    100: 'remoto',
    50: 'hibrido'
}
df['remoto'] = df['remoto'].replace(mapa_trabalho)
df['remoto'].value_counts()

df.head()

df.describe(include="object")

media_usd = df['usd'].mean(skipna=False).round(2)
print(media_usd)

#---------------------------------------- AULA 02 ---------------------------------------------

# Verifica se tem valores nulos na base
df.isnull()

# soma quantos campos nulos tem tada coluna
df.isnull().sum()

# valores unicos na coluna
df['ano'].unique()

df[df.isnull().any(axis=1)]



import numpy as np

# Edição de dados
# Criação de DATAFRAME teste
df_salarios = pd.DataFrame({
    'nome': ['Ana', 'Bruno', 'Carlos', 'Daniele', 'Val'],
    'salario': [4000, np.nan, 5000, np.nan, 100000]
}) 
"""
df_salarios - base
salario_media - coluna nova que está sendo criada

que vai receber:
dentro da base, vai ser preenchido (fillna)
com a media dos salários 
(round2) arredondamento de 2 casas decimais
"""
df_salarios['salario_media'] = df_salarios['salario'].fillna(df_salarios['salario'].mean().round(2))

df_salarios['salario_mediana'] = df_salarios['salario'].fillna(df_salarios['salario'].median())

df_salarios


df_temperaturas = pd.DataFrame({
    'dia': ['Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta'],
    'temperatura': [30, np.nan, np.nan, 28, 27]
})

df_temperaturas['preenchido_ffill'] = df_temperaturas['temperatura'].ffill()

df_temperaturas
 
df_temperaturas = pd.DataFrame({
    'dia': ['Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta'],
    'temperatura': [30, np.nan, np.nan, 28, 27]
})

df_temperaturas['preenchido_bfill'] = df_temperaturas['temperatura'].bfill()
df_temperaturas


df_cidades = pd.DataFrame({
    'nome': ['Ana', 'Bruno', 'Carlos', 'Daniele', 'Val'],
    'cidade': ['São Paulo', np.nan, 'Curitiba', np.nan, 'Belém'] 
})

df_cidades['cidade_preenchida'] = df_cidades['cidade'].fillna('Não informado')
df_cidades

df_limpo = df.dropna()
df_limpo.isnull().sum()

df_limpo.head()
df_limpo.info()

df_limpo = df_limpo.assign(ano = df_limpo['ano'].astype('int64'))
df_limpo.head()
df_limpo.info()

#------------------------------- AULA 03 -------------------------

# Criação de grafico
df['senioridade'].value_counts().plot(kind='bar', title = 'Distribuição de senioridade')

# Utilização da biblioteca SEABORN
import seaborn as sns
# Utilização da biblioteca MATPLOTLIB / seção dela
import matplotlib.pyplot as plt

sns.barplot(data = df_limpo, x = 'senioridade', y = 'usd')

# GRAFICO DE BARRA
plt.figure(figsize=(8,5))
sns.barplot(data = df_limpo, x = 'senioridade', y = 'usd')
plt.title('Salário médio por senioridade')
plt.xlabel('Nível de senioridade')
plt.ylabel('Salário médio anual (USD)')
plt.show()

df_limpo.groupby('senioridade')['usd'].mean().sort_values(ascending=False)
ordem = df_limpo.groupby('senioridade')['usd'].mean().sort_values(ascending=False).index
plt.figure(figsize=(8,5))
sns.barplot(data = df_limpo, x = 'senioridade', y = 'usd', order= ordem)
plt.title('Salário médio por senioridade')
plt.xlabel('Nível de senioridade')
plt.ylabel('Salário médio anual (USD)')
plt.show()


# HISTOGRAMA
plt.figure(figsize=(10,5))
# Bins são a quantidade de // do grafico, + granular fica
# kde é a linha azul que passa pelo grafico
sns.histplot(df_limpo['usd'], bins = 100, kde= True)
plt.title('Distribuição dos salários anuais')
plt.xlabel('Salário em USD')
plt.ylabel('Frequência')
plt.show()

# GRAFICO BOXPLOT
"""
-> 2 caixas - mostra a variância, valor min e max
-> linha do meio é a MEDIANA
-> os pontinhos são discrepâncias/exceções entre o 'normal' dos dados
"""
plt.figure(figsize=(8,5))
sns.boxplot(x=df_limpo['usd'])
plt.title('Boxplot salário')
plt.xlabel('Salário em USD')
plt.show()

# Boxplot de CADA senioridade
ordem_senioridade = ['junior', 'pleno', 'senior', 'executivo']
plt.figure(figsize=(8,5))
sns.boxplot(x='senioridade', y='usd', data=df_limpo, order=ordem_senioridade)
plt.title('Boxplot da distribuição por senioridade')
plt.xlabel('Salário em USD')
plt.ylabel('USD')
plt.show()

# MUDANDO A PALHETA DO GRAFICO
# palette e hue
ordem_senioridade = ['junior', 'pleno', 'senior', 'executivo']
plt.figure(figsize=(8,5))
sns.boxplot(x='senioridade', y='usd', data=df_limpo, order=ordem_senioridade, palette='Set2', hue='senioridade')
plt.title('Boxplot da distribuição por senioridade')
plt.xlabel('Salário em USD')
plt.ylabel('USD')
plt.show()

# Gráficos interativos
import plotly.express as px

senioridade_media_salario= df_limpo.groupby('senioridade')['usd'].mean().round(2).sort_values(ascending=False).reset_index()

fig = px.bar(senioridade_media_salario,
             x= 'senioridade',
             y= 'usd',
             title= 'Média salarial por senioridade',
             labels={'senioridade': 'Nível de senioridade', 'usd': 'Média salarial anual (USD)'})
# fig.update_yaxes(tickformat=".2f")
fig.show()


# Grafico de pizza/torta/rosquinha
remoto_contagem = df_limpo['remoto'].value_counts().reset_index()
remoto_contagem.columns = ['tipo_trabalho', 'quantidade']
# adiciona o hole pra virar rosquinha
fig = px.pie(remoto_contagem,
             names = 'tipo_trabalho', 
             values = 'quantidade',
             title= 'Proporção dos tipos de trabalho',
             hole=0.5
             )
fig.update_traces(textinfo='percent+label')
fig.show()


# ------------ AULA 04 -----------
import pycountry

# Função para converter ISO-2 para ISO-3
def iso2_to_iso3(code):
    try:
         return pycountry.countries.get(alpha_2=code).alpha_3
    except:
         return None
    
# Criar nova coluna ocm código ISO-3
df_limpo['residencia_iso3'] = df_limpo['residencia'].apply(iso2_to_iso3)

# Calcular média salarial por país (ISO-3)
df_ds = df_limpo[df_limpo['cargo']=='Data Scientist']
media_ds_pais = df_ds.groupby('residencia_iso3')['usd'].mean().reset_index()

# Gerar o mapa
fig = px.choropleth (
     media_ds_pais,
     locations='residencia_iso3',
     color='usd',
     color_continuous_scale='rdylgn',
     title='Salário médio de Ciêntista de Dados por país',
     labels={'usd': 'Salário médio (USD)', 'residencia_iso3': 'País'}
)

fig.show()

df_limpo.to_csv('dados-imersao-final.csv', index=False)