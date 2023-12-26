import subprocess

def run_exercicio(exercicio):
    command = f"docker run {exercicio}"
    subprocess.run(command, shell=True)

# Executar o exercício 1
run_exercicio("exercicio_1_pe")

# Executar o exercício 2
run_exercicio("exercicio_2_ae")

# Executar os testes automatizados
subprocess.run("docker run test_exercicio_1", shell=True)
subprocess.run("docker run test_exercicio_2", shell=True)