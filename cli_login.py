import os
import json
import getpass

LOGIN_CLIENTE = "dados_login.json"

class Login:
    def __init__(self, user_id, nome, senha):
        self.user_id = user_id
        self.nome = nome
        self.senha = senha


    def gerar_novo_id(usuarios):
        if not usuarios:
            return "u001"
        
        else:
            ids = [int(uuid[1:]) for uuid in usuarios.keys()]
            novo_id = max(ids) + 1
            return f"u{novo_id:03d}"

    # Estrutura do documento json (como serão salvos e lidos os dados):

    ### Como o JSON vai SALVAR os dados
    def salvar_usuario(nome, senha):
        usuarios = carregar_usuarios()
        novo_id = gerar_novo_id(usuarios)

        usuarios[novo_id] = {'nome': nome, 'senha' : senha}

        with open(LOGIN_CLIENTE, "w") as f:
            json.dump(usuarios, f, indent=4) 

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

    def cadastrar():
        print("\n================== 🏦 BANCO PY ==================\n")
        print("Área de Cadastro de Usuário (a)\n")
        usuarios = carregar_usuarios()
        nome = input("\nInsira seu Nome Completo 👤: ")
        #if any(user['nome'] == nome for user in usuarios.values()):
        for user_id, user_data in usuarios.items():
            if user_data["nome"] == nome:
                print(f"Usuário já cadastrado com ID {user_id}")
                return
        else:
            senha = getpass.getpass("\nInsira sua senha para cadastro 🔑: ")
            salvar_usuario(nome, senha)
            print("\nCadastro realizado com sucesso!")

    ### Efetuando login

    def logar():
        print("\n================== 🏦 BANCO PY ==================\n")
        print("Olá! 👋 Faça login para acessar a sua conta: \n")
        usuarios = carregar_usuarios()
        
        print("Usuários Cadastrados no momento: (Apenas para testes)\n", usuarios) # Apenas para testes
        nome = input("\nNome 👤 : ")
        senha = getpass.getpass("\nSenha 🔑: ")
        #if any(user['nome'] == nome for user in usuarios.values()): # Percorra usuarios.values e verifique se contém o nome
        for user_id, user_data in usuarios.items():
            if user_data['nome'] == nome and user_data['senha'] == senha: 
                print("\nLogin efetuado com sucesso!")
                return user_id
        
        print("Senha incorreta.")
        return None

