import Transacoes

def escolher_transacao():
    while True:
        print("\n================== 🏦 BANCO PY ==================")
        resposta = input(
            "Escolha uma opção:\n"
            "1️⃣  Depositar 💰\n"
            "2️⃣  Transferir 💸\n"
            "3️⃣  Empréstimo 💵\n"
            "4️⃣  Solicitar Cartão de Crédito 💳\n"
            "5️⃣  Pagar Conta 🧾\n"
            "6️⃣  Gerar Extrato 📄\n"
            "7️⃣  Sair com Saldo Final 🚪\n"
            "🔀 "
        )    

        if resposta.isdigit():
            resposta = int(resposta)
            if resposta == 1:
                Transacoes("deposito").executar()
            elif resposta == 2:
                Transacoes("transferencia").executar()
            elif resposta == 3:
                Transacoes("emprestimo").executar()
            elif resposta == 4:
                Transacoes("cartao").executar()
            elif resposta == 5:
                Transacoes("pagamento").executar()
            elif resposta == 6:
                mostrar_extrato()
            elif resposta == 7:
                dados = carregar_patrimonio()
                print("\n----------------------- SALDO FINAL -----------------------\n")
                print(f"Patrimônio final nesta instituição financeira: R${dados['patrimonio']:.2f}")
                break 
            else:
                print("Digite uma opção válida.")    
        else:
            print("Digite um número.")
