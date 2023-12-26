import unittest
import pandas as pd

class TestExercicio1(unittest.TestCase):
    def test_csv_reading(self):
        # Verifica se a leitura do CSV não gera exceções
        try:
            df = pd.read_csv('C:\\Users\\Alencar Porto\\src\\data\\First_Desafio.csv', sep=';', encoding='utf-8')
        except Exception as e:
            self.fail(f"Erro na leitura do CSV: {e}")

        # Verifica se o DataFrame não está vazio
        self.assertFalse(df.empty, "O DataFrame não deve estar vazio.")

        # Verifica se o DataFrame tem as colunas esperadas
        expected_columns = ['name', 'description', 'employees', 'total_funding', 'city', 'subcountry', 'lat', 'lng', 'label', 'txt']
        self.assertListEqual(list(df.columns), expected_columns, "As colunas do DataFrame não correspondem às esperadas.")

if __name__ == '__main__':
    unittest.main()
