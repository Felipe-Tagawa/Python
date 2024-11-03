class Pessoa:
    def __init__(self, nome: str, idade: int, matricula: int):
        self.nome = nome
        self.idade = idade
        self.matricula = matricula

def Binary_Search(matricula, pessoas): 
    low = 0
    high = len(pessoas) - 1
    while low <= high:
        mid = (low + high) // 2
        if pessoas[mid].matricula == matricula:  
            return mid
        elif matricula < pessoas[mid].matricula:
            high = mid - 1
        else:
            low = mid + 1
    return -1

pessoas = []  
n = 0
mat = int(input("Write the number that you want to search: "))

while True:
    nome = input("Nome: ")
    idade = int(input("Idade: "))
    matricula = int(input("Matrícula: "))
    pessoas.append(Pessoa(nome, idade, matricula)) 
    n += 1
    if matricula == -1:
        break

result_index = Binary_Search(mat, pessoas)  

if result_index != -1:
    print(f"Achou a matrícula na posição {result_index}")
    print(f"O nome da pessoa com a matrícula {mat} é {pessoas[result_index].nome}")
else:
    print("Não achou o valor")
