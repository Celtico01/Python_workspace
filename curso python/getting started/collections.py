familia = ["Alan", "Rosa", "Nilson"]
#             0       1        2
#             -3      -2       -1

idade = [20, 54, 63]

#print(familia[0:2]) # do 0 ao 2 removendo o 2


idade.extend([19, 25])

print(idade)

familia.insert(1, "Tufão")

print(familia)

try:
    familia.remove("Tufão")
except:
    print("Valor não encontrado")

print(familia)
print(type(familia))


#familia.clear() # limpa a lista

print(familia.count("Alan")) # conta quantos valores iguais existe na lista (Sensitive Case)

print(idade)
idade.sort()
print(idade)

#idade.sort()
idade.reverse()
print(idade)


print(familia)
#familia2 = familia # referencia
#print(familia2)
#familia.remove("Alan") 
#print(familia2)

# por valor

familia2 = familia[:]

print(familia2)
familia.remove("Alan")
print(familia)
print(familia2)


#tuple é imutavel(não pode ser alterado de qualquer forma)

cordenadas = (2, 4, 10)
print(cordenadas)
print(type(cordenadas))