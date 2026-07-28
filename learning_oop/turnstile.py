class Catraca:

    def __init__(self):

        self.estado = "fechada"
        self.jogo = "parado"

    def começar(self):

        self.jogo = "jogando"
        self.loop()

    def loop(self):

        while self.jogo == "jogando":
        
            print(f"\nSua catraca está {self.estado}")
            self.escolha()

        print("Obrigado por rodar!")

    def escolha(self):

        try:

            self.resposta = int(input("Oque você deseja fazer?\n"\
                        "digite 1 para colocar moeda\n"\
                        "digite 2 para empurrar a catraca\n"\
                        "digite 3 para desligar\n"\
                        "digite 4 para ligar\n"\
                        "digite 5 para sair\n"))

            self.logica()

            if self.resposta < 1 or self.resposta > 5:

                print("Por favor digite um valor valido inteiro entre 1 e 5.\n")
                self.escolha()


        except ValueError:

            print("Por favor digite um valor valido inteiro entre 1 e 5.\n")
            self.escolha()

    def logica(self):

        match self.resposta:

            case 1:

                self.colocar_moeda()

            case 2:

                self.empurrar()

            case 3:

                self.desligar()

            case 4:

                self.ligar()

            case 5:

                self.sair()

    def colocar_moeda(self):

        if self.estado == "fechada":

            self.estado = "aberta"

        elif self.estado == "aberta":

            return None

    def empurrar(self):

        if self.estado == "fechada":

            return None

        elif self.estado == "aberta":

            self.estado = "fechada"

    def desligar(self):

        self.estado = "desligada"

    def ligar(self):

        if self.estado == "desligada":

            self.estado = "fechada"

    def sair(self):

        if self.estado == "desligada":

            self.jogo = "parado"

        else:

            print("\npara sair a catraca deve estar desligada")

test = Catraca()
test.começar()