# Precisa estar ordenado maluco

def Binary_Search(valores, search):
    low = 0
    high = len(valores) - 1

    while(low <= high):
        mid = (low + high) // 2
        if(search == valores[mid]):
            return mid
        elif(search < valores[mid]):
            high = mid - 1
        elif(search > valores[mid]):
            low = mid + 1
    return -1

valores = []
search = int(input("Write the number that you want to search: "))
n = 0

valores.append(int(input()))
n += 1
while True:
    value = int(input())
    if value == -1:
        break
    valores.append(value)
    n += 1

result = Binary_Search(valores, search)

if(result != -1):
    print(f"Achou o valor na posição {result}")
else:
    print("Não achou o valor")