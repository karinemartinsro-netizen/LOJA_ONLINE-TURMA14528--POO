from Roupa import Roupa
from Eletronico import Eletronico
from Carrinho import CarrinhoDeCompras


def exibir_menu():
    print("\n" + "="*45)
    print("MENU DA LOJA ONLINE")
    print("=" *45)
    print("[1] Adicionar Roupa ")
    print("[2] Adicionar Eletrônico ")
    print("[3] Ver resumo do carrinho ")
    print("[0] Sair do sistema ")
    print("=" *45)

def main():
    carrinho = CarrinhoDeCompras()
    print("\n Bem vindo ao Sistema de vendas online")

    while True:
        exibir_menu()
        opcao = input ("Escolha uma opção :")

        if opcao == "1":
            print("\n----Cadastrando Roupa ----")
            nome = input("Nome da Roupa : ")

            try:
                preco = float(input("Preço: R$ "))
                tamanho = input("Tamanho (P/M/G) : ")
                nova_roupa = Roupa(nome, preco, tamanho)
                carrinho.adicionar_produto(nova_roupa)
            except ValueError:
                print("Erro, por favor digite um valor numérico válido para o preço ! ")


        elif  opcao =="2":
            print("\n ----- CADASTRANDO ELETRÔNICO  -----")
            nome = input ("Nome do eletrênico ")
            try: 
                preco = float (input("Preço : R$ "))
                voltagem = input("Voltagem (Ex. 110V/220V) : ")
                novo_eletronico = Eletronico(nome, preco, voltagem)
                carrinho.adicionar_produto(novo_eletronico)
            
            except ValueError:
                print("Erro, por favor digite um valor numérico válido para o preço ! ")

        elif opcao == "3" :
            carrinho.exibir_resumo()

        elif opcao == "0" :
            print("Encerrando o sistema, até logo! ")

        else : 
            print("Opção inválida, escolha uma opção de 0 á 3 !!!")
        
if __name__ == "__main__":
    main()