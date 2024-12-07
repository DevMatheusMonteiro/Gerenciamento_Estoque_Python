class Produto:
    def __init__(self,descricao:str=None,codigo:int=None,quantidade:int=None,custoItem:float=None,precoVenda:float=None):
        self.descricao = descricao
        self.codigo = codigo
        self.quantidade = quantidade
        self.custoItem = custoItem
        self.precoVenda = precoVenda
    def setDescricao(self, descricao: str):
        self.descricao = descricao
    def setCodigo(self, codigo: int):
        self.codigo = codigo
    def setQuantidade(self, quantidade: int):
        if quantidade >= 0:
            self.quantidade = quantidade
    def setCustoItem(self, custoItem: float):
        self.custoItem = custoItem
    def setPrecoVenda(self, precoVenda: float):
        self.precoVenda = precoVenda
    def calcularValorTotal(self):
        return self.precoVenda * self.quantidade
    def calcularLucroPresumido(self):
        return (self.precoVenda - self.custoItem) * self.quantidade
    def __str__(self):
        from utils.produtoUtil import ProdutoUtil
        return f"Código: {self.codigo}\nDescrição: {self.descricao}\nQuantidade: {self.quantidade}\nCusto do Item: {ProdutoUtil.formatarValorMonetario(self.custoItem)}\nPreço de Venda: {ProdutoUtil.formatarValorMonetario(self.precoVenda)}\nValor Total: {ProdutoUtil.formatarValorMonetario(self.calcularValorTotal())}\nLucro presumido: {ProdutoUtil.formatarValorMonetario(self.calcularLucroPresumido())}"