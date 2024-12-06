from repositories.produtoRepository import ProdutoRepository
from model.produto import Produto
import util
class ProdutoService:
    def validarCodigo(codigo: int):
        return not ProdutoRepository.buscarPorCodigo(codigo)
    def validarQuantidade(quantidade: int):
        return quantidade >= 0
    def validarPrecoVenda(precoVenda: float, custoItem: float):
        return precoVenda >= custoItem
    def entrarCodigo(self):
        while True:
            codigo = int(util.entrarNumero("Entre com o código do produto: "))
            if self.validarCodigo(codigo):
                return codigo
            print("Erro: código já cadastrado!")
    def entrarQuantidade(self):
        while True:
            quantidade = int(util.entrarNumero("Entre com a quantidade do produto: "))
            if self.validarQuantidade(quantidade):
                return quantidade
            print("Erro: quantidade não pode ser negativa")
    def entrarPrecoVenda(self,custoItem):
        while True:
            precoVenda = util.entrarNumero("Entre com o preço de venda do produto: ")
            if self.validarPrecoVenda(precoVenda, custoItem):
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
        descricao = util.entrarTexto("Entre com a descrição do produto: ").strip()
        codigo = self.entrarCodigo()
        quantidade = self.entrarQuantidade()
        custoItem = util.entrarNumero("Entre com o custo do produto: ")
        precoVenda = self.entrarPrecoVenda(custoItem)
        ProdutoRepository.criar(Produto(descricao,codigo,quantidade,custoItem,precoVenda))
    def listarTodos(self):
        self.relatorioGeral(ProdutoRepository.listar())
    def buscarPorDescricao(self,descricao: str):
        self.relatorioGeral(ProdutoRepository.buscarPorDescricao(descricao))
    def buscarPorCodigo(codigo: int):
        produto = ProdutoRepository.buscarPorCodigo(codigo)
        if not produto:
            return print("Nenhum produto encontrado!")
        print(produto)
    def filtrarPorLimiteDeQuantidade(self,quantidade:int=20):
        self.relatorioGeral(ProdutoRepository.filtrarPorLimiteDeQuantidade(quantidade))