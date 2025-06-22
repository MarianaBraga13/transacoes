import os
import json
ARQUIVO = "patrimonio.json"

# persistência de dados
def carregar_patrimonio():
    if os.path.exists(ARQUIVO):
        with open(ARQUIVO, "r") as f:
            return json.load(f)
    else:
        # estrutura inicial se o arquivo ainda não existir
        return({"patrimonio": 0.00 , "historico": []})          

def salvar_patrimonio(dados):
    with open(ARQUIVO, "w") as f:
        json.dump(dados, f, indent=4)

        

