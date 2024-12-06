from mock import estoque_lista
from services.produtoService import ProdutoService
from repositories.produtoRepository import ProdutoRepository
from model.produto import Produto
produtoService = ProdutoService(ProdutoRepository)
# produtoService.listarTodos()
produtoService.criar()