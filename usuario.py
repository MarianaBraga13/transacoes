import os
import json
from datetime import datetime

ARQUIVO_DADOS = "patrimonio.json"

class Usuario:
    def __init__(self, user_id, nome=None):
        self.user_id = user_id
        self.nome = nome
        self.patrimonio = 0.0
        self.historico = []
        self.carregar_dados()

    # persistência de dados

    def carregar_dados(self):
        if os.path.exists(ARQUIVO_DADOS):
            try:
                with open(ARQUIVO_DADOS, "r") as f:
                    dados_completos =  json.load(f)
                    dados_usuario = dados_completos.get(self.user_id)
                    if dados_usuario:
                        self.patrimonio = dados_usuario.get("patrimonio", 0.0)
                        self.historico = dados_usuario.get("historico", [])
            except json.JSONDecodeError:
                print("\nErro ao carregar dados. Arquivo corrompido!")

    def salvar_dados(self):
        if os.path.exists(ARQUIVO_DADOS):
            try:
                with open(ARQUIVO_DADOS, "r") as f:
                    dados_completos = json.load(f)

            except json.JSONDecodeError:
                print("\nErro ao carregar dados. Arquivo corrompido!")
                dados_completos = {}
        
        dados_completos[self.user_id] = {
                "patrimonio" : self.patrimonio,
                "historico" : self.historico
            }
        with open(ARQUIVO_DADOS, "w") as f:
                json.dump(dados_completos, f, indent=4)


    def mostrar_extrato(self):
        if not self.historico:
            print("\nNenhuma transação registrada até o momento.")
            return

        else:

            print("Agradecemos sua preferência em contar com os serviços financeiros do nosso Banco Py!\n 👋 Até breve!")
            print("\n=================== EXTRATO 📄 ===================\n")
            for item in self.historico:
                print(f"[{item['data']}] {item['tipo'].capitalize()}: R${item['valor']:.2f}")
            print(f"\n---------->Saldo final: R${self.patrimonio:.2f}")


    def depositar(self, valor):
            if valor > 0:
                self.patrimonio += valor
                self.historico.append({
                    "data": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    "tipo": "depósito",
                    "valor": valor
                })
                self.salvar_dados()
                print(f"✅ Depósito recebido com sucesso no valor de: R${valor:.2f}")
                print(f"✅ Novo Saldo: R${self.patrimonio:.2f}")
            else:
                print("❌ Valor inválido para depósito.")


    def transferir(self, valor):
        if 0 < valor <= self.patrimonio:
            self.patrimonio -= valor
            self.historico.append({
                "data": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "tipo": "transferência",
                "valor": valor
            })
            self.salvar_dados()
            print(f"✅ Transferência de R${valor:.2f} realizada com sucesso!")
            print(f"✅ Novo saldo: R${self.patrimonio:.2f}")
        else:
            print("❌ Valor inválido ou saldo insuficiente.")


    def pagar_conta(self, valor):
            if 0 <= valor <= self.patrimonio:
                self.patrimonio -= valor
                self.historico.append({
                    "data": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    "tipo": "pagamento",
                    "valor": valor
                })
                self.salvar_dados()
                print(f"✅ Pagamento realizado com sucesso no valor de: R${valor:.2f}")
                print(f"✅ Novo Saldo: R${self.patrimonio:.2f}")
            else:
                print("❌ Saldo insuficiente ou valor inválido.")


    def solicitar_cartao(self):
        return print("Serviço indisponível.")      

    def solicitar_emprestimo(self):
        return print("Serviço indisponível.")
    

    def analisar_credito(self):
        def analisar_frequencia():
            if len(self.historico) >= 5:
                return True
        if not analisar_frequencia():
            print(f"\nCliente {getattr(self, 'nome', self.user_id)}, sua solicitação de 🧠 Análise de Crédito foi recebida.\n"
                  "No momento, não há dados suficientes para gerar uma análise detalhada.\n"
                    "Realize mais movimentações para receber uma oferta personalizada. 🚀")
            return

        else:
            #print(f"\n🧠 Análise de Crédito para {getattr(self, 'nome', self.user_id)}:")
            print(f"\n🧠Análise de Crédito para {self.nome}:")
            if self.patrimonio >= 5000:
                limite_cartao = 3000
                limite_emprestimo = 10000
            elif self.patrimonio >= 2000:
                limite_cartao = 1500
                limite_emprestimo = 5000
            elif self.patrimonio >= 500:
                limite_cartao = 800
                limite_emprestimo = 2000
            else:
                limite_cartao = 300
                limite_emprestimo = 1000                 

            print(f"   💳 Limite pré-aprovado (Cartão): R$ {limite_cartao:.2f}")
            print(f"   💸 Limite sugerido (Empréstimo): R$ {limite_emprestimo:.2f}")
            print("==============================================================\n")


    def exibir_dashboard(self):
            print("\n================== 📊 DASHBOARD FINANCEIRO ==================")
            print(f"👤 Cliente: {self.user_id} {self.nome}")
            print(f"💰 Saldo atual: R$ {self.patrimonio:.2f}")
            print("\n📈 Últimas transações:")
            ultimas_transacoes = self.historico[-3:] if self.historico else []
            if ultimas_transacoes:
                for item in ultimas_transacoes:
                    print(f"{[item['data']]} {item['tipo'].capitalize()}: R$ {item['valor']:.2f}")
                print("\n==========================================\n")    
    
            if not self.historico:    
                print("\nNenhuma transação registrada ainda.")
                

        
            

        
            



