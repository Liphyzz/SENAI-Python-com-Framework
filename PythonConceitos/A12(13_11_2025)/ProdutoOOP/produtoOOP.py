class Produto:
    # Atributos
    nome: str
    preco: float
    unidades: int

    # Metodos
    def valor_total_em_estoque(self) -> float:
        return (self.preco * self.unidades)
    
    def adicionar_produtos(self, quantidade) -> int:
        self.unidades += quantidade
        return self.unidades
    
    def remover_produtos(self, quantidade) -> int:
        self.unidades -= quantidade
        return self.unidades
    
    def dados_do_produto(self) -> str:
        saida = f"\
|    • Nome do produto: {self.nome}\n\
|    • Valor de compra: {self.preco}\n\
|    • Quantidade em estoque: {self.unidades}\n\
|    • Valor total em estoque: R$ {self.valor_total_em_estoque():.2f}\n"
        return saida
