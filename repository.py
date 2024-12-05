""" 
# Camada para intermediária entre a aplicação e a fonte de dados
"""
from estoque import estoque_lista
def criar(produto):
    estoque_lista.append(produto)
def listar():
    return estoque_lista
def buscarPorCodigo(codigo):
    return next((produto for produto in estoque_lista if produto["codigo"] == codigo), None)
def buscarPorDescricao(descricao):
    return list(filter(lambda produto:produto["descricao"].lower().find(descricao.lower())!=-1,estoque_lista))
def ordenarPorQuantidade(produtos, decrescente=False):
    return sorted(produtos,key=lambda produto:produto["quantidade"],reverse=decrescente)
def filtrarPorLimiteDeQuantidade(quantidade):
    return list(filter(lambda produto:produto["quantidade"]<quantidade,estoque_lista))
def remover(produto):
    estoque_lista.remove(produto)
def aumentarQuantidade(produto):
    produto["quantidade"]+=1
def diminuirQuantidade(produto):
    produto["quantidade"]-=1
def atualizarPreco(produto, preco):
    produto["precoVenda"] = preco