from __future__ import annotations

class Usuario:

    def __init__(self, nome: str, dinheiro: float) -> None:

        self._nome: str = nome
        self._dinheiro: float = dinheiro
        self._mochila: list = []

    def adicionar_item(self, item: Produto) -> None:

        self._mochila.append(item)

    def pagar(self, preço: float) -> None:

        self._dinheiro -= preço
        print(f"Foi removido {preço} R$ do total")

    def devolver_dinheiro(self, valor: float) -> None:

        self._dinheiro += valor
        print(f"Você recebeu {valor} R$")

    def get_dinheiro(self) -> float:

        return self._dinheiro

    def exibir_mochila(self) -> None:

        for i, item in enumerate(self._mochila):

            print(f"{i+1} - {item}")

    def ver_carteira(self) -> None:

        print(f"Você possui {self._dinheiro} R$")
    
class Produto:

    def __init__(self, nome:str, preço: float, quantidade: int) -> None:

        self._nome: str = nome
        self._preço: float = preço
        self._quantidade: int = quantidade

    def __repr__(self) -> str:

        return f"{self._nome} - {self._preço} R$ - {self._quantidade}"

    def get_nome(self) -> str:

        return self._nome

    def get_preço(self) -> float:

        return self._preço

    def get_quantidade(self) -> int:

        return self._quantidade

    def add_quant(self, adicional: int) -> None:

        self._quantidade += adicional

    def comprado(self) -> None:

        self._quantidade -= 1

class Maquina:

    def __init__(self) -> None:

        self._itens: list = []
        self._saldo_inserido: float = 0.0

    def reg_item(self, item: Produto) -> None:

        if item in self._itens:

            print(f"Item já está no estoque, caso deseja adicionar mais itens use maquina.adicionar_prod(produto, quantidade)")

        else:

            self._itens.append(item)

    def colocar_dinheiro(self, comprador: Usuario, valor: float):

        if comprador.get_dinheiro() >= valor:

            self._saldo_inserido += valor
            comprador.pagar(valor)

        else:

            print("Dinheiro insuficiente")

    def comprar(self, comprador: Usuario, item: str) -> None:

        for itens in self._itens:

            if itens.get_nome() == item:

                if self._saldo_inserido >= itens.get_preço():

                    if itens.get_quantidade() >= 1:

                        print(f"Você comprou um {item}")
                        itens.comprado()
                        comprador.adicionar_item(itens)
                        comprador.devolver_dinheiro(max(0, self._saldo_inserido - itens.get_preço()))
                        self._saldo_inserido = 0
                        return 0

                    else:

                        print(f"Desculpe não temos {item} no momento")
                        comprador.devolver_dinheiro(self._saldo_inserido)
                        self._saldo_inserido = 0
                        return 0
                else:

                    print("Dinheiro insuficiente")
                    comprador.devolver_dinheiro(self._saldo_inserido)
                    self._saldo_inserido = 0
                    return 0
                
        print(f"Desculpe não vendemos {item}")
        comprador.devolver_dinheiro(self._saldo_inserido)
        self._saldo_inserido = 0

    def exibir_estoque(self) -> None:

        for i, item in enumerate(self._itens):

            print(f"{i+1} - {item}")

    def adicionar_prod(self, produto: Produto, quantidade: int) -> None:

        produto.add_quant(quantidade)

if __name__ == "__main__":

    # Instanciando os objetos
    maquina = Maquina()
    user = Usuario("Paulo", 312313)
    coca = Produto("Coca", 54, 1000)
    chips = Produto("Doritos", 8.0, 1)
    agua = Produto("Água Mineral", 3.0, 0)

    # cadastro e avisos de duplicidade
    maquina.reg_item(coca)
    maquina.reg_item(chips)
    maquina.reg_item(agua)
    maquina.reg_item(coca)

    maquina.exibir_estoque()
    user.exibir_mochila()
    user.ver_carteira()

    # tentativa de compra sem saldo
    maquina.comprar(user, "Coca")
    maquina.comprar(user, "Água Mineral")

    # inserção de dinheiro e compras com sucesso e troco
    maquina.colocar_dinheiro(user, 1000)
    user.ver_carteira()
    maquina.comprar(user, "Coca")

    maquina.colocar_dinheiro(user, 1000)
    maquina.comprar(user, "Doritos")

    # inserção de dinheiro em item sem estoque (Devolução)
    maquina.colocar_dinheiro(user, 1000)
    maquina.comprar(user, "Água Mineral")

    # exibição do estado final
    maquina.exibir_estoque()
    user.exibir_mochila()
    user.ver_carteira()