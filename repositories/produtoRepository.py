from mock import Mock
from model.produto import Produto
class ProdutoRepository:
    """
    Classe responsável por atuar como um repositório intermediário entre a fonte de dados e a aplicação, gerenciando operações relacionadas ao estoque de produtos.
    """
    estoque = Mock.criarListaEstoque()
    def criar(self,produto: Produto):
        """
        Adiciona um produto ao estoque.

        Args:
            produto (Produto): O objeto do tipo Produto a ser adicionado ao estoque.
        """
        self.estoque.append(produto)
    def listar(self):
        """
        Retorna a lista completa de produtos no estoque.

        Returns:
            list: Lista de produtos no estoque.
        """
        return self.estoque
    def buscarPorCodigo(self,codigo: int):
        """
        Busca um produto no estoque pelo seu código.

        Args:
            codigo (int): O código do produto a ser buscado.

        Returns:
            Produto | None: O produto correspondente ao código, ou None caso não encontrado.
        """
        return next((produto for produto in self.estoque if produto.codigo == codigo), None)
    def buscarPorDescricao(self,descricao: str):
        """
        Busca produtos no estoque que contenham a descrição fornecida.

        Args:
            descricao (str): A descrição (ou parte dela) a ser buscada.

        Returns:
            list: Lista de produtos que possuem a descrição fornecida.
        """
        return list(filter(lambda produto: produto.descricao.lower().find(descricao.lower()) != -1, self.estoque))
    def ordenarPorQuantidade(self,produtos: list[Produto], decrescente:bool=False):
        """
        Ordena uma lista de produtos com base na quantidade em estoque.

        Args:
            produtos (list[Produto]): A lista de produtos a ser ordenada.
            decrescente (bool): Define se a ordenação será em ordem decrescente (padrão é False).

        Returns:
            list: A lista de produtos ordenada pela quantidade.
        """
        return sorted(produtos,key=lambda produto:produto.quantidade,reverse = decrescente)
    def consultarProdutosEsgotados(self):
        """
        Consulta os produtos que estão com a quantidade igual a zero no estoque.

        Returns:
            list: Lista de produtos esgotados (quantidade = 0).
        """
        return list(filter(lambda produto:produto.quantidade == 0,self.estoque))
    def filtrarPorLimiteDeQuantidade(self, quantidade: int):
        """
        Filtra os produtos no estoque cuja quantidade seja menor ou igual ao limite especificado.

        Args:
            quantidade (int): O limite máximo da quantidade de produtos a ser filtrado.

        Returns:
            list: Lista de produtos com quantidade menor ou igual ao limite.
        """
        return list(filter(lambda produto:produto.quantidade <= quantidade,self.estoque))
    def remover(self, produto: Produto):
        """
        Remove um produto do estoque.

        Args:
            produto (Produto): O produto a ser removido do estoque.
        """
        self.estoque.remove(produto)
    def aumentarQuantidade(self, produto: Produto):
        """
        Aumenta a quantidade de um produto em uma unidade.

        Args:
            produto (Produto): O produto cujo estoque será aumentado.
        """
        produto.quantidade += 1
    def diminuirQuantidade(self, produto: Produto):
        """
        Diminui a quantidade de um produto em uma unidade.

        Args:
            produto (Produto): O produto cujo estoque será diminuído.
        """
        produto.quantidade -= 1
    def atualizarPreco(self, produto: Produto, precoVenda: float):
        """
        Atualiza o preço de venda de um produto.

        Args:
            produto (Produto): O produto cujo preço será atualizado.
            precoVenda (float): O novo preço de venda do produto.
        """
        produto.precoVenda = precoVenda