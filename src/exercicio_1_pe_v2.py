import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import SVC
from sklearn.pipeline import make_pipeline
from sklearn.metrics import classification_report
import io

# Carregando o conjunto de dados
file_path = 'C:\\Users\\Alencar Porto\\src\\data\\First_Desafio.csv'
with io.open(file_path, 'r', encoding='utf-8') as file:
    # Detectando automaticamente o número correto de colunas
    first_line = file.readline().strip()
    num_columns = len(first_line.split(';'))

# Carregando novamente o conjunto de dados com o número correto de colunas
df = pd.read_csv(file_path, sep=';', encoding='utf-8', header=None, names=range(num_columns))

# Verificar a estrutura atual do DataFrame
print("Estrutura atual do DataFrame:")
print(df.head())

# Renomear as colunas apenas se houver 8 colunas
if num_columns >= 8:
    print("8")
    # Renomear as colunas conforme necessário
    df.columns = ['name', 'description', 'employees', 'total_funding', 'city', 'subcountry', 'lat', 'lng', 'label', 'txt']
    print("9")
    # Filtrar empresas relacionadas ao tratamento de água com base nas palavras-chave fornecidas
    keywords = ['solutions on waste and water', 'water quality', 'water', 'water contamination', 'water for human consumption', 'water resources']
    filtered_df = df[df['description'].str.contains('|'.join(keywords), case=False, na=False)]
    print("10")
    # Verificar se há linhas válidas após a filtragem
    if not filtered_df.empty:
        # Separando o conjunto de dados em treino e teste
        train_data, test_data, train_labels, test_labels = train_test_split(
            filtered_df['description'],  # Usando as descrições como features
            filtered_df['name'],  # Supondo que você tenha uma coluna 'name' indicando a relevância para o tratamento de água
            test_size=0.9,
            random_state=4200
        )
        print("11")
        # Criando um modelo de classificação usando TF-IDF e SVM
        model = make_pipeline(TfidfVectorizer(), SVC(kernel='linear'))

        # Treinando o modelo
        model.fit(train_data, train_labels)

        # Fazendo previsões no conjunto de teste
        predictions = model.predict(test_data)

        # Avaliando o desempenho do modelo
        print("\nDesempenho do modelo:")
        print(classification_report(test_labels, predictions))

    else:
        print("\nNão há linhas válidas após a filtragem.")
else:
    print("\nO número de colunas não é 8, então as colunas não serão renomeadas.")
