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

def criar_usuario():
    print("\n================== 🏦 BANCO PY ==================\n")
    print("Área de Cadastro de Usuário (a)\n")
    usuarios = carregar_usuarios()
    nome = input("Insira seu primeiro nome: ")
    if nome in usuarios:
        print("Nome já cadastrado.")
    else:
        senha = getpass.getpass("Insira sua senha para cadastro: ")
        salvar_usuario(nome, senha)
        print("\nCadastro realizado com sucesso!")

### Efetuando login

def logar():
    print("\n================== 🏦 BANCO PY ==================\n")
    print("Área de login\n")
    usuarios = carregar_usuarios()
    
    print("Conteúdo de usuarios:", usuarios)
    nome = input("Nome: ")
    if nome in usuarios:
        senha = getpass.getpass("Senha: ")
        if senha == usuarios[nome]['senha']:
            print("\nLogin efetuado com sucesso!")
            return True 
        else:
            print("Senha incorreta.")
            return False
    else:
        print("Usuário não cadastrado.")
        return False
logar()
criar_usuario()
     
           


         
   
        
        
    
    


    

 
     
          


               
          
     
     

     
     
    
                    

              


                  
                  
                  

             
             
