from cli_interativo import escolher_transacao
from cli_login import logar, cadastrar

if __name__ == "__main__":
    while True:
        print("\n======== Bem-vindo(a) ao Banco PY 🏦 ==================")
        opcao = input("Você já possui uma conta? 🔐 (s/n): ").strip().lower()

        if opcao == "s":
            if logar():
                escolher_transacao()
                break  # Sai do loop após transação
            else:
                print("\n❌ Login falhou. Tente novamente.")
        elif opcao == "n":
            cadastrar()
            print("\n✅ Agora vamos fazer o login...")
            if logar():
                escolher_transacao()
                break
        else:
            print("Opção inválida. Digite 's' para sim ou 'n' para não.")
  
  
    

    