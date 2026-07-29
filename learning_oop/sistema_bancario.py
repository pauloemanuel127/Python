class ContaBancaria:

    def __init__(self, titular: str):

        self.titular = titular
        self.__saldo = 0
        self.start = False

    def depositar(self, valor: float):

        if valor > 0:

            print(f"Você depositou {valor:.2f} R$")
            self.__saldo += valor
            _ = input("Precione a tecla Enter para proseguir\n")

        else:

            print("Erro! Você não pode depositar valores negativos ou iguais a zero")
            _ = input("Precione a tecla Enter para proseguir\n")

    def sacar(self, valor: float):

        if self.__saldo >= valor:

            print(f"Você sacou um total de {valor:.2f} R$")
            self.__saldo -= valor
            _ = input("Precione a tecla Enter para proseguir\n")

        else:

            print(f"Saldo insuficiente!")
            _ = input("Precione a tecla Enter para proseguir\n")
    def exibir_saldo(self):

        print(f"=" *15, "SALDO", "=" *15, "\n")
        print(f"{f"Você tem um saldo de {self.__saldo:.2f} R$":^37}\n")
        print(f"=" * 37)
        _ = input("Precione a tecla Enter para proseguir\n")

    def interface(self):

        print("=" *15, "Banco", "=" *15, "")
        print(f"Titular da conta: {self.titular}")
        print(f"Saldo: {"*" *len(str(self.__saldo))}")
        print(f"Qual operação deseja realizar:\n"\
              f"Digite 1 para Deposito\n"\
              f"Digite 2 para Saque\n"\
              f"Digite 3 para Exibir Saldo\n"\
              f"Digite 4 para Sair")

    def começar(self):

        print("Deseja iniciar o sistema do Banco? S/N")
        vontade = input().lower()

        if vontade == "s":
            
            self.start = True
            self.loop()

        else:

            print("Tenha um bom dia!")

    def sair(self):

        self.start = False
        print("Obrigado por usar nossos serviços, O Banco agradece!")
        _ = input("Precione a tecla Enter para proseguir\n")

    def logica(self):

        try:
            escolha = int(input())

            if escolha <1 or escolha>4:

                print("\nDigito não reconhecido por favor tente novamente")
                _ = input("Precione a tecla Enter para proseguir\n")
                return
            else:

                match escolha:

                    case 1:

                        dinheiro = float(input("\nDigite o valor que deseja depositar:\n"))
                        self.depositar(dinheiro)

                    case 2:

                        dinheiro = float(input("\nDigite o valor que deseja sacar:\n"))
                        self.sacar(dinheiro)

                    case 3:

                        self.exibir_saldo()

                    case 4:

                        self.sair()

        except ValueError:

            print("\nDigito não reconhecido por favor tente novamente")
            _ = input("Precione a tecla Enter para proseguir\n")
            return

    def loop(self):

        while self.start:

            self.interface()
            self.logica()


conta1 = ContaBancaria("Felipe")
conta1.começar()