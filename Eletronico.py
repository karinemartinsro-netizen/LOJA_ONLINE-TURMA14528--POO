from Loja import Produto

class Eletronico(Produto):
    def __init__(self, nome, preco, voltagem):
        super().__init__(nome, preco)
        self.voltagem = voltagem

    def exibir_detalhes(self):
        print(f"Eletrônicos : {self.nome} ({self.voltagem}V) | Preço: R${self.get_preco()}")
