class Livro:

    def __init__(self, titulo: str, autor: str) -> None:

        self._titulo: str = titulo
        self._autor =  autor
        self._emprestimo: bool = False

    def __repr__(self) -> str:

        return f"{self._titulo} - {self._autor}"

    def get_titulo(self) -> str:

        return self._titulo
    
    def get_emprestimo(self) -> bool:

        return self._emprestimo

    def pick_book(self) -> None:
            
        print("Você pegou o livro emprestado!")
        self._emprestimo = True

    def return_book(self) -> None:

        print("Obrigado por devolver o livro!")
        self._emprestimo = False

class Biblioteca:

    def __init__(self):

        self._livros: list = []

    def add_book(self, livro: Livro) -> None:

        if livro in self._livros:

            print("O livro já faz parte da biblioteca!")

        else:

            print("Obrigado, agora o livro faz parte de biblioteca!")
            self._livros.append(livro)

    def get_object(self, livro: str) -> Livro | None:

        for livros in self._livros:

            if livros.get_titulo() == livro:

                return livros

        return None

    def exibir_livros(self):

        print("="*15, "BIBLIOTECA", "="*15, "\n")

        for i, livro in enumerate(self._livros):

            print(f"{i+1} - {livro}\n")

        print("="*40, "\n")

    def emprestar(self, livro: str) -> bool:

        for livros in self._livros:

            if livros.get_titulo() == livro:

                print("A biblioteca tem o livro!")

                if not livros.get_emprestimo():

                    livros.pick_book()
                    return True

                else:

                    print("O livro já está emprestado!")
                    return False

        print("A biblioteca não tem o livro")
        return False

    def devolver(self, livro: str) -> bool:

        for livros in self._livros:
        
            if livros.get_titulo() == livro:
        
                if not livros.get_emprestimo():
        
                    print("O livro não está emprestado")
                    return False
        
                else:
        
                    livros.return_book()
                    return True

        print("A biblioteca não tem o livro")
        return False

class User:

    def __init__(self) -> None:

        self._user_livros: list = []

    def exibir_user_livros(self) -> None:

        print("="*15, "USUARIO", "="*15, "\n")

        for i, livro in enumerate(self._user_livros):

            print(f"{i+1} - {livro}\n")

        print("="*37, "\n")

    def emprestimo(self, biblioteca: Biblioteca, livro:str) -> None:

        emprestimo: bool = biblioteca.emprestar(livro)

        item: Livro = biblioteca.get_object(livro)

        if emprestimo:

            self._user_livros.append(item)

    def devolução(self, biblioteca: Biblioteca, livro: str) -> None:

        emprestimo: bool = biblioteca.devolver(livro)
        
        item: Livro = biblioteca.get_object(livro)
        
        if emprestimo:
        
            self._user_livros.remove(item)


biblioteca_alexandria = Biblioteca()
livro1 = Livro("1984", "George Orwell")
livro2 = Livro("Dom Quixote", "Miguel de Cervantes")
livro3 = Livro("O Hobbit", "J.R.R. Tolkien")
jonas = User()
visitante = User()

print("--- ADICIONANDO LIVROS AO ACERVO ---")
biblioteca_alexandria.add_book(livro1)
biblioteca_alexandria.add_book(livro2)
biblioteca_alexandria.add_book(livro3)

biblioteca_alexandria.add_book(livro1) 
print("\n")

biblioteca_alexandria.exibir_livros()

print("--- JONAS PEGANDO LIVROS ---")
jonas.emprestimo(biblioteca_alexandria, "1984")
jonas.emprestimo(biblioteca_alexandria, "O Hobbit")
print("\n")

jonas.exibir_user_livros()

print("--- TESTANDO LIMITAÇÕES DA BIBLIOTECA ---")

jonas.emprestimo(biblioteca_alexandria, "O Código Da Vinci")

visitante.emprestimo(biblioteca_alexandria, "1984")
print("\n")

print("--- JONAS DEVOLVENDO LIVRO ---")
jonas.devolução(biblioteca_alexandria, "1984")
print("\n")

jonas.exibir_user_livros()

print("--- TESTANDO FALHAS DE DEVOLUÇÃO ---")

jonas.devolução(biblioteca_alexandria, "Dom Quixote") 

jonas.devolução(biblioteca_alexandria, "O Código Da Vinci")