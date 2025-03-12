
texto: str = 'Uma palavra'
numero: int = 1234
flutuante: float = 3.5
boleano: bool = True

um_set: set = {1, 2, 3}
uma_lista: list = []
uma_tupla: tuple = 1, 2, 3
um_dic: dict = {}


# Com função
def soma(x: int, y: int, z: float) -> float:
    return x + y + z

print(soma(4, 5, 2))

# Lista
lista_int: list[int] = [1, 2, 3, 4]
lista_string: list[str] = ["a", "b", "c"]
lista_tupl: list[tuple] = [(1, "a"), (2, "b")]
lista_lista_int: list[list[int]] = [[1], [4, 5]]
