class Produto:

    def __init__(self, nome: str, preco: float) -> None:    

        self.nome: str = nome
        self.preco: float =  preco

    def __repr__(self) -> str:

        return f"{self.nome} - {self.preco}"

class Carrinho:

    def __init__(self) -> None:

        self.__produtos: list = []

    def adicionar_produto(self, produto: Produto) -> None:

        if produto in self.__produtos:

            print("Produto já está no carrinho")

        else:

            self.__produtos.append(produto)
            print("Produto adicionado com sucesso!")

    def remover_produto(self, nome_produto: str) -> None:

        for produto in self.__produtos:

            if nome_produto == produto.nome:

                self.__produtos.remove(produto)
                print("Produto removido com sucesso!")
                return

      
        print("O produto já não está no carrinho")

    def __calcular_total(self) -> float:

        total: float = 0.0

        for produto in self.__produtos:

            total += produto.preco

        return total

    def exibir_carrinho(self) -> None:

        print("=" *15, "CARRINHO", "=" *15)

        for i, produto in enumerate(self.__produtos):

            print(f"{f"{i+1}. {produto}":^38}\n")

        print(f"{f"TOTAL = {self.__calcular_total()}":^38}")
        print("="*38)


banana = Produto("Banana", 10.00)
chocolate = Produto("Chocolate", 15.00)
pêra = Produto("Pêra", 8.00)
toddynho = Produto("Toddynho", 5.00)
treloso = Produto("Treloso", 3.00)

carrinho = Carrinho()

carrinho.adicionar_produto(banana)
carrinho.adicionar_produto(chocolate)
carrinho.adicionar_produto(pêra)
carrinho.adicionar_produto(toddynho)
carrinho.adicionar_produto(treloso)

carrinho.exibir_carrinho()

carrinho.remover_produto("Chocolate")

carrinho.exibir_carrinho()