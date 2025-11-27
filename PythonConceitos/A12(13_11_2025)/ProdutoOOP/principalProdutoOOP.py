import produtoOOP as p # Importar o módulo

p1 = p.Produto() # Instanciar o objeto

# Entrada de dados
print("\n--Digite os dados do produto--")
p1.nome = input("   Nome: ")
p1.preco = float(input("   Preço: R$ ").replace("," , "."))
p1.unidades = int(input("   Unidades: "))

# Saída de dados 1
print("\n|--Dados do produto 1--")
print(p1.dados_do_produto())