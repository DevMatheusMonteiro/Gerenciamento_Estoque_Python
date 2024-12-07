from mock import Mock
from model.produto import Produto
class ProdutoRepository:
    estoque = Mock.criarListaEstoque()
    def criar(self,produto: Produto):
        self.estoque.append(produto)
    def listar(self):
        return self.estoque
    def buscarPorCodigo(self,codigo: int):
        return next((produto for produto in self.estoque if produto.codigo == codigo), None)
    def buscarPorDescricao(self,descricao: str):
        return list(filter(lambda produto: produto.descricao.lower().find(descricao.lower()) != -1, self.estoque))
    def ordenarPorQuantidade(self,produtos: list[Produto], decrescente:bool=False):
        return sorted(produtos,key=lambda produto:produto.quantidade,reverse = decrescente)
    def consultarProdutosEsgotados(self):
        return list(filter(lambda produto:produto.quantidade == 0,self.estoque))
    def filtrarPorLimiteDeQuantidade(self, quantidade: int):
        return list(filter(lambda produto:produto.quantidade <= quantidade,self.estoque))
    def remover(self, produto: Produto):
        self.estoque.remove(produto)
    def aumentarQuantidade(self, produto: Produto):
        produto.quantidade += 1
    def diminuirQuantidade(self, produto: Produto):
        produto.quantidade -= 1
    def atualizarPreco(self, produto: Produto, precoVenda: float):
        produto.precoVenda = precoVenda