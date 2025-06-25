import os
import json
from cli_login import logar
ARQUIVO_DADOS = "patrimonio.json"

# persistência de dados
def carregar_patrimonio(user_id):
    if os.path.exists(ARQUIVO_DADOS):
        with open(ARQUIVO_DADOS, "r") as f:
            dados_completos =  json.load(f)
            return dados_completos.get(user_id, {"patrimonio" : 0.0, "historico" : []})
    else:
        # estrutura inicial se o arquivo ainda não existir
        return({"patrimonio": 0.00 , "historico": []})          

def salvar_patrimonio(user_id, dados_usuario):
    if os.path.exists(ARQUIVO_DADOS):
        with open(ARQUIVO_DADOS, "r") as f:
            dados_completos = json.load(f)
    else: dados_completos = {}
    dados_completos[user_id] = dados_usuario # dados completos com user_id recebe dados do usuário.

    with open(ARQUIVO_DADOS, "w") as f:
         json.dump(dados_completos, f, indent=4)


def mostrar_extrato(user_id):
    if os.path.exists(ARQUIVO_DADOS):
        with open(ARQUIVO_DADOS, "r") as f:
            try:
                dados_completos = json.load(f)
                dados_usuario = dados_completos.get(user_id)

                if not dados_usuario:
                    print("Usuário não encontrado.")
                    return

                historico = dados_usuario.get("historico", [])

                if not historico:
                    print("Nenhuma transação registrada.")
                else:
                    print("\n------------------ EXTRATO ------------------")
                    for item in historico:
                        print(f"[{item['data']}] {item['tipo'].capitalize()}: R${item['valor']:.2f}")
            except json.JSONDecodeError:
                print("Erro ao ler o extrato.")
    else:
        print("Nenhuma transação realizada ainda.")

                



        

