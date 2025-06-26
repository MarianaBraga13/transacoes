import os
import json
import getpass

LOGIN_CLIENTE = "dados_login.json"

class Login:
    def __init__(self, nome, senha, user_id):
        self.novo_id = "u001"
        self.nome = nome
        self.senha = senha
        self.gerar_novo_id() = user_id
        self.carregar_usuarios() 

    def gerar_novo_id(self, novo_id):
        if not self.user_id:
                with open(LOGIN_CLIENTE, "r") as f:
                    todos_usuarios = json.load(f)
                    ids = [int(uuid[1:]) for uuid in todos_usuarios.keys()]
                    novo_id = max(ids) + 1
                    return f"u{novo_id:03d}"        

    # Estrutura do documento json (como serão salvos e lidos os dados):

    ### Como o JSON vai SALVAR os dados
    def salvar_usuario(self):
            if os.path.exists(LOGIN_CLIENTE):
                with open(LOGIN_CLIENTE, "r") as f:
                    dados_completos = json.load(f)
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
    def carregar_usuarios(self):
        if os.path.exists(LOGIN_CLIENTE):
            with open(LOGIN_CLIENTE, "r") as f:
                dados_completos = json.load(f)
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
            else:
                senha = input("Insira uma senha: ")
                senha = int(self.senha)
                if senha:
                    print("Cadastro realizado com sucesso!")
        except ValueError:
            print("Insira caracteres numéricos para senha.")        








        #if any(user['nome'] == nome for user in todos_usuarios.values()):
        for user_id, user_data in todos_usuarios.items():
            if user_data["nome"] == nome:
                print(f"Usuário já cadastrado com ID {user_id}")
                return
        else:
            senha = getpass.getpass("\nInsira sua senha para cadastro 🔑: ")
            print("\nCadastro realizado com sucesso!")

    ### Efetuando login

    def logar():
        print("\n================== 🏦 BANCO PY ==================\n")
        print("Olá! 👋 Faça login para acessar a sua conta: \n")
        todos_usuarios = carregar_usuarios()
        
        print("Usuários Cadastrados no momento: (Apenas para testes)\n", todos_usuarios) # Apenas para testes
        nome = input("\nNome 👤 : ")
        senha = getpass.getpass("\nSenha 🔑: ")
        #if any(user['nome'] == nome for user in todos_usuarios.values()): # Percorra todos_usuarios.values e verifique se contém o nome
        for user_id, user_data in todos_usuarios.items():
            if user_data['nome'] == nome and user_data['senha'] == senha: 
                print("\nLogin efetuado com sucesso!")
                return user_id
        
        print("Senha incorreta.")
        return None

