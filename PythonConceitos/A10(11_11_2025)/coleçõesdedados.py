#↓--------COLEÇÕES DE DADOS NO PYTHON--------↓#


#------Listas/List------#
#Definição: Lista é uma coleção entre colchetes->[], ordenada e mutável. Permite itens duplicados/iguais.
#Índices:   0   ,   1  ,  2,   3
lista = ["Senai", False, 22, 3.14]

print(type(lista))#Confere qual o tipo de variável(nesse caso, se é mesmo uma lista)
print(lista)#Todos os itens
print(lista)#Apenas o item contido no índice 3 (não dá pra trabalhar com índices que não se tenha nada armazenado)
print(len(lista))#Ver o tamanho da lista (do 0 ao 3 -> 4)
del lista[1]#Deleta um elemento/s da lista pelo seu índice [x]. Estrutura -> del nomedalista[Índice]
lista.insert(1, "Python")#Insere um item na lista em um índice "x". Estrutura -> nomedalista.insert(Índice, item a ser inserido)
lista.append("Clodoaldo")#Adiciona um novo (índice com variável) ao final da lista
lista.remove(22)#Remove um item da lista pelo seu valor (se houver mais de um igual, remove o primeiro que encontrar)
lista.extend(["Maria", 45, True])#Adiciona vários itens ao final da lista (pode ser uma outra lista ou tupla)
lista.pop()#Remove o último item da lista
lista.count(True)#Conta quantas vezes um determinado item aparece na lista
lista.index(3.14)#Retorna o índice do item especificado (se houver mais de um igual, retorna o primeiro que encontrar)

for i in range(len(lista)):#Percorre todos os itens da lista
    print(lista[i])#Imprime cada item da lista individualmente (sem ser em formato de lista)

lista.reverse()#Inverte a ordem da lista (último item passa a ser o primeiro)
lista.clear()#Limpa a lista (exclui todos os itens dela)
lista.sort()#Ordena a lista do menor ao maior (ordem crescente), mas não funciona com valores bool
lista.sort(reverse=True)#Ordena a lista do maior ao menor (ordem decrescente), mas não funciona com valores bool
lista2 = lista.copy()#Copia a lista para outra variável
lista3 = lista + lista2#Concatena duas listas em uma nova lista
lista4 = lista * 3#Repete os itens da lista "x" vezes em uma nova lista
lista5 = lista[1:4]#Fatia a lista, criando uma nova lista com os itens do índice 1 ao 3 (o índice 4 não é incluído)
lista6 = lista[::2]#Fatia a lista, criando uma nova lista com todos os itens de 2 em 2 (pula 1 item)
lista7 = lista[::-1]#Fatia a lista, criando uma nova lista com todos os itens em ordem inversa
#...
#-------------------------------------------------------------------------------------------------------------------------------#


#------Tuplas/Tuple------#
#Definição: Tupla é uma coleção entre parênteses->(), ordenada e imutável. Permite itens duplicados/iguais.
#Índice:    0   ,  1  , 2 ,  3
tupla = ("Senai", True, 33, 4.7)

print(type(tupla))
print(tupla)
print(tupla[3])
print(len(tupla))
print(tupla.count(33))#Conta quantas vezes um determinado item aparece na tupla
print(tupla.index("Senai"))#Retorna o índice do item especificado (se houver mais de um igual, retorna o primeiro que encontrar)
#-------------------------------------------------------------------------------------------------------------------------------#


#------Dicionários/Dict-----#
#Definição: Dicionário é uma coleção entre chaves->{}, não indexada e mutável. Permite itens duplicados/iguais, mas não permite chaves duplicadas/iguais. (utiliza "chaves" para localizar os itens dentro da mesma)
#Índices:    {chave : conteúdo,  chave : conteúdo,  chave  : conteúdo,   chave   : conteúdo}
dicionario = {"nome": "senai" , "lógico": False  , "número":    2    ,"Flutuante":   1.73}
print(type(dicionario))
print(dicionario)
print(dicionario["lógico"])
print(len(dicionario))
print(dicionario.keys())#Retorna todas as chaves do dicionário
print(dicionario.values())#Retorna todos os valores do dicionário
print(dicionario.items())#Retorna todas as chaves e valores do dicionário

for chave in dicionario.keys(): #navegar pelo dicionário
    print(chave, "->", dicionario[chave])

dicionario.update({"novo": "César"})
del dicionario["lógico"]
dicionario.update({"nome": "senai"})
dicionario.pop("número")
dicionario.popitem()#Remove o último item adicionado ao dicionário
dicionario2 = dicionario.copy()
dicionario.clear()
#...
#-------------------------------------------------------------------------------------------------------------------------------#


#------Conjunto/Set------#
#Definição: Conjunto é uma coleção entre chaves->{}, sem indexação e mutável. Não permite itens duplicados/iguais.
#Não tem índices, acessa-se as variáveis escrevendo o próprio nome da mesma (por isso não permite itens duplicados)
conjunto = {"Senai", True, 10, 1.75}
print(type(conjunto))
print(conjunto)
print(len(conjunto))
print("Senai" in conjunto)#Verifica se um item está presente no conjunto (retorna True ou False)
print("Python" not in conjunto)#Verifica se um item NÃO está presente no conjunto (retorna True ou False)

#print(conjunto[1]) -> Não funciona (não tem índice)
conjunto.add(False)#Adiciona um item ao conjunto (desde que não)
conjunto.remove("Senai")#Remove um item do conjunto pelo nome do mesmo
conjunto.clear()#Limpa todo o conjunto
conjunto2 = conjunto.copy()
conjunto3 = conjunto.union(conjunto2)#Une dois conjuntos em um novo conjunto
conjunto4 = conjunto.intersection(conjunto2)#Cria um novo conjunto com os itens que são comuns aos dois conjuntos
conjunto5 = conjunto.difference(conjunto2)#Cria um novo conjunto com os itens que estão no primeiro conjunto, mas não estão no segundo
conjunto6 = conjunto.symmetric_difference(conjunto2)#Cria um novo conjunto com os itens que estão em um dos conjuntos, mas não em ambos
conjunto7 = conjunto.union({"Python", 42})#Adiciona novos itens ao conjunto, criando um novo conjunto
conjunto8 = conjunto.intersection_update(conjunto2)#Atualiza o conjunto, mantendo apenas os itens que são comuns aos dois conjuntos
#...
#-------------------------------------------------------------------------------------------------------------------------------#