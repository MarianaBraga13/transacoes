from cli_interativo import escolher_transacao
from teste_cli_login import Login
from  usuario import Usuario

def iniciar_transacao():
    user_id = Login
    if user_id:
        usuario = Usuario(user_id)
        escolher_transacao(usuario)
        return True
    else:
        print("\n❌ Login falhou. Tente novamente.")
        return False

if __name__ == "__main__":
    while True:
        print("\n======== Bem-vindo(a) ao Banco PY 🏦 ==================")
        opcao = input("Você já possui uma conta? 🔐 (s/n): ").strip().lower()
        
        if opcao == "s":
            if iniciar_transacao():
                break
        elif opcao == "n":
            Login()
            print("\n✅ Agora vamos fazer o login...")
            if iniciar_transacao():
                break
        else:
            print("Opção inválida. Digite 's' para sim ou 'n' para não.")
