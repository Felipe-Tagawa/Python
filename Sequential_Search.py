def sequential_search(valores, search):
    for i in range(len(valores)):
        if valores[i] == search:
            return True
    return False

valores =[]
n = 0
search = int(input("Write the number that you want to search: "))

valores.append(int(input()))
n += 1
while True:
    value = int(input())
    if value == -1:            
        break
    valores.append(value)
    n += 1

if(sequential_search(valores, search)):
    print("Achou o valor")
else:
    print("Não achou o valor")

