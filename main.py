from login import Login
from usuario import Usuario
from cli_interativo import escolher_transacao

def iniciar_transacao():
    login = Login()
    user_id = login.logar()
    if user_id:
        usuario = Usuario(user_id)
        escolher_transacao(usuario)
        return True
    return False

if __name__ == "__main__":
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
