import os

# persistência de dados
def carregar_patrimonio():
    if os.path.exists("patrimonio.txt"):
        with open("patrimonio.txt", "r") as f:
            return float(f.read().strip())
    return 0.0

def salvar_patrimonio(valor):
    with open("patrimonio.txt", "w") as f:
        f.write(str(valor)) 