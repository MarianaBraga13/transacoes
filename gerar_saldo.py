import os
import json

# persistência de dados
def carregar_patrimonio():
    if os.path.exists("patrimonio.json"):
        with open("patrimonio.json", "r") as f:
            return json.load(f)
    else:
        # estrutura inicial se o arquivo ainda não existir
        return({"patrimonio": 0.00 , "historico": []})          

def salvar_patrimonio(dados):
    with open("patrimonio.json", "w") as f:
        json.dump(dados, f, indent=4)

        

