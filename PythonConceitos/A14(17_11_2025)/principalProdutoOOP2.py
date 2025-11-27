import produtoOOP2 as p

# --Entrada de Dados--
nome = input("Nome: ")
preco = float(input("Preço: R$"))
unidades = int(input("Unidades: "))

# --Instanciação--
ps = p.Produto(nome, preco, unidades)

# --Saída de Dados--
print(ps.dados_do_produto())