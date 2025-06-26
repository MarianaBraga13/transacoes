import os
import json
import getpass

LOGIN_CLIENTE = "dados_login.json"

class Login:
    def __init__(self, nome, senha, user_id , dados_completos):
        self.novo_id = "u001"
        self.nome = nome
        self.senha = senha
        self.gerar_novo_id() == user_id
        self.carregar_usuarios() == dados_completos

    def gerar_novo_id(self, novo_id):
        if not self.user_id:
                with open(LOGIN_CLIENTE, "r") as f:
                    todos_usuarios = json.load(f)
                    ids = [int(uuid[1:]) for uuid in todos_usuarios.keys()]
                    novo_id = max(ids) + 1
                    return f"u{novo_id:03d}"       

    # Estrutura do documento json (como serão salvos e lidos os dados):

    ### Como o JSON vai SALVAR os dados
    def salvar_usuario(self, dados_completos):
            if os.path.exists(LOGIN_CLIENTE):
                if not dados_completos:
                    return{}
                else:
                    self.gerar_novo_id()
                    # como eu quero que salve os dados
                    dados_completos[self.user_id] = {
                        "nome" : self.nome,
                        "senha" : self.senha
                    }
                with open(LOGIN_CLIENTE, "w") as f:
                    json.dump(dados_completos, f, indent=4) 

    ### Como o JSON vai LER os dados
    def carregar_usuarios(self, dados_completos):
            dados_usuario = dados_completos.get(self.user_id)
            if dados_usuario:
                self.nome = dados_usuario.get("nome" , {})
                self.senha = dados_usuario.get("senha", {})

            return {}

    ### Cadastrando o usuário (a)

    def cadastrar(self, user_id, nome, senha):
        
        print("\n================== 🏦 BANCO PY ==================\n")
        print("Área de Cadastro de Usuário (a)\n")
        nome = input("\nInsira seu Nome Completo 👤: ")
        try:
            nome = str(nome)
            if nome == self.nome:
                print(f"\nNome já cadastrado com o id: {user_id}, por favor, efetue o login.")
                return self.logar()
            else:
                senha = getpass.getpass("\nInsira uma senha para cadastro 🔑: ")
                senha = int(self.senha)
                if senha:
                    print("Cadastro realizado com sucesso!")
        except ValueError:
            print("Insira caracteres numéricos para senha.") 

    ### Efetuando login

        def logar(self, nome, senha, dados_completos):
            print("\n================== 🏦 BANCO PY ==================\n")
            print("Olá! 👋 Faça login para acessar a sua conta: \n")

            # apenas para testes:
            for dados_usuario in dados_completos:
                print(f"Usuários cadastrados: {dados_usuario[self.nome]} {dados_usuario[self.senha]}")

            nome = input("\nNome 👤 : ")
            senha = getpass.getpass("\nSenha 🔑: ")
            #if any(user['nome'] == nome for user in todos_usuarios.values()): # Percorra todos_usuarios.values e verifique se contém o nome
            for dados_usuario in dados_completos:
                if self.nome['nome'] == nome and self.senha['senha'] == senha: 
                    print("\nLogin efetuado com sucesso!")
                    return user_id
            
            print("Senha incorreta.")
            return None

