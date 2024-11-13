#funcao menu
#variavel operacao
#loop while para o programa funcionar ate ordem
#do usuario
import criar_campanha_phishing as cp
import monitorar_emails as me
import Analise_de_dados as ad
import os
from time import sleep

def opcoesMenu():
    print("Escolha a opcao desejada")
    print("1- Criar campanha de phishing")
    print("2- Monitorar emails")
    print("3- Analise de dados")

def limparTela():
    os.system('cls' if os.name == 'nt' else 'clear')

class menu():
    def __init__(self, opcaodesejada):
        opcaodesejada = opcaodesejada
    while True:
        opcoesMenu()
        opcao_desejada = int(input(">"))

        match(opcao_desejada):
            case 1:
                campanha = cp.criar_campanha_phishing()
                print(campanha.campanha_de_phishing())

            case 2:
                monitorar = me.monitorar_emails()
                print(monitorar.monitoramento())

            case 3:
                analise = ad.analise_de_dados()
                print(analise.analise_de_dados())

            case 1:
                campanha = cp.criar_campanha_phishing()
                print(campanha.campanha_de_phishing())

            case _:
                print("Opcao invalida")

        continuar = input("Deseja continuar no software? (S/N) :").lower()

        while continuar not in ("s","n"):
            print("Opção inválida. Digite 's' para continuar ou 'n' para sair.")
            continuar = input("Deseja continuar no software? (S/N) :").lower()
        

        if (continuar == "n"):
            print("Saindo da aplicação")
            sleep(3)
            break

        limparTela()

        
        
