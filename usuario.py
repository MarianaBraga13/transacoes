import os
import json
from datetime import datetime

ARQUIVO_DADOS = "patrimonio.json"

class Usuario:
    def __init__(self, user_id, nome=None): # O argumento nome=None é opcional aqui e vem do login
        self.user_id = user_id
        self.nome = nome
        self.patrimonio = 0.0
        self.historico = []
        self.limite_cartao = 0.0
        self.limite_emprestimo = 0.0
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
                        self.limite_cartao = dados_usuario.get("cartao")
                        self.limite_emprestimo = dados_usuario.get("emprestimo")
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
                "historico" : self.historico,
                "cartao" : self.limite_cartao,
                "emprestimo" : self.limite_emprestimo
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

    def emprestar(self, valor):
            if 0 <= valor <= self.limite_emprestimo:
                self.limite_emprestimo -= valor
                self.historico.append({
                    "data": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    "tipo": "emprestimo",
                    "valor": valor
                })
                self.salvar_dados()
                return True
            else:
                return False

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
        if self.analisar_credito():
            print("\nCartão aprovado, confira os valores de crédito na opção: 'Análise de Crédito'")
        else:
            print("\nCartão em análise, por favor acompanhe seu status na opção 'Análise de Crédito'")
    

    def analisar_credito(self):
        def analisar_frequencia():
            if len(self.historico) >= 5:
                return True
                
        if not analisar_frequencia():
            print(f"\nCliente {getattr(self, 'nome', self.user_id)}, sua solicitação de 🧠 Análise de Crédito foi recebida.\n"
                  "No momento, não há dados suficientes para gerar uma análise detalhada.\n"
                    "Realize mais movimentações para receber uma oferta personalizada. 🚀")
        else:
            #print(f"\n🧠 Análise de Crédito para {getattr(self, 'nome', self.user_id)}:")
            print(f"\n🧠Análise de Crédito para {self.nome}:")
            if self.patrimonio >= 5000:
                self.limite_cartao = 3000
                limite_total = 10000
            elif self.patrimonio >= 2000:
                self.limite_cartao = 1500
                limite_total = 5000
            elif self.patrimonio >= 500:
                self.limite_cartao = 800
                limite_total = 2000
            else:
                self.limite_cartao = 300
                limite_total = 1000

            emprestimos_usados = sum(item["valor"] for item in self.historico if item["tipo"] == "emprestimo"
            )
            self.limite_emprestimo = max(0, limite_total - emprestimos_usados)
            self.salvar_dados()

            print(f"💳 Limite pré-aprovado (Cartão): R$ {self.limite_cartao:.2f}")
            print(f"💸 Limite total aprovado (Empréstimo): R$ {limite_total:.2f}")
            print(f"💸 Limite atualizado (Empréstimo): R$ {self.limite_emprestimo:.2f}")
            print("==============================================================\n")
            return True        

    def exibir_dashboard(self):
            self.carregar_dados()
            print("\n================== 📊 DASHBOARD FINANCEIRO ==================")
            print(f"👤 Cliente: {self.user_id} {self.nome}")
            print(f"💰 Saldo atual: R$ {self.patrimonio:.2f}")
            print(f"📄 Limite para empréstimo: R$ {self.limite_emprestimo:.2f}")

            print("\n📈 Últimas transações:")
            ultimas_transacoes = self.historico[-3:] if self.historico else []
            if ultimas_transacoes:
                for item in ultimas_transacoes:
                    print(f"{[item['data']]} {item['tipo'].capitalize()}: R$ {item['valor']:.2f}")
                print("\n==========================================\n")    
    
            if not self.historico:    
                print("\nNenhuma transação registrada ainda.")
                

        
            

        
            



