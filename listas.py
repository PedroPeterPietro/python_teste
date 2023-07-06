lista = ["teste"]

lista.append("ola")
lista2 = lista.copy()
lista.append("[um, dois]")
lista.extend("[tres, quatro]")
print(lista)
print(lista.pop())
print(lista.pop())
lista2.reverse()
print(lista2)
lista.sort()
print(lista)
print(len(lista))