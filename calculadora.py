
from gerar_extrato import mostrar_extrato, registrar_extrato
from gerar_saldo import salvar_patrimonio, carregar_patrimonio


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
            if 1 <= resposta <= 4:
                if resposta == 1:
                    return depositar()
                
                elif resposta == 2:
                    return transferir()
                elif resposta == 3:
                    return
                elif resposta == 4:
                    return
                elif resposta == 5:
                    return pagar_conta()
                elif resposta == 6:
                    return mostrar_extrato()
                elif resposta == 7:
                    dados = carregar_patrimonio()
                    print("\n----------------------- SALDO FINAL -----------------------\n")
                    print(f"Patrimônio final nesta instituição financeira: R${dados["patrimonio"]:.2f}")
                    break 
            else:
                print("Digite uma opção válida.")    
        else:
            print("Digite um número.")            
    

def depositar():
    dados = carregar_patrimonio()
    patrimonio = dados["patrimonio"]

    while True:
        deposito = input("Digite o valor para o depósito:\nR$ ")
        if deposito.isdigit():
            deposito = float(deposito)
            if deposito > 0:
                dados["patrimonio"] += deposito
                salvar_patrimonio(dados)
                registrar_extrato("Depósito", deposito)
                print(f"Depósito recebido com sucesso no valor de:R${deposito:.2f}")
                print(f"Novo Saldo: R${dados["patrimonio"]:.2f}")
                resposta = input("\nQualquer tecla para continuar | (S) para sair:")
                if resposta.upper() == "S":
                    print("\nObrigada por utilizar nossos serviços! Até breve.")
                    break
                else:
                    return escolher_transacao()
            else:
                print("Digite um valor maior que zero.")
        else:
            print("Digite apenas valores numéricos.")

    return patrimonio

def transferir():
    dados = carregar_patrimonio()
    patrimonio = dados["patrimonio"]

    while True:
        transferencia = input("Insira o valor da transferência:\nR$ ")
        if transferencia.isdigit():
            transferencia = float(transferencia)
            if 0 <= transferencia <= patrimonio:
                dados["patrimonio"] -= transferencia
                salvar_patrimonio(dados)
                registrar_extrato("Transferência", transferencia)
                print(f"Transferência realizada com sucesso no valor de:R${transferencia:.2f}")
                print(f"Novo Saldo: R${dados["patrimonio"]:.2f}")
                resposta = input("\nQualquer tecla para continuar | (S) para sair:")
                if resposta.upper() == "S":
                    print("\nObrigada por utilizar nossos serviços! Até breve.")
                    break
                else:
                    return escolher_transacao()
            else:
                print("Saldo insuficiente.")
        else:
            print("Digite um valor.")        

    return patrimonio

def pagar_conta():
    dados = carregar_patrimonio()
    patrimonio = dados["patrimonio"]    

    while True:
            pagamento = input("Insira o valor do Pagamento:\nR$ ")
            dados = carregar_patrimonio()

            if pagamento.isdigit():
                pagamento = float(pagamento)
                if 0 <= pagamento <= patrimonio:
                    dados["patrimonio"] -= pagamento
                    salvar_patrimonio(dados)
                    registrar_extrato("Pagamentos", pagamento)
                    print(f"Pagamento realizado com sucesso no valor de:R${pagamento:.2f}")
                    print(f"Novo Saldo: R${dados["patrimonio"]:.2f}")
                    resposta = input("\nQualquer tecla para continuar | (S) para sair:")
                    if resposta.upper() == "S":
                        print("\nObrigada por utilizar nossos serviços! Até breve.")
                        break
                    else:
                        return escolher_transacao()
                else:
                    print("Saldo insuficiente.")
            else:
                print("Digite um valor.")        

    return patrimonio


                    

                
                        
