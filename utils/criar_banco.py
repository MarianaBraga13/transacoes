import os
import json

ARQUIVO_DADOS = "patrimonio.json"

def criar_banco():
    if not os.path.exists(ARQUIVO_DADOS):
        with open(ARQUIVO_DADOS, "x") as f:
            json.dump({} , f , indent=4)