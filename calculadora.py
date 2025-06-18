import os

def escolher_transacao():
    while True:
        resposta = input("Olá, seja muito bem vindo (a) ao nosso banco Py.\n"
                         "Por favor, escolha entre as opções:\n1 - Depositar\n"
                         "2 - Transferir\n3 - Ver saldo\n4 - Sair\n")
        if resposta.isdigit():
            resposta = int(resposta)
            if 1 <= resposta <= 3:
                if resposta == 1:
                    return depositar()
                
                elif resposta == 2:
                    return transferir()
                
                elif resposta == 3:
                    return
                
                elif resposta == 4:
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
                print(f"Depósito recebido com sucesso no valor de:R${deposito:.2f}")
                print(f"Seu patrimônio no momento é:R${patrimonio:.2f}")
                break
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
                print(f"Transferência realizada com sucesso no valor de:R${transferencia:.2f}")
                break
            else:
                print("Saldo insuficiente.")
        else:
            print("Digite um valor.")        

    return patrimonio


                 

            
                     
