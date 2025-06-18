from calculadora import escolher_transacao, carregar_patrimonio



if __name__ == "__main__":
    escolher_transacao()

    patrimonio_atual = carregar_patrimonio()
    print(f"Patrimônio final nesta instituição financeira: R${patrimonio_atual:.2f}")