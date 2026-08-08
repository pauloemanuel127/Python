from random import randint

class Vaga:

    def __init__(self) -> None:

        self.carro: None | Carro = None
        self._ocupada: bool = False

    def __repr__(self) -> str:

        if not self.verificar():

            return f"Vaga disponivel"

        else:

            return f"Vaga ocupada por {self.carro}"
    
    def verificar(self) -> bool:

        return self._ocupada

    def get_carro(self) -> Carro:

        return self.carro

    def add_carro(self, carro: Carro) -> None:

        self.carro = carro
        self._ocupada = True

    def rem_carro(self) -> None:

        self.carro = None
        self._ocupada = False

class Estacionamento:

    def __init__(self) -> None:

        self.vagas = []

    def add_vagas(self, vaga: Vaga) -> None:

        self.vagas.append(vaga)

    def exibir_vagas(self) -> None:

        for i, vaga in enumerate(self.vagas):

            print(f"vaga{i} - {vaga}")

    def estacionar(self, carro: Carro) -> None:

        for vaga in self.vagas:

            if not vaga.verificar():

                if not carro.verificar():

                    vaga.add_carro(carro)
                    carro.estacionar()
                    return 0

                else:

                    print("O carro já está estacionado!\n")
                    return 0

        print("Nenhuma vaga disponivel!\n")

    def sair(self, carro: Carro, horas: int) -> float:

        tarifa = 5.0

        if carro.verificar():

            for vaga in self.vagas:

                if vaga.verificar():

                    if vaga.get_carro() == carro:

                        valor_a_pagar = horas * tarifa

                        print(f"Você deve pagar {valor_a_pagar} R$, deseja pagar agora? S/N")
                        escolha = input().lower()

                        if escolha == 's':

                            vaga.rem_carro()
                            carro.desestacionar()

                        elif escolha == 'n':

                            print("Certo, então não poderá sair com o carro até que o valor seja pago!")

                        else:

                            print("Faça uma escolha de S ou N!")    

        else:

            print("O carro não está estacionado!")
            
class Carro:

    def __init__(self, nome) -> None:

        self.nome = nome
        self.estacionado = False

    def __repr__(self) -> str:

        return f"{self.nome}"

    def verificar(self) -> bool:

        return self.estacionado

    def entrar(self, estacionamento: Estacionamento) -> None:

        print("Bem vindo ao estacionamento, cobramos 5.0 R$ por hora estacionada, deseja entrar? S/N")
        escolha = input().lower()

        if escolha == 's':

            estacionamento.estacionar(self)

        elif escolha == 'n':

            print("Obrigado por visitar!")

        else:

            print("Faça uma escolha de S ou N!")

    def sair(self, estacionamento: Estacionamento) -> None:

        horas = randint(1, 168)

        estacionamento.sair(self, horas)

    def estacionar(self) -> None:

        self.estacionado =  True
        print("Carro estacionado!\n")

    def desestacionar(self) -> None:

        self.estacionado =  False
        print("Carro saiu!")


if __name__ == "__main__":

    # Instanciando os objetos

    vaga1 = Vaga()
    vaga2 = Vaga()
    estacionamento = Estacionamento()
    carro1 = Carro("Civic")
    carro2 = Carro("HB20")
    carro3 = Carro("Celta")

    # testando as funções de adicionar e exibir vagas
    estacionamento.add_vagas(vaga1)
    estacionamento.add_vagas(vaga2)

    estacionamento.exibir_vagas()

    #testando estacionar os carros, e estacionar com todas as vagas ocupadas

    carro1.entrar(estacionamento)
    carro3.entrar(estacionamento)
    carro2.entrar(estacionamento)

    estacionamento.exibir_vagas()

    #testando a saida, pagando e não pagando a tarifa

    carro1.sair(estacionamento)
    carro3.sair(estacionamento)

    estacionamento.exibir_vagas()

    carro2.entrar(estacionamento)

    estacionamento.exibir_vagas()