import os
import json
from cli_login import logar
ARQUIVO_DADOS = "patrimonio.json"


# persistência de dados
def carregar_patrimonio(user_id):
    user_id = logar()
    if user_id:
        if os.path.exists(ARQUIVO_DADOS):
            with open(ARQUIVO_DADOS, "r") as f:
                return json.load(f)
        else:
            # estrutura inicial se o arquivo ainda não existir
            return({"patrimonio": 0.00 , "historico": []})          

def salvar_patrimonio(user_id, dados):
    user_id = logar()
    if user_id:
        with open(ARQUIVO_DADOS, "w") as f:
            json.dump(dados, f, indent=4)

def mostrar_extrato(user_id):
        user_id = logar()
        if user_id:
            if os.path.exists(ARQUIVO_DADOS):
                with open(ARQUIVO_DADOS, "r") as f:
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
                



        

