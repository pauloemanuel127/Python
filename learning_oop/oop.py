class Canal:
    # Ao definir uma classe, se cria um molde para objetos, tipo um modelo base com caracateristicas especificas, que podem ou não vir predefinidas
    # Como no exemplo dos canais onde o numero de inscritos
    def __init__(self, nome: str, descrição: str, inscritos: int):
        # Esse metódo chamado __init__ é responsavél por inicializar os objetos e colocar suas caracteristicas em seus devidos lugares
        # O self.variavel e responsavel por determinar variaveis que poderão ser usadas para obter acesso as caracteristicas de um objeto
        self.nome = nome
        self.descrição = descrição
        self.inscritos = inscritos
        self.videos = []

    def inscrever(self, quantidade=1):
        # Esse metódo é um exemplo de "função", que modifica alguma carateristica de um objeto especifico
        self.inscitos += quantidade
        return

    def postar_video(self, video):

        if video in self.videos:
            print("Esse video já foi postado")
            return

        self.videos.append(video)

class CanaisAmigos(Canal):
    # Aqui estou desenvolvendo uma classe que herda as caracteristicas da outra classe, assim aplicando o pilar de herança
    def __init__(self, nome: str, descrição: str, inscritos: int, amigos: list):
        # O primeiro metodo construtor da classe, se responsabiliza por inicializar os objetos seguindo as caracateristicas dessa classe
        super().__init__(nome, descrição, inscritos)
        # O super().__init__ chama o metodo construtor da classe "base"
        self.amigos = amigos
        self._membros = []
        # O self._membros seria para definir que a variavel membros é privada e não deve ser alterada fora da classe,
        # Porém o python n possui esse funcionamento na pratica

    @property
    # O @property faz com que o metodo se torne uma propriedade do objeto, 
    # Fazendo com que não seja mais necessario quando for utilizar colocar os parenteses ao fim como em canal.membros()

    # Essas funções seriam as responsaveis por gerenciar o acesso a variavel "privada"
    # Assim melhorando a forma como elas estão sendo utilizadas, e não deixando livre de qualquer forma
    def membros(self):
        return self._membros

    def add_membro(self, nome: str):

        if nome not in self._membros:
            self._membros.append(nome)
            return

        else:
            print(f"O membro {nome} já está registrado")
            return

    def remover_membro(self, nome: str):

        if nome in self._membros:
            self._membros.remove(nome)
            return

        else:
            print(f"O membro {nome} já foi removido, ou nunca esteve registrado")
            return

class Video:
    # Essa classe foi criada para a demonstração da composição, aqui seriam objetos que pertencem a outra classe
    def __init__(self, titulo: str, descrição: str):
        self.titulo = titulo
        self.descrição = descrição
        self.visualizações = 0
        self.likes = 0
        self.deslikes = 0
        self.comentarios = []

    def __repr__(self):
        # Esse metodo faz com que quando seja solicitado para exibir uma str do objeto ele exiba oq o metodo retorna, 
        # coloquei os <> para determinar que é um objeto
        return f"<{self.titulo}>"
    
    def assistir(self):
        self.visualizações += 1
        return

    def curtir(self):
        self.likes += 1
        return

    def descurtir(self):
        self.deslikes += 1
        return

    def comentar(self, comentario: str):
        self.comentarios.append(comentario)
        return

    def dados(self):
        print(f"""Titulo: {self.titulo}
Descrição: {self.descrição}
{self.visualizações} visualizações
{self.likes} likes
{self.deslikes} deslikes
comentarios: {self.comentarios}\n""")
        return

        
canal_paulo = Canal("joao", "amo youtube", 10000)
canal_jabulandio = CanaisAmigos("Primo do jabulandio", "faço videos com meu primo obeso e sordido", 100, ["pauloemanuel127", "ramon_royale", "GuguGx", "Voltailk_Breno"])

# print(canal_paulo.inscitos)
# print(canal_jabulandio.inscitos)

# canal_jabulandio.inscrever()
# canal_paulo.inscrever(1000000)

# print(canal_paulo.inscitos)
# print(canal_jabulandio.inscitos)
# print(canal_jabulandio.membros)

# canal_jabulandio.add_membro("Paulo")

# print(canal_jabulandio.membros)

# canal_jabulandio.add_membro("Paulo")
# canal_jabulandio.add_membro("Ramon")

# print(canal_jabulandio.membros)

# canal_jabulandio.remover_membro("Paulo")

# print(canal_jabulandio.membros)

# canal_jabulandio.remover_membro("Paulo")

video_futebol_com_primo = Video("jogando bola com meu primo no x1, ganhei?", "Fut com meu primo")
video_fortnite = Video("Gameplay de fortnite com meus amigos, joguei serio?", f"{canal_jabulandio.amigos}")

# video_futebol_com_primo.dados()

canal_jabulandio.postar_video(video_futebol_com_primo)
canal_jabulandio.postar_video(video_fortnite)

print(canal_jabulandio.videos)