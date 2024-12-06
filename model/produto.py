class Produto:
    def __init__(self,descricao: str,codigo: int,quantidade: int,custoItem: float,precoVenda: float):
        self.descricao = descricao
        self.codigo = codigo
        self.quantidade = quantidade
        self.custoItem = custoItem
        self.precoVenda = precoVenda
    def valorTotal(self):
        return self.precoVenda * self.quantidade
    def __str__(self):
        return f"Código: {self.codigo}\nDescrição: {self.descricao}\nQuantidade: {self.quantidade}\nCusto do Item: {self.custoItem}\nPreço de Venda: {self.precoVenda}\nValor Total: {self.valorTotal()}"