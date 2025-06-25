from datetime import datetime

def depositar(self, valor):
        if valor > 0:
            self.patrimonio += valor
            self.historico.append({
                "data": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "tipo": "depósito",
                "valor": valor
            })
            self.salvar_dados()
            print(f"✅Depósito recebido com sucesso no valor de: R${valor:.2f}")
            print(f"✅Novo Saldo: R${self.patrimonio:.2f}")
        else:
            print("❌Valor inválido para depósito.")


def transferir(self, valor):
    if 0 < valor <= self.patrimonio:
        self.patrimonio -= valor
        self.historico.append({
            "data": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "tipo": "transferência",
            "valor": valor
        })
        self.salvar_dados()
        print(f"✅Transferência de R${valor:.2f} realizada com sucesso!")
        print(f"✅Novo saldo: R${self.patrimonio:.2f}")
    else:
        print("❌Valor inválido ou saldo insuficiente.")


def pagar_conta(self, valor):
        if 0 <= valor <= self.patrimonio:
            self.patrimonio -= valor
            self.historico.append({
                "data": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "tipo": "valor",
                "valor": valor
            })
            self.salvar_dados()
            print(f"✅Pagamento realizado com sucesso no valor de: R${valor:.2f}")
            print(f"✅Novo Saldo: R${self.patrimonio:.2f}")
        else:
            print("❌Saldo insuficiente ou valor inválido.")



def solicitar_cartao(self):
    return print("Serviço indisponível.")      

def solicitar_emprestimo(self):
    return print("Serviço indisponível.")
                    

                
                        
