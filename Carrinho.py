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
