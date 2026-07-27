# Calculadora em Python 🐍

Este projeto é um sistema de calculadora desenvolvido para praticar lógica de programação e os fundamentos da linguagem Python. O foco principal foi aplicar recursos que tornem o código robusto, organizado e de fácil interação.

### 🚀 Funcionalidades Atuais

- **Operações Matemáticas:** Realiza cálculos de soma (+), subtração (-), multiplicação (*), divisão (/), potenciação (^) e radiciação (r).
- **Suporte a Números Negativos e Decimais:** O sistema interpreta corretamente entradas matemáticas complexas (ex: `-5.5 + 3`).
- **Persistência de Dados (Histórico):** Armazena e carrega automaticamente os últimos 10 cálculos realizados, gravando-os no ficheiro estático `historico.txt`. O utilizador pode consultar este registo a qualquer momento digitando o comando `hist`.
- **Validação com Expressões Regulares (Regex):** O programa utiliza a biblioteca `re` para validar e extrair as entradas do utilizador, garantindo precisão e evitando falhas por entradas inválidas de formato.
- **Lógica Matemática Específica:** O código trata divisões por zero de forma técnica, diferenciando entre **Indefinido** (X/0) e **Indeterminação** (0/0).
- **Uso Contínuo:** A calculadora opera num ciclo fechado (`while True`), permitindo múltiplas contas em sequência até que o comando `exit` seja acionado.

### 🛠️ Tecnologias Utilizadas

- **Python 3**
- **Estruturas de Dados:** Listas para gestão e filtragem do histórico.
- **Expressões Regulares (Regex):** Para manipulação e validação avançada de *strings* e *inputs*.
- **I/O de Ficheiros:** Utilização da função `open()` com codificação UTF-8 para garantir a persistência de dados na memória do computador.
- **Modularização:** Separação de responsabilidades (Front-end no *loop* principal e Back-end matemático num módulo separado).

### 📋 Como utilizar

1. Certifica-te de ter o Python instalado.
2. Certifica-te de que os ficheiros `calculadora.py` e `operacoes.py` estão na mesma pasta.
3. Executa o comando no teu terminal: `python calculadora.py`.
4. **Formato de entrada:** Digita a conta com ou sem espaços (Ex: `10+20`, `-5 * 4`, ou `2 r 16`).
5. **Comandos de suporte:** Usa `hist` para ver o histórico ou `exit` para salvar os dados e sair.

### 📈 Próximos Passos (Roadmap)

Este projeto está em desenvolvimento contínuo. As metas alcançadas e futuras são:
- [x] **Modularização:** Criar funções específicas para cada operação matemática.
- [x] **Criação de Biblioteca:** Organizar a lógica de cálculos num módulo separado (`operacoes.py`).
- [x] **Melhoria no Input:** Ajustar a lógica de entrada para aceitar expressões sem a necessidade obrigatória de espaços e com suporte a números negativos.
- [x] **Persistência de Dados:** Implementar a gravação e o carregamento automático das últimas 10 operações num ficheiro `.txt` para acesso posterior mesmo após fechar o programa.
- [ ] **Interface Gráfica:** (Opcional) Migrar a calculadora do terminal para uma interface visual usando bibliotecas como `Tkinter` ou `CustomTkinter`.

---
*Projeto desenvolvido como exercício de lógica e portfólio em Python.*