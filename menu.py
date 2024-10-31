#funcao menu
#variavel operacao
#loop while para o programa funcionar ate ordem
#do usuario
import criar_campanha_phishing as cp
import monitorar_emails as me
import Analise_de_dados as ad
class menu:
    def __init__(self, opercacao, opcaodesejada):
        opercacao = opercacao
        opcaodesejada = opcaodesejada
    operacao = True
    while(operacao == True):
        opcao_desejada = int(input("Escolha a opcao desejada \n 1- Criar campanha de phishing \n 2- Monitorar emails \n 3- Analise de dados"))
        if(opcao_desejada == 1):
            campanha = cp.criar_campanha_phishing()
            print(campanha.campanha_de_phishing())
        elif(opcao_desejada == 2):
            monitorar = me.monitorar_emails()
            print(monitorar.monitoramento())
        elif(opcao_desejada == 3):
            analise = ad.analise_de_dados()
            print(analise.analise_de_dados())
        else:
            print("Opcao invalida, digite \n 1- Criar campanha de phishing \n 2- Monitorar emails \n 3- Analise de dados")
        coninuar = input("Deseja continuar no software?\n")
        if(coninuar == "s"):
            operacao = True
        else:
            operacao = False
