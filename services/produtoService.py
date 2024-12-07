from repositories.produtoRepository import ProdutoRepository
from model.produto import Produto
from exceptions.produtoExceptions import ProdutoException
class ProdutoService:
    produtoRepository = ProdutoRepository()
    def relatorioGeral(self, produtos: list[Produto]):
        if not produtos:
            return print("Nenhum produto encontrado!")
        for i,produto in enumerate(produtos):
            if i == (len(produtos)-1):
                print(str(produto))
            else:
                print(str(produto) + "\n************")
    def criar(self, produto: Produto):
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
        self.relatorioGeral(self.produtoRepository.listar())
    def buscarPorDescricao(self,descricao: str):
        self.relatorioGeral(self.produtoRepository.buscarPorDescricao(descricao))
    def buscarPorCodigo(self,codigo: int):
        produto = self.produtoRepository.buscarPorCodigo(codigo)
        if not produto:
            return print("Nenhum produto encontrado.")
        print(produto)
    def filtrarPorLimiteDeQuantidade(self,quantidade:int=20):
        self.relatorioGeral(ProdutoRepository.filtrarPorLimiteDeQuantidade(quantidade))
    def aumentarQuantidade(self, codigo: int):
        produto = self.produtoRepository.buscarPorCodigo(codigo)
        if produto:
            self.produtoRepository.aumentarQuantidade(produto)
            return produto
        print("Nenhum produto encontrado!")
    def diminuirQuantidade(self, codigo: int):
        produto = self.produtoRepository.buscarPorCodigo(codigo)
        if not produto:
            return print("Nenhum produto encontrado.")
        if produto.quantidade == 0:
            return print("Não há nenhum produto desse no estoque.")
        self.produtoRepository.diminuirQuantidade(produto)
        return produto
    def atualizarPreco(self, codigo: int, precoVenda: float):
        produto = self.produtoRepository.buscarPorCodigo(codigo)
        if not produto:
            return print("Nenhum produto encontrado.")
        if precoVenda < produto.custoItem:
            raise ProdutoException("Erro: preço de venda não pode ser menor que o custo do item.")
        self.produtoRepository.atualizarPreco(produto,precoVenda)
        return produto