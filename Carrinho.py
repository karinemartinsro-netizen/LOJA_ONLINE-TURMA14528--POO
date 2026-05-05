class CarrinhoDeCompras:
    def __init__(self):
        self.itens = []


    def adicionar_produto(self, produto):
        self.itens.append(produto)
        print (f"{produto.nome} Foi adicionado ao carrinho")


    def exibir_resumo(self):
        print("\n --- RESUMO DO CARRINHO ---")
        total = 0

        for item in self.itens:
            item.exibir_detalhes()
            totatl += item.get_preco()

        print(f"TOTAL Á PAGAR : R$ {total}")
        print("-" *45)

    def listar_produtos(self, produto):
        if not produto:
            print("O carrinho está vazio !")
            return
        
        for i, item in enumerate (self.itens):

    
    
    
    def deletar_produto(self, produto):
        self.itens
        if not self.itens:
            print("O carrinho está vazio !")
            return
        print("Selecione o item para excluir :")
        for i, item in enumerate (self.itens):
            opcao = item['Opção']

        try:
            indice = int(input("Digite o número do item que deseja excluir do carrinho?"))
            item_removido = self.itens.pop(indice)
            print("Feito, item deletado do carrinho !")

        except:
            print("Digite uma opção válida . ")