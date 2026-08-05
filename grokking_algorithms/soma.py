# funções do exercicios do livro, função de soma de elementos de um array, função de conta de quantos elementos tem em um array,
# função para encontrar o valor mais alto em um array e busca binaria por meio da recursão.

def soma(arr: list) -> int:

    if arr == []:

        return 0

    return arr[0] + soma(arr[1:])

def conta(arr: list) -> int:

    if arr == []:

        return 0

    return 1 + conta(arr[1:])

def maior(arr: list) -> int:

    if len(arr) == 2:

        return arr[0] if arr[0] > arr[1] else arr[1]

    sub_max = maior(arr[1:])

    return arr[0] if arr[0] > sub_max else sub_max

def binary_search(arr: list, value: int) -> int:

    if not arr:

        return -1

    meio = len(arr) // 2

    if arr[meio] == value:

        return meio

    elif arr[meio] > value: 

        return binary_search(arr[:meio], value)

    else:

        resultado = binary_search(arr[meio+1:], value)

        return meio + 1 + resultado if resultado != -1 else -1