# depósito

def depositar():
    while True:
        deposito = input("Digite o valor para o depósito:\nR$")
        if deposito.isdigit():
            deposito = float(deposito)
            if deposito > 0:
                print("Depósito recebido com sucesso!")
                break
            else:
                print("Digite um valor maior que zero.")
        else:
            print("Digite apenas valores numéricos.")

    return deposito
        
             

            
                     
