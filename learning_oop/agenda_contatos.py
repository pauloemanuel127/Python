from __future__ import annotations

class Contato:

    def __init__(self, nome: str, numero: int) -> None:

        self.nome: str = nome
        self.__numero: int = numero

    def __repr__(self) -> str:

        return f"{self.nome}"

    def atualizar(self, novo_nome: str ="", novo_numero: int= 0) -> None:

        if novo_nome == "" and novo_numero == 0:

            return
        
        elif novo_nome == "":

            self.__numero: int = novo_numero

        elif novo_numero == 0:

            self.nome: str = novo_nome

        else:

            self.nome: str = novo_nome
            self.__numero: int = novo_numero

    def demonstrar(self) -> None:

        print(f"nome: {self.nome}; numero: {self.__numero}")
        
class Agenda:

    def __init__(self) -> None:

        self.contatos: list = []

    def add_contato(self, novo_contato: Contato) -> None:

        if novo_contato in self.contatos:

            print("O contato já está presente na agenda, caso deseje alterar algo sobre o contato use a função atualizar contato")

        else:

            self.contatos.append(novo_contato)

    def remover_contato(self, nome: str) -> None:

        for contato in self.contatos:

            if contato.nome == nome:

                self.contatos.remove(contato)
                return

        print("O contato selecionado não está na agenda")

    def atualizar(self, nome: str) -> None:

        for contato in self.contatos:

            if contato.nome == nome:

                novo_nome: str = input("Digite o novo nome para o contato, caso não deseje mudar aperte Enter\n")
                novo_numero: str = input("Digite o novo numero para o contato, caso não deseje mudar aperte Enter\n")

                if novo_nome == "":

                    novo_numero = int(novo_numero)
                    contato.atualizar("", novo_numero)
                    return

                if novo_numero == "":

                    contato.atualizar(novo_nome)
                    return


                novo_numero = int(novo_numero)
                contato.atualizar(novo_nome, novo_numero)
                return

        print("Contato não está na agenda")

    def lista_contatos(self) -> None:

        for i, contato in enumerate(self.contatos):
            print(f"{i+1}.{contato}")

    def achar(self, nome: str) -> None:

        for contato in self.contatos:

            if contato.nome == nome:

                contato.demonstrar()
                return

        print("Contato não está na agenda")

if __name__ == "__main__":

    # instanciando objetos
    agenda = Agenda()
    contato1 = Contato("Breno", 84991122209)
    contato2 = Contato("Gustavo", 84913231412)

    # testando a função de adicionar
    agenda.add_contato(contato1)
    agenda.add_contato(contato2)
    agenda.lista_contatos()

    # testando as funções de encontrar, e atualizar
    agenda.achar("Breno")
    agenda.atualizar("Gustavo")
    agenda.achar("Paulo")

    # testando a função de remover
    agenda.remover_contato("Bergson")
    agenda.lista_contatos()