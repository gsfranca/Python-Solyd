frase = "Oi, tudo bem?"
lista_nomes = ["Guilherme", "Maria", "João", "Diego"] # Tipo List
lista_nomes.append("Lorena")
lista_nomes.remove("Maria")
lista_nomes.insert(1 , "Giovana")
lista_nomes[0] = "Roberta"
contador = lista_nomes.count("João")

f_separada = frase.split(",")

print(f_separada)
print(frase[ : :-1])
print(contador)
print(len(lista_nomes))
print(lista_nomes.pop())
print(lista_nomes)
print(lista_nomes[0:3]) # -X = de traz pra frente