from datetime import datetime
import os


def registrar_extrato(tipo, valor):
    data_hora = datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")
    with open("extrato.txt", "a") as f:
        f.write(f"{data_hora} {tipo.upper()}: R$ {valor:.2f}\n")

def mostrar_extrato():
        if os.path.exists("extrato.txt"):
            print("\n------------------ EXTRATO -----------------")
            with open("extrato.txt", "r") as f:
                print(f.read())

                
