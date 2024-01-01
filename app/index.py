# app/index.py
import sys
from pathlib import Path

# Adicione o diretório principal ao sys.path
sys.path.append(str(Path(__file__).resolve().parents[1]))

from src.exercicio_2_ae import exercicio_2_ae
from src.exercicio_1_pe_v2 import exercicio_1_pe


def main():
    print("Executando o projeto...")

    # Chame as funções ou lógica principal dos exercícios aqui
    exercicio_1_pe()
    exercicio_2_ae()
    
if __name__ == "__main__":
    main()
