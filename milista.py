#ejemplo de uso de listas
misnovios=("hector", "hector najera")
numeros=(666, 77, 10)
#mostrando mis novios
print(misnovios)
#mostrando mis numeros raros
print(numeros)
print("----accediendo a los elementos de la lista----")
print(misnovios[0])
print(numeros[1])
if "hector" in misnovios:
    print("si, 'hector' esta en la lista de mis novios")
else:
    print("chale no eres mi novio")
print("numero de novios:")
Nnovios=len(misnovios)
print(f"numero de novios = {Nnovios}")
print("Mi Media Naranja: ")
posicion=0
for medianaranja in misnovios:
    print(posicion," ",medianaranja)
    posicion+=1