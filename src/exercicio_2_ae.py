import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Carregando o conjunto de dados
df = pd.read_csv('C:\\Users\\Alencar Porto\\src\\data\\First_Desafio.csv', sep=';', encoding='utf-8')

# Filtrando empresas relacionadas ao tratamento de água com base nas palavras-chave fornecidas
keywords = ['solutions on waste and water', 'water', 'Improve water quality', 'water efficiency use', 'water contamination', 'water for human consumption', 'water resources']
filtered_df = df[df['name'].str.contains('|'.join(keywords), case=False, na=False)]

# Adicionando informações sobre empregados, financiamento, etc. à análise
additional_columns = ['employees', 'total_funding', 'city', 'subcountry', 'lat', 'lng']

# Visualizando estatísticas descritivas das variáveis adicionais
print(filtered_df[additional_columns].describe())

# Visualizando a distribuição geográfica das empresas
plt.figure(figsize=(10, 6))
sns.scatterplot(x='lng', y='lat', data=filtered_df, hue='city', palette='viridis', size='employees', sizes=(20, 200), alpha=0.7)
plt.title('Distribuição Geográfica das Empresas')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.legend(title='Cidade')
plt.show()

# Identificando as principais cidades (pólos de desenvolvimento)
top_cities = filtered_df['city'].value_counts().head(5)
print(f'Principais cidades para desenvolvimento:\n{top_cities}')

# Visualizando o total de financiamento por cidade
plt.figure(figsize=(12, 6))
sns.barplot(x='total_funding', y='city', data=filtered_df, estimator=sum, ci=None, palette='coolwarm')
plt.title('Total de Financiamento por Cidade')
plt.xlabel('Total de Financiamento')
plt.ylabel('Cidade')
plt.show()
