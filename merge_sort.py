def merge_sort(lista):
    # Caso base: lista já tem 1 ou nenhum elemento
    if len(lista) <= 1:
        return lista
        
    # Dividir a lista ao meio
    meio = len(lista) // 2
    esquerda = lista[:meio]
    direita = lista[meio:]
    
    # Chamada recursiva para ordenar as duas metades
    esquerda = merge_sort(esquerda)
    direita = merge_sort(direita)

    # Mesclar as duas listas ordenadas
    return merge(esquerda, direita)

def merge(esquerda, direita):
    resultado = []
    i, j = 0, 0
    
    # Comparar os elementos de ambas as listas e adicionar o menor à lista resultado
    while i < len(esquerda) and j < len(direita):
        if esquerda[i] < direita[j]:
            resultado.append(esquerda[i])
            i += 1
        else:
            resultado.append(direita[j])
            j += 1
 
    # Adicionar os elementos restantes da lista esquerda (se houver)
    while i < len(esquerda):
        resultado.append(esquerda[i])
        i += 1
    
    # Adicionar os elementos restantes da lista direita (se houver)
    while j < len(direita):
        resultado.append(direita[j])
        j += 1
    
    return resultado

# Exemplo de uso
lista = [38, 27, 43, 3, 9, 82, 10]
print("Lista original:", lista)
lista_ordenada = merge_sort(lista)
print("Lista ordenada:", lista_ordenada)

# Exemplo de uso 2
lista = [2, 25, 34, 3, 9, 23, 1]
print("Lista original:", lista)
lista_ordenada = merge_sort(lista)
print("Lista ordenada:", lista_ordenada)

# Exemplo de uso 3
lista = [20, 15, 10, 3, 9, 100, 10]
print("Lista original:", lista)
lista_ordenada = merge_sort(lista)
print("Lista ordenada:", lista_ordenada)

