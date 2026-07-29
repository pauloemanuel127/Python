class ContaBancaria:

    def __init__(self, titular: str):

        self.titular = titular
        self.__saldo = 0

    def depositar(self, valor: float):

        if valor > 0:

            self.__saldo += valor

        else:

            print("Erro! Você não pode depositar valores negativos ou iguais a zero")

    def sacar(self, valor: float):

        if self.__saldo >= valor:

            print(f"Você sacou um total de {valor} R$")

        else:

            print(f"Saldo insuficiente!")

    def exibir_saldo(self):

        print(f"=" *15, "SALDO", "=" *15)
        print(" {:^35}".format(f"Você tem um saldo de {self.__saldo:.2f} R$"))
        print(f"=" * 37)


banco1 = ContaBancaria("Paulo")

banco1.exibir_saldo()