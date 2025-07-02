from login import Login
from usuario import Usuario
from cli_interativo import escolher_transacao
from utils.criar_banco import criar_banco

def iniciar_transacao():
    # Reflexão para estudo, pensando em classe == "mochila da vida real".
    # o Login passa a "mochila" - user_id - (onde cabem todos os selfs) para login
    # login insere o user_id executando a função logar()
    # se o usuário logou então ele vai usar a class Usuario com user_id (ou seja, juntamos as duas classes aqui)
    # que vai escolher a transação com a nova "mochila" - usuario
    # A linha usuario = Usuario(user_id) - Junta as duas "mochilas"(classes) em uma só
    login = Login()
    user_id, nome = login.logar() # momento em que já pegou tudo que precisava e colocou na mochila
    if user_id: # Se conseguiu logar
        usuario = Usuario(user_id, nome) # Junta as mochilas
        escolher_transacao(usuario) # numa única chamada usuario para que caibam mais infos sobre ele
        return True
    return False

if __name__ == "__main__":
    criar_banco()
    while True:
        print("\n======== Bem-vindo(a) ao Banco PY 🏦 ==================")
        opcao = input("Você já tem conta? (s/n): ").lower()

        if opcao == "s":
            if iniciar_transacao():
                break
        elif opcao == "n":
            login = Login()
            login.cadastrar()
            if iniciar_transacao():
                break
        else:
            print("Opção inválida. Digite 's' ou 'n'.")
