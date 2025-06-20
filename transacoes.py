from datetime import datetime
from gerar_extrato import mostrar_extrato, registrar_extrato
from gerar_saldo import salvar_patrimonio, carregar_patrimonio
from painel_interativo import escolher_transacao


class Transacoes:
    def __init__(self, tipo):
        self.tipo = tipo.lower()
        self.dados = carregar_patrimonio()

    def executar(self):
        patrimonio = self.dados["patrimonio"]

        valor = input(f"Digite o valor para {self.tipo}: R$ ")
        if not valor.replace('.', '', 1).isdigit():
            print("Digite apenas valores numéricos.")
            return

        valor = float(valor)

        if self.tipo in ["transferencia", "pagamento"] and valor > patrimonio:
            print("Saldo insuficiente.")
            return

        if valor <= 0:
            print("Digite um valor maior que zero.")
            return

        if self.tipo in ["transferencia", "pagamento"]:
            self.dados["patrimonio"] -= valor
        else:
            self.dados["patrimonio"] += valor

        self.dados["historico"].append({
            "data": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "tipo": self.tipo,
            "valor": valor
        })

        salvar_patrimonio(self.dados)
        registrar_extrato(self.tipo.capitalize(), valor)

        print(f"\n{self.tipo.capitalize()} realizado com sucesso no valor de: R${valor:.2f}")
        print(f"Novo Saldo: R${self.dados['patrimonio']:.2f}")

        resposta = input("\nQualquer tecla para continuar | (S) para sair:")
        if resposta.upper() == "S":
            print("\nObrigada por utilizar nossos serviços! Até breve.")
        else:
            escolher_transacao()


