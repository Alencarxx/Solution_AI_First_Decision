import unittest
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

class TestExercicio2(unittest.TestCase):
    def setUp(self):
        # Carrega o conjunto de dados
        self.df = pd.read_csv('C:\\Users\\Alencar Porto\\src\\data\\First_Desafio.csv', sep=';', encoding='utf-8')

    def test_keyword_filtering(self):
        # Verifica se o filtro de palavras-chave não gera exceções
        keywords = ['solutions on waste and water', 'water', 'Improve water quality', 'water efficiency use', 'water contamination', 'water for human consumption', 'water resources']
        try:
            filtered_df = self.df[self.df['name'].str.contains('|'.join(keywords), case=False, na=False)]
        except Exception as e:
            self.fail(f"Erro no filtro de palavras-chave: {e}")

        # Verifica se o DataFrame filtrado não está vazio
        self.assertFalse(filtered_df.empty, "O DataFrame filtrado não deve estar vazio.")

    def test_visualization(self):
        # Verifica se a visualização não gera exceções
        try:
            plt.figure(figsize=(10, 6))
            sns.scatterplot(x='lng', y='lat', data=self.df, hue='city', palette='viridis', size='employees', sizes=(20, 200), alpha=0.7)
            plt.title('Distribuição Geográfica das Empresas')
            plt.xlabel('Longitude')
            plt.ylabel('Latitude')
            plt.legend(title='Cidade')
            plt.close()
        except Exception as e:
            self.fail(f"Erro na visualização: {e}")

if __name__ == '__main__':
    unittest.main()
