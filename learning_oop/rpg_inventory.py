class Item:

    def __init__(self, nome: str, peso: float, raridade: str) -> None:

        self._nome: str = nome
        self._peso: float = peso
        self._raridade: str = raridade

    def __repr__(self) -> str:

        return f"{self._nome}\n-Peso: {self._peso}\n-Raridade: {self._raridade}"

    def get_peso(self) -> float:

        return self._peso

    def get_nome(self) -> str:

        return self._nome

class Arma(Item):

    def __init__(self, nome: str, dano: float, peso: float, raridade: str) -> None:

        super().__init__(nome, peso, raridade)

        self._dano: float = dano

    def __repr__(self) -> str:

        return f"{self._nome}\n-Dano: {self._dano}\n-Peso: {self._peso}\n-Raridade: {self._raridade}"

class Pocao(Item):

    def __init__(self, nome: str, peso: float, raridade: str) -> None:

        super().__init__(nome, peso, raridade)

    def __repr__(self) -> str:

        return super().__repr__()

class Personagem:

    def __init__(self, capacidade_maxima: float =25.0) -> None:

        self.capacidade_maxima: float = capacidade_maxima
        self._itens: list = []

    def _calcular_peso(self) -> float:

        peso_atual = 0
        
        for item in self._itens: 
                        
            peso_atual += item.get_peso()

        return peso_atual

    def adicionar_item(self, item: Item) -> None:

        permissão = self._calcular_peso()

        if permissão + item.get_peso() > self.capacidade_maxima:

            print("Você não consegue carregar esse item!\n")

        else:

            print("Item adicionado com sucesso!\n")
            self._itens.append(item)

    def remover_item(self, nome_item: str) -> None:

        for item in self._itens:

            if item.get_nome() == nome_item:

                self._itens.remove(item)
                print("Item removido da mochila!\n")
                return

        print("Item não encontrado na mochila!\n")

    def exibir_inventario(self) -> None:

        print("="*15, "INVENTARIO", "="*15, "\n")

        for i, item in enumerate(self._itens):

            print(f"{i+1} - {item}\n")

        print(f"Capacidade: {self._calcular_peso()}/{self.capacidade_maxima}\n")
        print("="*42, "\n")

if __name__ == "__main__":

    # Instanciando os objetos
    Rogerio = Personagem()
    espada_de_fogo = Arma("espada flamejante", 25.0, 5.0, "épica")
    poção_de_vida = Pocao("poção de vida", 0.5, "comum")
    minigun = Arma("minigun", 100.0, 20.5, "lendária")

    # testando a função de adicionar
    Rogerio.adicionar_item(espada_de_fogo)
    Rogerio.adicionar_item(poção_de_vida)
    Rogerio.exibir_inventario()

    # testando a função de controle de peso
    Rogerio.remover_item("espada flamejante")
    Rogerio.adicionar_item(minigun)
    Rogerio.exibir_inventario()
    Rogerio.remover_item("poção de vida")
    Rogerio.adicionar_item(espada_de_fogo)
    Rogerio.exibir_inventario()