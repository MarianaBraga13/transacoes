import os
import getpass
import json

ARQUIVO_USUARIOS_TESTE = "usuarios_teste.json"

# Como o json vai carregar e como vai salvar os dados
def carregar_usuarios():
        if os.path.exists(ARQUIVO_USUARIOS_TESTE):
            with open(ARQUIVO_USUARIOS_TESTE, "r") as f:
                return json.load(f)
        else:
             return {}

        
def salvar_usuarios(usuarios):
     with open(ARQUIVO_USUARIOS_TESTE, "w") as f:
          json.dump(usuarios, f, indent=4)
                  
# Como vamos get(usuario)

def cadastrar_usuario():
     usuarios = (carregar_usuarios())
     usuario = input("Insira seu nome: ")
     if usuario in usuarios:
          print("Usuário (a) já cadastrado (a), digite sua senha.")
     else:
          senha = getpass.getpass("Digite sua senha: ")
          usuarios[usuario] = {'senha': senha} # Usuário recebe a senha e será salva junto ao seu correspondente
          salvar_usuarios(usuarios)
          print("Usuário (a) Cadastrado (a) com sucesso!")

def logar():
     usuarios = carregar_usuarios()
     usuario = input("Usuário (a): ")
     
     if usuario not in usuarios:
          print("Usuário (a) não cadastrado(a).")

     else:
          senha = getpass.getpass("Senha:")
          
          if senha == usuarios[usuario]['senha']:
            print(f"Login efetuado com sucesso. Bem vindo (a), {usuario}")
          else:
               print("Senha incorreta.")  

cadastrar_usuario()
logar()     
     



    

 
     
          


               
          
     
     

     
     
    
                    

              


                  
                  
                  

             
             
