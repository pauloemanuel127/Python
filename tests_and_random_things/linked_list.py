#Trying to make a linked list algorith

def create_node(value):
    """
    This function creates the node that will always be the last one in the linked list.
    """

    # Nessa função ele recebe o valor desejado e cria o nó dele na lista encadeada, esse valor será sempre adicionado no final da lista
    return {'value': value, 'next': None}

def append(head, value):
    """
    This function adds a new element who will be the last node in the list until a new one is appended.
    """

    # Nessa função ele recebe a lista entitulada como head e o valor que será inserido,
    # Logo no começo ele usa da função create_node para criar o novo nó na lista
    new_node = create_node(value)

    # Aqui ele verifica se a lista está vazia, caso estiver ele retorna o novo nó como elemento
    if head is None:
        return new_node
    
    # Seguindo o caminho ele coloca que o ponto atual é o primeiro elemento da lista que vai sempre está como head
    current = head

    # Nesse loop while, ele testa que enquanto o proximo elemento da lista não tiver chavemento None, ele irá passar para o proximo
    # Já que o elemento adicionado será sempre no final
    while current['next'] is not None:
        current = current['next']

    # Após isso ele coloca que o ultimo elemento será no novo nó e retorna a lista alterada
    current['next'] = new_node
    return head

def remove(head, value):
    """
    This function removes the chosen element in the linked list.
    """

    # Aqui ele primeiro verifica se o valor desejado a ser removido é o primeiro elemento, 
    # Caso for ele irá remover o elemento e a função acaba
    if head['value'] == value:
        head = head['next']
        return head
    
    # Caso não ele ira procurar o elemento até o final da lista, 
    # Caso o elemento estiver presente na lista ele irá remove-lo
    # Se não estiver ele retorna apenas a lista sem alterações
    # O loop while usa da mesma logica do append, 
    # porém ele passa do elemento 2 para o elemento seguinte sempre procurando o valor desejado
    else:
        current = head

        while current['next'] is not None:

            if current['next']['value'] == value:
                current['next'] = current['next']['next']
                return head
            else:
                current = current['next']
        return head

def find(head, target):
    """
    This function searches linearly if the target it's on the list,
    if it's on the list returns a message with its position,
    if not returns a message saying it isn't present.
    """

    # Aqui ele coloca o ponteiro apontando pra lista e verifica se a posição do proximo elemento é None, 
    # Se não for segue o funcionamento, ele verifica se o valor atual é o procurado, se for ele exibe a mensagem
    # Se não for ele aumenta a posição em mais 1 e avança pra o proximo elemento,
    # Se o elemento não for encontrado ele informa que não está na lista
    current = head
    posicao = 0

    while current is not None:

        if current['value'] == target:
            print(f"O valor está presente na lista na posição: {posicao}")
            return True
        
        else:
            current = current['next']
            posicao += 1
    
    print(f"O elemento não está presente na lista")
    return False
    
def display(head):
    """
    This fuction prints the elements on the linked list.
    """

    # Aqui ele pega todos os elementos da lista até o ultimo que é quando o valor de current['next'] for igual a None
    # Trasforma os elementos em uma string e armazena numa lista nativa do python,
    # Depois exibe os elementos presentes nessa lista até indicar o final
    current = head
    elements = []
    
    while current is not None:
        elements.append(str(current['value']))
        current = current['next']
    
    print(" -> ".join(elements) + " -> None")

my_list = None

my_list = append(my_list, 10)
my_list = append(my_list, 20)
my_list = append(my_list, 30)

find(my_list, 20)
display(my_list)

my_list = remove(my_list, 20)

find(my_list, 20)
display(my_list)