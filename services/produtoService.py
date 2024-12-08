from repositories.produtoRepository import ProdutoRepository
from model.produto import Produto
from exceptions.produtoExceptions import ProdutoException
class ProdutoService:
    """
    Classe de serviço responsável por fornecer operações relacionadas a produtos,
    servindo como intermediária entre o repositório e a aplicação.
    """
    produtoRepository = ProdutoRepository()
    def relatorioGeral(self, produtos: list[Produto]):
        """
        Gera um relatório geral dos produtos fornecidos.

        Args:
            produtos (list[Produto]): Lista de produtos a serem exibidos no relatório.

        Returns:
            None: Imprime os produtos no console com um separador.
        """
        if not produtos:
            return print("Nenhum produto encontrado!")
        for i,produto in enumerate(produtos):
            if i == (len(produtos)-1):
                print(str(produto))
            else:
                print(str(produto) + "\n************")
    def criar(self, produto: Produto):
        """
        Cria um novo produto no sistema após validações.

        Args:
            produto (Produto): O objeto Produto a ser adicionado.

        Raises:
            ProdutoException: Se o código for negativo, já existir no sistema,
                              a quantidade for negativa ou o preço for inválido.

        Returns:
            Produto: O produto criado.
        """
        if produto.codigo < 0:
            raise ProdutoException("Erro: código do produto não por ser menor que 0.")
        if self.produtoRepository.buscarPorCodigo(produto.codigo):
            raise ProdutoException("Erro: código já cadastrado.")
        if produto.quantidade < 0:
            raise ProdutoException("Erro: quantidade do produto não por ser menor que 0.")
        if produto.precoVenda < produto.custoItem:
            raise ProdutoException("Erro: preço de venda não pode ser menor que o custo do item.")
        self.produtoRepository.criar(produto)
        return produto
    def listarTodos(self):
        """
        Lista todos os produtos no sistema.

        Returns:
            list[Produto]: Lista de produtos.
        """
        return self.produtoRepository.listar()
    def buscarPorDescricao(self,descricao: str):
        """
        Busca produtos pela descrição.

        Args:
            descricao (str): A descrição ou parte dela a ser buscada.

        Returns:
            list[Produto]: Lista de produtos correspondentes à descrição.
        """
        return self.produtoRepository.buscarPorDescricao(descricao)
    def filtrarPorLimiteDeQuantidade(self,quantidade:int=20):
        """
        Filtra produtos com base em uma quantidade limite.

        Args:
            quantidade (int): O limite máximo de quantidade (padrão é 20).

        Returns:
            list[Produto]: Produtos com quantidade menor ou igual ao limite.
        """
        return self.produtoRepository.filtrarPorLimiteDeQuantidade(quantidade)
    def consultarProdutosEsgotados(self):
        """
        Consulta produtos com estoque zerado.

        Returns:
            list[Produto]: Produtos que estão esgotados.
        """
        return self.produtoRepository.consultarProdutosEsgotados()
    def ordenarPorQuantidade(self, produtos: list[Produto], decrescente:bool=False):
        """
        Ordena os produtos pela quantidade em estoque.

        Args:
            produtos (list[Produto]): Lista de produtos a ser ordenada.
            decrescente (bool): Se True, ordena em ordem decrescente (padrão é False).

        Returns:
            list[Produto]: Lista ordenada de produtos.
        """
        return self.produtoRepository.ordenarPorQuantidade(produtos, decrescente)
    def buscarPorCodigo(self,codigo: int):
        """
        Busca um produto pelo código.

        Args:
            codigo (int): O código do produto.

        Raises:
            ProdutoException: Se o produto não for encontrado.

        Returns:
            Produto: O produto correspondente ao código.
        """
        produto = self.produtoRepository.buscarPorCodigo(codigo)
        if not produto:
            raise ProdutoException("Erro: nenhum produto encontrado.")
        return produto
    def aumentarQuantidade(self, codigo: int):
        """
        Aumenta a quantidade de um produto.

        Args:
            codigo (int): O código do produto a ser atualizado.

        Returns:
            Produto: O produto atualizado.
        """
        produto = self.produtoRepository.buscarPorCodigo(codigo)
        if produto:
            self.produtoRepository.aumentarQuantidade(produto)
            return produto
        print("Nenhum produto encontrado!")
    def diminuirQuantidade(self, codigo: int):
        """
        Diminui a quantidade de um produto no estoque.

        Não permite a diminuição caso o produto já esteja esgotado (quantidade = 0).

        Args:
            codigo (int): O código do produto a ser atualizado.

        Returns:
            Produto | None: O produto atualizado ou None se o produto não for encontrado.
        """
        produto = self.produtoRepository.buscarPorCodigo(codigo)
        if not produto:
            return print("Nenhum produto encontrado.")
        if produto.quantidade == 0:
            return print("Produto esgotado.")
        self.produtoRepository.diminuirQuantidade(produto)
        return produto
    def atualizarPreco(self, codigo: int, precoVenda: float):
        """
        Atualiza o preço de venda de um produto.

        Args:
            codigo (int): O código do produto.
            precoVenda (float): O novo preço de venda.

        Raises:
            ProdutoException: Se o preço de venda for menor que o custo do item.

        Returns:
            Produto: O produto atualizado.
        """
        produto = self.produtoRepository.buscarPorCodigo(codigo)
        if not produto:
            return print("Nenhum produto encontrado.")
        if precoVenda < produto.custoItem:
            raise ProdutoException("Erro: preço de venda não pode ser menor que o custo do item.")
        self.produtoRepository.atualizarPreco(produto,precoVenda)
        return produto
    def remover(self, codigo: int):
        """
        Remove um produto do estoque.

        Args:
            codigo (int): O código do produto a ser removido.

        Returns:
            Produto | None: O produto removido ou None se não for encontrado.
        """
        produto = self.produtoRepository.buscarPorCodigo(codigo)
        if produto:
            self.produtoRepository.remover(produto)
            return produto
        return None
    def totalDeLucroPresumidoEmEstoque(self):
        """
        Calcula o lucro presumido total dos produtos em estoque.

        Returns:
            float: O valor total do lucro presumido.
        """
        return sum([produto.calcularLucroPresumido() for produto in self.listarTodos()])