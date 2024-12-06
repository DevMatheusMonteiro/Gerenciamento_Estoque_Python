from mock import estoque_lista
from model.produto import Produto
class ProdutoRepository:
    def criar(produto: Produto):
        estoque_lista.append(produto)
    def listar():
        return estoque_lista
    def buscarPorCodigo(codigo: int):
        return next((produto for produto in estoque_lista if produto.codigo == codigo), None)
    def buscarPorDescricao(descricao: str):
        return list(filter(lambda produto:produto.descricao.lower().find(descricao.lower())!=-1,estoque_lista))
    def ordenarPorQuantidade(produtos: list[Produto], decrescente: bool=False):
        return sorted(produtos,key=lambda produto:produto.quantidade,reverse = decrescente)
    def filtrarPorLimiteDeQuantidade(quantidade: int):
        return list(filter(lambda produto:produto.quantidade < quantidade,estoque_lista))
    def remover(produto: int):
        estoque_lista.remove(produto)
    def aumentarQuantidade(produto: int):
        produto.quantidade += 1
    def diminuirQuantidade(produto):
        produto.quantidade -= 1
    def atualizarPreco(produto: Produto, preco: float):
        produto.precoVenda = preco