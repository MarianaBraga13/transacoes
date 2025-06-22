from cli_interativo import escolher_transacao
import os
import json
import getpass
from cli_interativo import escolher_transacao

# Caminho do arquivo
ARQUIVO_USUARIOS = "usuarios.json"

# Estrutura do documento json (como serão salvos e lidos os dados):

### Como o JSON vai LER os dados

def carregar_usuarios():
    if os.path.exists(ARQUIVO_USUARIOS):
        with open(ARQUIVO_USUARIOS, "r") as f:
            return json.load(f)
    return {} # Me retorne o que tiver dentro

### Como JSON vai salvar os dados

def salvar_usuarios(usuarios):
    with open(ARQUIVO_USUARIOS, "w") as f:
        json.dump(usuarios, f, indent=4)

# Como vai funcionar o cadastro:

def cadastrar_usuario():
    print("\n================== 🏦 BANCO PY ==================\n")
    print("Área de Cadastro de Usuário (a)\n")
    usuarios = carregar_usuarios() # Carrego usuários para verificarem se já existem
    username = input("Cadastro de Usuário (a).\nEscolha o nome do usuário (a):\n")
    
    if username in usuarios:
        print("Usuário (a) já existe.")
        return
    else:
        senha = getpass.getpass("Crie uma senha: ")
        usuarios[username] = {'senha': senha} # Enviar para o ARQUIVO_USUARIOS dessa forma
        salvar_usuarios()
        print("Usuário (a) cadastrado (a) com sucesso.\n Bem vindo (a) ao Banco Py")

# Como vai fazer login

def fazer_login():
    print("\n================== 🏦 BANCO PY ==================\n")
    print("Área de login\n")
    usuarios = carregar_usuarios()
    username = input("Usuário (a): ")

    if username not in usuarios:
        print("Usuário (a) não cadastrado (a)") 
        return   

    else:
        senha = getpass.getpass("Senha: ")

        if senha == usuarios[username]['senha']:
            print(f"Login efetuado com sucesso. Bem vindo (a), {username}")
            return
        else:
            print("Senha incorreta.")
            return




        
        
