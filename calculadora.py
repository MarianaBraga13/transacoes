import os
from gerar_extrato import mostrar_extrato, registrar_extrato


def escolher_transacao():
    while True:
        print("\n================== 🏦 BANCO PY ==================")
        resposta = input(
            "Escolha uma opção:\n"
            "1️⃣  Depositar 💰\n"
            "2️⃣  Transferir 💸\n"
            "3️⃣  Gerar Extrato e Sair 📄\n"
            "4️⃣  Sair c/ Saldo Final 🚪\n"
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
                    return mostrar_extrato()
                
                elif resposta == 4:
                    patrimonio_atual = carregar_patrimonio()
                    print("\n------------------ SALDO FINAL -----------------\n")
                    print(f"Patrimônio final nesta instituição financeira: R${patrimonio_atual:.2f}")
                    break 
            else:
                print("Digite uma opção válida.")    
        else:
            print("Digite um número.")

# persistência de dados
def carregar_patrimonio():
    if os.path.exists("patrimonio.txt"):
        with open("patrimonio.txt", "r") as f:
            return float(f.read().strip())
    return 0.0

def salvar_patrimonio(valor):
    with open("patrimonio.txt", "w") as f:
        f.write(str(valor))      

def depositar():
    patrimonio = carregar_patrimonio()

    while True:
        deposito = input("Digite o valor para o depósito:\nR$ ")
        if deposito.isdigit():
            deposito = float(deposito)
            if deposito > 0:
                patrimonio += deposito
                salvar_patrimonio(patrimonio)
                registrar_extrato("Depósito", deposito)
                print(f"Depósito recebido com sucesso no valor de:R${deposito:.2f}")
                print(f"Seu patrimônio no momento é:R${patrimonio:.2f}")
                resposta = input("\nQualquer tecla para continuar | (S) para sair:")
                if resposta.upper() == "S":
                    print("Obrigada por utilizar nossos serviços! Até breve.")
                    break
                else:
                    return escolher_transacao()
            else:
                print("Digite um valor maior que zero.")
        else:
            print("Digite apenas valores numéricos.")

    return patrimonio

def transferir():
    patrimonio = carregar_patrimonio()

    while True:
        transferencia = input("Insira o valor da transferência:\nR$ ")
        if transferencia.isdigit():
            transferencia = float(transferencia)
            if 0 <= transferencia <= patrimonio:
                patrimonio -= transferencia
                salvar_patrimonio(patrimonio)
                registrar_extrato("Transferência", transferencia)
                print(f"Transferência realizada com sucesso no valor de:R${transferencia:.2f}")
                resposta = input("\nQualquer tecla para continuar | (S) para sair:")
                if resposta.upper() == "S":
                    print("Obrigada por utilizar nossos serviços! Até breve.")
                    break
                else:
                    return escolher_transacao()
            else:
                print("Saldo insuficiente.")
        else:
            print("Digite um valor.")        

    return patrimonio


                 

            
                     
