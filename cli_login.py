import os
import json
import getpass

LOGIN_CLIENTE = "dados_login.json"
# Estrutura do documento json (como serão salvos e lidos os dados):

### Como o JSON vai SALVAR os dados
def salvar_usuario(nome, senha):
    usuarios = carregar_usuarios()
    usuarios[nome] = {'senha' : senha}
    with open(LOGIN_CLIENTE, "w") as f:
        json.dump(usuarios, f, indent=4) 

### Como o JSON vai LER os dados
def carregar_usuarios():
    if os.path.exists(LOGIN_CLIENTE):
        with open(LOGIN_CLIENTE, "r") as f:
            return json.load(f)
    return {}

### Cadastrando o usuário (a)

def cadastrar():
    print("\n================== 🏦 BANCO PY ==================\n")
    print("Área de Cadastro de Usuário (a)\n")
    usuarios = carregar_usuarios()
    nome = input("\n Insira seu Nome Completo 👤: ")
    if nome in usuarios:
        print("Nome já cadastrado.")
    else:
        senha = getpass.getpass("\n Insira sua senha para cadastro 🔑: ")
        salvar_usuario(nome, senha)
        print("\nCadastro realizado com sucesso!")

### Efetuando login

def logar():
    print("\n================== 🏦 BANCO PY ==================\n")
    print("Olá! 👋 Faça login para acessar a sua conta: \n")
    usuarios = carregar_usuarios()
    
    print("Usuários Cadastrados no momento: (Apenas para testes)\n", usuarios) # Apenas para testes
    nome = input("\nNome 👤 : ")
    if nome in usuarios:
        senha = getpass.getpass("\n Senha 🔑: ")
        if senha == usuarios[nome]['senha']:
            print("\nLogin efetuado com sucesso!")
            return True 
        else:
            print("Senha incorreta.")
            return False
    else:
        print("Usuário não cadastrado.")
        return False

     
           


         
   
        
        
    
    


    

 
     
          


               
          
     
     

     
     
    
                    

              


                  
                  
                  

             
             
