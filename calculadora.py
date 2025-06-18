# depósito
PATRIMONIO = 0.0

def depositar():
    global PATRIMONIO
    while True:
        deposito = input("Digite o valor para o depósito:\nR$")
        if deposito.isdigit():
            deposito = float(deposito)
            if deposito > 0:
                PATRIMONIO += deposito
                print("Depósito recebido com sucesso!")
                print(f"Seu patrimônio no momento é:R${PATRIMONIO:.2f}")
                break
            else:
                print("Digite um valor maior que zero.")
        else:
            print("Digite apenas valores numéricos.")

    return PATRIMONIO


                 

            
                     
