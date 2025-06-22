from datetime import datetime
from registro_transacoes import salvar_patrimonio, carregar_patrimonio, mostrar_extrato


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
            "👉 "
            )    

        if resposta.isdigit():
            resposta = int(resposta)
            if 1 <= resposta <= 7:
                if resposta == 1:
                    return depositar()                
                elif resposta == 2:
                    return transferir()
                elif resposta == 3:
                    return solicitar_emprestimo() 
                elif resposta == 4:
                    return solicitar_cartao()
                elif resposta == 5:
                    return pagar_conta()
                elif resposta == 6:
                    return mostrar_extrato()
                elif resposta == 7:
                    dados = carregar_patrimonio()
                    print("\n-------------------- SALDO FINAL ------------------\n")
                    print(f"Saldo final no Banco Py: R${dados["patrimonio"]:.2f}")
                    break 
            else:
                print("Digite uma opção válida.")    
        else:
            print("Digite um número.")            
    

def depositar():
    dados = carregar_patrimonio()

    while True:
        deposito = input("Digite o valor para o depósito:\nR$ ")

        try:
            deposito = float(deposito)
            if deposito > 0:
                dados["patrimonio"] += deposito
                dados["historico"].append({
                    "data": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    "tipo": "depósito",
                    "valor": deposito
                })
                salvar_patrimonio(dados)
                print(f"Depósito recebido com sucesso no valor de: R${deposito:.2f}")
                print(f"Novo Saldo: R${dados['patrimonio']:.2f}")
                resposta = input("Qualquer tecla para continuar | (S) para sair: ")
                if resposta.upper() == "S":
                    print("\n================== 🏦 BANCO PY ==================")
                    print("\nObrigada por utilizar nossos serviços! Até breve.")
                    break
                else:
                    return escolher_transacao()
            else:
                print("Digite um valor maior que zero.")
        except ValueError:
            print("Digite apenas números válidos. Ex: 10.00, 50.5, etc.")


def transferir():
    dados = carregar_patrimonio()

    while True:
        transferencia = input("Insira o valor da transferência:\nR$ ")
        try:
            transferencia = float(transferencia)
            if 0 <= transferencia <= dados["patrimonio"]:
                dados["patrimonio"] -= transferencia
                dados["historico"].append({
                    "data": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    "tipo": "transferencia",
                    "valor": transferencia
                })
                salvar_patrimonio(dados)
                print(f"Transferência realizada com sucesso no valor de: R${transferencia:.2f}")
                print(f"Novo Saldo: R${dados['patrimonio']:.2f}")
                resposta = input("Qualquer tecla para continuar | (S) para sair:")
                if resposta.upper() == "S":
                    print("\n================== 🏦 BANCO PY ==================")
                    print("\nObrigada por utilizar nossos serviços! Até breve.")
                    break
                else:
                    return escolher_transacao()
            else:
                print("Saldo insuficiente.")
        except ValueError:
            print("Digite um valor numérico válido.")

def pagar_conta():
    dados = carregar_patrimonio()

    while True:
        pagamento = input("Insira o valor do Pagamento:\nR$ ")
        try:
            pagamento = float(pagamento)
            if 0 <= pagamento <= dados["patrimonio"]:
                dados["patrimonio"] -= pagamento
                dados["historico"].append({
                    "data": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    "tipo": "pagamento",
                    "valor": pagamento
                })
                salvar_patrimonio(dados)
                print(f"Pagamento realizado com sucesso no valor de: R${pagamento:.2f}")
                print(f"Novo Saldo: R${dados['patrimonio']:.2f}")
                resposta = input("Qualquer tecla para continuar | (S) para sair:")
                if resposta.upper() == "S":
                    print("\n================== 🏦 BANCO PY ==================")
                    print("\nObrigada por utilizar nossos serviços! Até breve.")
                    break
                else:
                    return escolher_transacao()
            else:
                print("Saldo insuficiente.")
        except ValueError:
            print("Digite um valor numérico válido.")


def solicitar_cartao():
    return print("Serviço indisponível.")      

def solicitar_emprestimo():
    return print("Serviço indisponível.")
                    

                
                        
