class Produto:
    """
    Classe que representa um produto no sistema, contendo informações como
    descrição, código, quantidade, custo do item e preço de venda.
    """
    def __init__(self,descricao:str=None,codigo:int=None,quantidade:int=None,custoItem:float=None,precoVenda:float=None):
        """
        Inicializa um objeto Produto com os valores fornecidos.

        Args:
            descricao (str, optional): A descrição do produto.
            codigo (int, optional): O código identificador do produto.
            quantidade (int, optional): A quantidade do produto em estoque.
            custoItem (float, optional): O custo unitário do item.
            precoVenda (float, optional): O preço de venda do produto.
        """
        self.descricao = descricao
        self.codigo = codigo
        self.quantidade = quantidade
        self.custoItem = custoItem
        self.precoVenda = precoVenda
    def setDescricao(self, descricao: str):
        """
        Define a descrição do produto.

        Args:
            descricao (str): A nova descrição do produto.
        """
        self.descricao = descricao
    def setCodigo(self, codigo: int):
        """
        Define o código identificador do produto.

        Args:
            codigo (int): O novo código do produto.
        """
        self.codigo = codigo
    def setQuantidade(self, quantidade: int):
        """
        Define a quantidade do produto, desde que não seja negativa.

        Args:
            quantidade (int): A nova quantidade do produto.

        Notes:
            A quantidade só será atualizada se for maior ou igual a zero.
        """
        if quantidade >= 0:
            self.quantidade = quantidade
    def setCustoItem(self, custoItem: float):
        """
        Define o custo unitário do produto.

        Args:
            custoItem (float): O custo unitário do item.
        """
        self.custoItem = custoItem
    def setPrecoVenda(self, precoVenda: float):
        """
        Define o preço de venda do produto.

        Args:
            precoVenda (float): O novo preço de venda do produto.
        """
        self.precoVenda = precoVenda
    def calcularValorTotal(self):
        """
        Calcula o valor total do produto em estoque.

        Returns:
            float: O valor total, calculado como (preço de venda * quantidade).
        """
        return self.precoVenda * self.quantidade
    def calcularLucroPresumido(self):
        """
        Calcula o lucro presumido com base no custo do item e no preço de venda.

        Returns:
            float: O lucro presumido, calculado como 
                   ((preço de venda - custo do item) * quantidade).
        """
        return (self.precoVenda - self.custoItem) * self.quantidade
    def __str__(self):
        """
        Retorna uma representação em string do produto com suas informações formatadas.

        Returns:
            str: Uma string contendo código, descrição, quantidade, custo, preço de venda,
                 valor total e lucro presumido formatados.

        Notes:
            A formatação monetária é feita pela classe ProdutoUtil.
        """
        from utils.produtoUtil import ProdutoUtil
        return f"Código: {self.codigo}\nDescrição: {self.descricao}\nQuantidade: {self.quantidade}\nCusto do Item: {ProdutoUtil.formatarValorMonetario(self.custoItem)}\nPreço de Venda: {ProdutoUtil.formatarValorMonetario(self.precoVenda)}\nValor Total: {ProdutoUtil.formatarValorMonetario(self.calcularValorTotal())}\nLucro presumido: {ProdutoUtil.formatarValorMonetario(self.calcularLucroPresumido())}"