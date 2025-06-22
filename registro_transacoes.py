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

def mostrar_extrato():
    if os.path.exists(ARQUIVO):
        with open(ARQUIVO, "r") as f:
            try:
                dados = json.load(f)
                historico = dados.get("historico", []) #acessando o dict como uma lista

                if not historico:
                    print("Nenhuma transação registrada")
                else:
                    for item in historico:
                        print(f"[{item['data']}] {item['tipo'].capitalize()}: R${item['valor']:.2f}")
                       
            except json.JSONDecodeError:
                print("Erro ao ler o extrato.")
    else:
        print("Nenhuma transação realizada ainda.")
                



        

