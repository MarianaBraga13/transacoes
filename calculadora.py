from datetime import datetime
from registro_transacoes import salvar_patrimonio, carregar_patrimonio


def depositar(user_id):
    from cli_interativo import escolher_transacao
    dados = carregar_patrimonio(user_id)

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
                salvar_patrimonio(user_id)
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


def transferir(user_id):
    from cli_interativo import escolher_transacao
    dados = carregar_patrimonio(user_id)

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

def pagar_conta(user_id):
    from cli_interativo import escolher_transacao
    dados = carregar_patrimonio(user_id)

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
                    

                
                        
