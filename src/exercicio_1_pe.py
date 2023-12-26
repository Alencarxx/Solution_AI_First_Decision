import pandas as pd
from io import StringIO
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import SVC
from sklearn.pipeline import make_pipeline
from sklearn.metrics import classification_report
import chardet

# Função para detectar a codificação do arquivo
def detect_encoding(file_path):
    with open(file_path, 'rb') as f:
        result = chardet.detect(f.read())
    return result['encoding']

# Lista para armazenar os dados lidos
data = []

# Lista para armazenar as linhas validadas
valid_lines = []

# Caminho do arquivo
file_path = 'C:\\Users\\Alencar Porto\\src\\data\\First_Desafio_2.csv'

# Detectar a codificação do arquivo
encoding = detect_encoding(file_path)

# Tente abrir o arquivo e ler linha por linha
with open(file_path, 'r', encoding=encoding) as file:
    for line in file:
        try:
            # Tente realizar a leitura da linha
            row = pd.read_csv(StringIO(line), header=None).values.flatten()

            # Adicione a linha à lista de dados
            data.append(row)

            # Adicione a linha à lista de linhas validadas
            valid_lines.append(line)

        except pd.errors.ParserError:
            # Se houver um erro, pule para a próxima linha
            continue

# Crie um DataFrame a partir dos dados lidos
df = pd.DataFrame(data)

# Mantenha apenas as primeiras 8 colunas
df = df.iloc[:, :8]

# Renomeie as colunas conforme necessário
df.columns = ['name', 'description', 'employees', 'total_funding', 'city', 'subcountry', 'lat', 'lng']

# Imprima as linhas validadas
print("Linhas validadas:")
for valid_line in valid_lines:
    print(valid_line.strip())

# Palavras-chave para filtrar
keywords = ['solutions on waste and water', 'water quality', 'water efficiency use', 'water contamination', 'water for human consumption', 'water resources']

# Filtrar com base nas palavras-chave
filtered_df = df[df['description'].str.contains('|'.join(keywords), case=False, na=False)]

# Imprima o número de linhas válidas após a filtragem
print("\nNúmero de linhas válidas após a filtragem:", len(filtered_df))

# Imprima algumas amostras das descrições para verificar
print("\nAmostras das descrições:")
print(filtered_df['description'].head())

# Verifique se há dados suficientes para dividir em conjuntos de treino e teste
if len(filtered_df) >= 1:
    # Selecione aleatoriamente algumas amostras para criar conjuntos de treino e teste
    train_data, test_data = train_test_split(filtered_df['description'], test_size=0.2, random_state=42)

    # Criando um modelo de classificação usando TF-IDF e SVM
    model = make_pipeline(TfidfVectorizer(), SVC(kernel='linear'))

    # Treinando o modelo
    model.fit(train_data, train_data)

    # Fazendo previsões no conjunto de teste
    predictions = model.predict(test_data)

    # Avaliando o desempenho do modelo
    print("\nDesempenho do modelo:")
    print(classification_report(test_data, predictions))

else:
    print("\nNão há dados suficientes para dividir em conjuntos de treino e teste.")
