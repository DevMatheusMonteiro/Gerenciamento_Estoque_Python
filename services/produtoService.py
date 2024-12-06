from repositories.produtoRepository import ProdutoRepository
from model.produto import Produto
import util
class ProdutoService:
    def __init__(self, ProdutoRepository:ProdutoRepository):
        self.produtoRepository = ProdutoRepository
    def validarCodigo(self,codigo: int):
        return not self.produtoRepository.buscarPorCodigo(codigo)
    def entrarCodigo(self):
        while True:
            codigo = int(util.entrarNumero("Entre com o código do produto: "))
            if self.validarCodigo(codigo):
                return codigo
            print("Erro: código já cadastrado!")
    def entrarQuantidade():
        while True:
            quantidade = int(util.entrarNumero("Entre com a quantidade do produto: "))
            if quantidade >= 0:
                return quantidade
            print("Erro: quantidade não pode ser negativa!")
    def entrarPrecoVenda(self,custoItem):
        while True:
            precoVenda = util.entrarNumero("Entre com o preço de venda do produto: ")
            if precoVenda >= custoItem:
                return precoVenda
            print("Erro: preço de venda não pode ser menor que o custo do item!")
    def relatorioGeral(produtos: list[Produto]):
        if not produtos:
            return print("Nenhum produto encontrado!")
        for i,produto in enumerate(produtos):
            if i == (len(produtos)-1):
                print(str(produto))
            else:
                print(str(produto) + "\n************")
    def criar(self):
        produto = Produto()
        produto.setDescricao(descricao=util.entrarTexto("Entre com a descrição do produto: ").strip())
        produto.setCodigo(self.entrarCodigo())
        produto.setQuantidade(self.entrarQuantidade())
        produto.setCustoItem(util.entrarNumero("Entre com o custo do produto: "))
        produto.setPrecoVenda(self.entrarPrecoVenda(custoItem))
        ProdutoRepository.criar(produto)
    def listarTodos(self):
        self.relatorioGeral(self.produtoRepository.listar())
    def buscarPorDescricao(self,descricao: str):
        self.relatorioGeral(self.produtoRepository.buscarPorDescricao(descricao))
    def buscarPorCodigo(self,codigo: int):
        produto = self.produtoRepository.buscarPorCodigo(codigo)
        if not produto:
            return print("Nenhum produto encontrado!")
        print(produto)
    def filtrarPorLimiteDeQuantidade(self,quantidade:int=20):
        self.relatorioGeral(ProdutoRepository.filtrarPorLimiteDeQuantidade(quantidade))