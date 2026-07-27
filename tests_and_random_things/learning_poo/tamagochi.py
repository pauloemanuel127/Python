import random

class Tamagochi:

    def __init__(self):

        self.fome = 50
        self.sono = 50
        self.tristeza = 50
        self.estado = "parado"

    def jogar(self):

        self.estado = "jogando"
        self.loop()

    def sair(self):

        self.estado = "parado"
        print("Adeus :)\n")

    def loop(self):

        while self.estado == "jogando":

            print(f"Seu tamagochi está com as seguintes condições: {self.fome} de fome, {self.sono} de sono e {self.tristeza} de tristeza.")
            self.decisão()
            self.tempo()
            self.logica()

        valor = input("Como seu tamagochi morreu, você deseja criar outro? S/N\n").lower()

        if valor == "s":
            self.jogar()

        else:
            self.sair()

    def sentir_fome(self):

        self.fome += 5

    def sentir_sono(self):

        self.sono += 5

    def sentir_tristeza(self):

        self.tristeza += 5

    def tempo(self):

        acontecimentos = [self.sentir_fome, self.sentir_sono, self.sentir_tristeza]
        evento_sorteado = random.choice(acontecimentos)
        evento_sorteado()

    def alimentar(self):

        self.fome = max(0, self.fome - 5)
        print("Delicia, obrigado pelo alimento!\n")

    def dormir(self):

        self.sono = max(0, self.sono - 5)
        print("Que sono bom, me sinto revigorado!\n")

    def brincar(self):

        self.tristeza = max(0, self.tristeza - 5)
        print("Que brincadeira legal, estou bem mais feliz!\n")

    def logica(self):

        if self.fome >= 100:

            self.estado = "game_over"
            print("Seu tamagochi morreu :(")

        elif self.sono >= 100:

            self.estado = "game_over"
            print("Seu tamagochi morreu :(")

        elif self.tristeza >= 100:

            self.estado = "game_over"
            print("Seu tamagochi morreu :(")

    def decisão(self):
        valor = input("Oque voce deseja fazer?\n" \
        "Alimentar - Digite comer\n" \
        "Dormir - Digite dormir\n" \
        "Brincar - Digite brincar\n" \
        "Sair - digite sair\n").lower()

        match valor:

            case "comer":
                self.alimentar()

            case "dormir":
                self.dormir()

            case "brincar":
                self.brincar()

            case "sair":
                self.sair()

jogo = Tamagochi()

print("Bem Vindo\n" \
"Deseja iniciar o jogo? S/N")

entrada = input().lower()

if entrada == "s":
    jogo.jogar()

else:
    print("Obrigado por acessar")