from calculadora import depositar, transferir, pagar_conta, solicitar_cartao,solicitar_emprestimo
from registro_transacoes import mostrar_extrato, carregar_patrimonio



def escolher_transacao(user_id):
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
            "👉 "
            )    

        if resposta.isdigit():
            resposta = int(resposta)
            if 1 <= resposta <= 7:
                if resposta == 1:
                    return depositar(user_id)                
                elif resposta == 2:
                    return transferir(user_id)
                elif resposta == 3:
                    return solicitar_emprestimo(user_id) 
                elif resposta == 4:
                    return solicitar_cartao(user_id)
                elif resposta == 5:
                    return pagar_conta(user_id)
                elif resposta == 6:
                    return mostrar_extrato(user_id)
                elif resposta == 7:
                    dados = carregar_patrimonio(user_id)
                    print("\n-------------------- SALDO FINAL ------------------\n")
                    print(f"Saldo final no Banco Py: R${dados["patrimonio"]:.2f}")
                    break 
            else:
                print("Digite uma opção válida.")    
        else:
            print("Digite um número.")            
    