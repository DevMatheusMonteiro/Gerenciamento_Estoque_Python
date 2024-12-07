from model.produto import Produto
from services.produtoService import ProdutoService
from utils.genericUtil import GenericUtil
from exceptions.produtoExceptions import ProdutoException
class ProdutoUtil:
    produtoService = ProdutoService()
    @staticmethod
    def criar():
        while True:
            try:
                descricao = GenericUtil.entrarTexto("Entre com a descrição do produto: ").strip()
                codigo = int(GenericUtil.entrarNumero("Entre com o código do produto: "))
                quantidade = int(GenericUtil.entrarNumero("Entre com a quantidade do produto: "))
                custoItem = GenericUtil.entrarNumero("Entre com o custo do produto: ")
                precoVenda = GenericUtil.entrarNumero("Entre com o preço de venda do produto: ")
                return ProdutoUtil.produtoService.criar(Produto(descricao,codigo,quantidade,custoItem,precoVenda))
            except ProdutoException as e:
                print(e)
