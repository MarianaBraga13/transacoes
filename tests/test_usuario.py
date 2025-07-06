import os
import json
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from usuario import Usuario
import pytest

ARQUIVO_TESTE = "teste_patrimonio.json"

class UsuarioTeste(Usuario):
    def __init__(self, user_id, nome=None): # O argumento nome=None é opcional aqui e vem do login
        self.user_id = user_id
        self.nome = nome
        self.patrimonio = 0.0
        self.historico = []
        self.limite_cartao = 0.0
        self.limite_emprestimo = 0.0
        self.arquivo = ARQUIVO_TESTE
        self.carregar_dados()

    # para não afetar o banco de dados original
    def carregar_dados(self):
        if os.path.exists(self.arquivo):
            try:
                with open(ARQUIVO_TESTE, "r") as f:
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
        dados_completos = {}
        if os.path.exists(self.arquivo):
            try:
                with open(self.arquivo, "r") as f:
                    dados_completos = json.load(f)

            except json.JSONDecodeError:
                print("\nErro ao carregar dados. Arquivo corrompido!")                
        
        dados_completos[self.user_id] = {
                "patrimonio" : self.patrimonio,
                "historico" : self.historico,
                "cartao" : self.limite_cartao,
                "emprestimo" : self.limite_emprestimo
            }
        with open(ARQUIVO_TESTE, "w") as f:
                json.dump(dados_completos, f, indent=4)
    

@pytest.fixture

# garantindo que o arquivo esteja limpo
def usuario_limpo():
    if os.path.exists(ARQUIVO_TESTE):
        os.remove(ARQUIVO_TESTE)
    return UsuarioTeste("teste01", "Teste Usuario")

# chamo a função usuario_limpo para usa-la:

def test_deposito(usuario_limpo):
    usuario = usuario_limpo
    usuario.depositar(400)
    assert usuario.patrimonio == 400
    assert len(usuario.historico) == 1
    assert usuario.historico[0]["tipo"] == "depósito"    

def test_transferencia(usuario_limpo):
    usuario = usuario_limpo
    usuario.depositar(400)
    usuario.transferir(200)
    assert usuario.patrimonio == 200
    assert len(usuario.historico) == 2
    assert usuario.historico[0]["tipo"] == "depósito"
    assert usuario.historico[1]["tipo"] == "transferência"

def test_pagamento(usuario_limpo):
    usuario = usuario_limpo
    usuario.depositar(100)
    usuario.pagar_conta(100)
    assert usuario.patrimonio == 0
    assert len(usuario.historico) == 2
    assert usuario.historico[0]["tipo"] == "depósito"
    assert usuario.historico[1]["tipo"] == "pagamento"

def test_emprestimo_nocred(usuario_limpo):
    usuario = usuario_limpo
    usuario.depositar(2345)
    usuario.pagar_conta(345)
    assert usuario.patrimonio == 2000
    assert usuario.historico[0]["tipo"] == "depósito"
    assert usuario.historico[1]["tipo"] == "pagamento"
    print("❌ Valor inválido ou crédito insuficiente.\nCaso ainda não tenha acesso ao serviço, solicite uma análise de crédito.\n")
    resultado = usuario.emprestar
    assert not resultado is False


def test_emprestimo_cred(usuario_limpo):
    usuario = usuario_limpo
    usuario.depositar(2345)
    usuario.pagar_conta(345)
    usuario.depositar(500)
    usuario.transferir(500)
    usuario.transferir(500)
    usuario.emprestar(456)
    assert usuario.patrimonio == 1500
    assert usuario.historico[0]["tipo"] == "depósito"
    assert usuario.historico[1]["tipo"] == "pagamento"
    assert usuario.historico[2]["tipo"] == "depósito"
    assert usuario.historico[3]["tipo"] == "transferência"
    assert usuario.historico[4]["tipo"] == "transferência"
    assert usuario.historico[5]["tipo"] == "emprestimo"


