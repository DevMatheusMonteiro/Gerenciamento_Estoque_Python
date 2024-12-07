from repositories.produtoRepository import ProdutoRepository
from utils.produtoUtil import ProdutoUtil
from services.produtoService import ProdutoService
# print(ProdutoUtil.criar())
produtoService = ProdutoService()
produtoService.buscarPorDescricao("Notebook")
print(produtoService.totalDeLucroPresumidoEmEstoque())