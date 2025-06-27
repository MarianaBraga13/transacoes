import os
import json
import getpass

LOGIN_CLIENTE = "dados_login.json"

class Login:
    def __init__(self):
        self.nome = ""
        self.senha = ""
        self.user_id = ""

    def gerar_novo_id(self):
        if not os.path.exists(LOGIN_CLIENTE):
            return "u001"
        with open(LOGIN_CLIENTE, "r") as f:
            usuarios = json.load(f)
            ids = [int(uid[1:]) for uid in usuarios.keys()]
            novo_id = max(ids) + 1
            return f"u{novo_id:03d}"

    def cadastrar(self):
        print("\n📝 Cadastro de Novo Usuário")
        self.nome = input("Nome: ")
        self.senha = getpass.getpass("Senha: ")
        self.user_id = self.gerar_novo_id()

        dados = {}
        if os.path.exists(LOGIN_CLIENTE):
            with open(LOGIN_CLIENTE, "r") as f:
                dados = json.load(f)

        dados[self.user_id] = {"nome": self.nome, "senha": self.senha}
        with open(LOGIN_CLIENTE, "w") as f:
            json.dump(dados, f, indent=4)

        print(f"\n✅ Cadastro realizado com sucesso! Seu ID é {self.user_id}")

    def logar(self):
        print("\n🔐 Login de Usuário")
        nome = input("Nome: ")
        senha = getpass.getpass("Senha: ")

        if os.path.exists(LOGIN_CLIENTE):
            with open(LOGIN_CLIENTE, "r") as f:
                dados = json.load(f)
                for uid, info in dados.items():
                    if info["nome"] == nome and info["senha"] == senha:
                        print("✅ Login realizado!")
                        self.nome = nome
                        self.senha = senha
                        self.user_id = uid
                        return uid, nome
        print("❌ Nome ou senha incorretos.")
        return None, None
