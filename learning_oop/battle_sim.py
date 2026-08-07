from random import randint

class Personagem:

    def __init__(self, nome: str) -> None:

        self.nome: str = nome
        self._vida: float = 10.0
        self._ataque: float = 4.0
        self._magia: float = 4.0
        self._defesa: int = 5
        self._defesa_magica: int = 5

    def sofrer_dano(self, inimigo: Personagem, Dano: int) -> None:

        if isinstance(inimigo, Mago):
            
            self._vida -= max(0, Dano - self._defesa_magica)

        elif isinstance(inimigo, Guerreiro):

            self._vida -= max(0, Dano - self._defesa)

        else:

            self._vida -= max(0, Dano - self._defesa - self._defesa_magica)

    def vivo(self) -> bool:

        return self._vida > 0

    def get_defesa(self) -> int:

        return self._defesa

    def get_defesa_magica(self) -> int:

        return self._defesa_magica

    def get_defesas(self) -> int:

        return self._defesa + self._defesa_magica

    def get_hp(self) -> str:

        return f"O {self.nome} está com {int(self._vida)} de vida"
class Mago(Personagem):

    def __init__(self, nome: str) -> None:

        super().__init__(nome)
        self._defesa: int = 3
        self._defesa_magica: int = 7

    def atacar(self, inimigo: Personagem) -> None:

        valor = randint(3, 7)
        inimigo.sofrer_dano(self, self._magia * valor)
        print(f"O {self.nome} atacou e causou {int((self._magia * valor) - inimigo.get_defesa_magica())} de dano")
class Guerreiro(Personagem):

    def __init__(self, nome: str) -> None:

        super().__init__(nome)
        self._defesa: int = 7
        self._defesa_magica: int = 3

    def atacar(self, inimigo: Personagem) -> None:

        valor = randint(3, 7)
        inimigo.sofrer_dano(self, self._ataque * valor)
        print(f"O {self.nome} atacou e causou {int((self._ataque * valor) - inimigo.get_defesa())} de dano")  
class Monstro(Personagem):

    def __init__(self):

        super().__init__("Goblin")
        self._vida: float = 20.0
        self._ataque: float = 2.5

    def atacar(self, inimigo: Personagem) -> None:

        valor = randint(5, 10)
        inimigo.sofrer_dano(self, self._ataque * valor)
        print(f"O Monstro atacou e causou {int((self._ataque * valor) - inimigo.get_defesas())} de dano")

    def get_hp(self) -> str:

        return f"O Monstro está com {int(self._vida)} de vida"

class Arena:

    def __init__(self) -> None:

        self.jogo: str = "jogando"

    def começar(self, Monstro: Personagem) -> None:

        print("Bem vindo digite seu nome:")
        nome: str = input()
        print("Agora escolha sua classe:\n" \
        "1. Guerreiro\n" \
        "2. Mago\n")
        classe: int = int(input())

        match(classe):

            case 1:

                personagem = Guerreiro(nome)
                self.loop(personagem, Monstro)
                self.reiniciar()

            case 2:

                personagem = Mago(nome)
                self.loop(personagem, Monstro)
                self.reiniciar()

    def loop(self, Personagem: Personagem, Monstro: Personagem) -> None:

        while self.jogo == "jogando":

            if (Personagem.vivo() and Monstro.vivo()):

                Personagem.atacar(Monstro)
                Monstro.atacar(Personagem)
                print(Personagem.get_hp())
                print(Monstro.get_hp())

            else:

                if Personagem.vivo(): 

                    print("Você venceu! O monstro morreu\n")

                elif Monstro.vivo():

                    print(f"Você perdeu, seu personagem: {Personagem.nome} morreu\n")

                else:

                    print(f"Os dois guerreiros morreram lutando, infelizmente você perdeu e seu personagem: {Personagem.nome} morreu\n")

                break

        self.jogo = "acabou"

    def reiniciar(self) -> None:

        print("Você deseja reiniciar? s/n")
        decisão: str = input().lower()

        match(decisão):

            case 's':

                self.jogo = "jogando"
                novo_monstro = Monstro()
                self.começar(novo_monstro)

            case 'n':

                self.jogo = "jogando"
                print("Obrigado por jogar!")

if __name__ == "__main__":

    # instanciando os objetos
    monstro = Monstro()
    arena = Arena()

    # começando a simulação
    arena.começar(monstro)