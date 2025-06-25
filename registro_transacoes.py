import os
import json
ARQUIVO_DADOS = "patrimonio.json"

class Usuario:
    def __init__(self, user_id):
        self.user_id = user_id
        self.patrimonio = 0.0
        self.historico = []
        self.carregar_dados()

# persistência de dados
def carregar_dados(self):
    if os.path.exists(ARQUIVO_DADOS):
        with open(ARQUIVO_DADOS, "r") as f:
            dados_completos =  json.load(f)
            dados_usuario = dados_completos.get(self.user_id)
            if dados_usuario:
                self.patrimonio = dados_usuario.get("patrimonio", 0.0)
                self.historico = dados_usuario.get("historico", [])       

def salvar_dados(self):
    if os.path.exists(ARQUIVO_DADOS):
        with open(ARQUIVO_DADOS, "r") as f:
            dados_completos = json.load(f)
    else: 
        dados_completos = {}

    dados_completos[self.user_id] = {
        "patrimonio" : self.patrimonio,
        "historico" : self.historico
    }

    with open(ARQUIVO_DADOS, "w") as f:
         json.dump(dados_completos, f, indent=4)


def mostrar_extrato(self):
    if os.path.exists(ARQUIVO_DADOS):
        with open(ARQUIVO_DADOS, "r") as f:
            try:
                dados_completos = json.load(f)
                dados_usuario = dados_completos.get(self.user_id)

                if not dados_usuario:
                    print("Usuário não encontrado.")
                    return

                historico = dados_usuario.get(self.historico)

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


