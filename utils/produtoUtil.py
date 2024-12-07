from model.produto import Produto
from services.produtoService import ProdutoService
from utils.genericUtil import GenericUtil
from exceptions.produtoExceptions import ProdutoException
import locale
locale.setlocale(locale.LC_ALL,'pt_BR.UTF-8')
class ProdutoUtil:
    produtoService = ProdutoService()
    @staticmethod
    def formatarValorMonetario(valor: float):
        return locale.currency(valor,grouping=True)
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
    @staticmethod
    def atualizarPreco():
        while True:
            try:
                codigo = int(GenericUtil.entrarNumero("Entre com codigo do produto que deseja atualizar o preço: "))
                ProdutoUtil.produtoService.buscarPorCodigo(codigo)
                preco = GenericUtil.entrarNumero("Entre com o novo preço de venda do produto: ")
                ProdutoUtil.produtoService.atualizarPreco(codigo,preco)
                return print("Preço de venda atualizado com sucesso!")
            except ProdutoException as e:
                print(e)
    @staticmethod
    def definirQuantidade(mensagem):
        quantidade = int(GenericUtil.entrarNumero((mensagem)))
        while quantidade < 1:
            if quantidade < 1:
                print("Entre com um valor maior que 0.")
            quantidade = int(GenericUtil.entrarNumero((mensagem)))
        return quantidade
    @staticmethod
    def aumentarQuantidade():
        try:
            codigo = int(GenericUtil.entrarNumero("Entre com codigo do produto que deseja aumentar a quantidade: "))
            ProdutoUtil.produtoService.buscarPorCodigo(codigo)
            quantidade = ProdutoUtil.definirQuantidade("Quantas vezes deseja aumentar a quantidade? ")
            for i in range(quantidade):
                ProdutoUtil.produtoService.aumentarQuantidade(codigo)
            print(f"Quantidade do produto aumentada {quantidade} vez(es)")
        except ProdutoException as e:
            print(e)
    @staticmethod
    def diminuirQuantidade():
        try:
            codigo = int(GenericUtil.entrarNumero("Entre com codigo do produto que deseja diminuir a quantidade: "))
            ProdutoUtil.produtoService.buscarPorCodigo(codigo)
            quantidade = ProdutoUtil.definirQuantidade("Quantas vezes deseja diminuir a quantidade? ")
            i = 0 
            for i in range(quantidade):
                produto = ProdutoUtil.produtoService.diminuirQuantidade(codigo)
                if not produto:
                    break
                i += 1
            print(f"Quantidade do produto diminuída {i} vez(es)")
        except ProdutoException as e:
            print(e)
    @staticmethod
    def menuAtualizar():
        escolha = int(GenericUtil.entrarNumero("1 - Atualizar preço de venda\n2 - Aumentar quantidade no estoque\n3 - Diminuir quantidade no estoque\n0 - Sair\nEscolha: "))
        while escolha != 0:
            if escolha == 1:
                ProdutoUtil.atualizarPreco()
            elif escolha == 2:
                ProdutoUtil.aumentarQuantidade()
            elif escolha == 3:
                ProdutoUtil.diminuirQuantidade()
            elif escolha == 0:
                pass
            else:
                print("Escolha inválida.")
            escolha = int(GenericUtil.entrarNumero("1 - Atualizar preço de venda\n2 - Aumentar quantidade no estoque\n3 - Diminuir quantidade no estoque\n0 - Sair\nEscolha: "))
        print("Saindo da atualização...\n")
    @staticmethod
    def ordenarPorQuantidade(produtos: list[Produto]):
        escolha = int(GenericUtil.entrarNumero("Deseja ordenar os produtos por quantidade (1 - Sim | 0 - Não)? "))
        while escolha != 1 and escolha != 0:
            if escolha != 1 and escolha != 0:
                print("Escolha inválida.")
            escolha = int(GenericUtil.entrarNumero("Deseja ordenar os produtos por quantidade (1 - Sim | 0 - Não)? "))
        if escolha == 0:
            return ProdutoUtil.produtoService.relatorioGeral(produtos)
        decrescente = int(GenericUtil.entrarNumero("Ordem crescente (1) ou decrescente (2)? "))
        while decrescente != 1 and decrescente != 2:
            if decrescente != 1 and decrescente != 2:
                print("Escolha inválida.")
            decrescente = int(GenericUtil.entrarNumero("Ordem crescente (1) ou decrescente (2)? "))
        ProdutoUtil.produtoService.relatorioGeral(ProdutoUtil.produtoService.ordenarPorQuantidade(produtos, decrescente == 2))
    @staticmethod
    def menuPesquisa():
        escolha = int((GenericUtil.entrarNumero("1 - Listar todos\n2 - Buscar por descrição do produto\n3 - Buscar por código\n4 - Filtrar por limite de quantidade\n0 - Sair\nEscolha: ")))
        while escolha != 0:
            if escolha == 1:
                ProdutoUtil.ordenarPorQuantidade(ProdutoUtil.produtoService.listarTodos())
            elif escolha == 2:
                ProdutoUtil.ordenarPorQuantidade(ProdutoUtil.produtoService.buscarPorDescricao(GenericUtil.entrarTexto("Entre com a descrição: ")))
            elif escolha == 3:
                try:
                    produto = ProdutoUtil.produtoService.buscarPorCodigo(int(GenericUtil.entrarNumero("Entre com o código: ")))
                    print(produto)
                except ProdutoException:
                    print("Nenhum produto encontrado")
            elif escolha == 4:
                ProdutoUtil.ordenarPorQuantidade(ProdutoUtil.produtoService.filtrarPorLimiteDeQuantidade(int(GenericUtil.entrarNumero("Entre com o limite de quantidade: "))))
            elif escolha == 0:
                pass
            else:
                print("Escolha inválida.")
            escolha = int((GenericUtil.entrarNumero("1 - Listar todos\n2 - Buscar por descrição do produto\n3 - Buscar por código\n4 - Filtrar por limite de quantidade\n0 - Sair\nEscolha: ")))
        print("Saindo da pesquisa...\n")
    @staticmethod
    def remover():
        while True:
            try:
                codigo = int(GenericUtil.entrarNumero("Entre com o código do produto que deseja remover: "))
                ProdutoUtil.produtoService.buscarPorCodigo(codigo)
                ProdutoUtil.produtoService.remover(codigo)
                return print("Produto removido com sucesso!")
            except ProdutoException as e:
                print(e)
    def menu():
        escolha = int(GenericUtil.entrarNumero("1 - Criar novo produto\n2 - Atualizar produto\n3 - Remover produto\n4 - Buscar produtos\n5 - Calcular total de lucro presumido em estoque\n0 - Encerrar\nEscolha: "))
        while escolha != 0:
            if escolha == 1:
                ProdutoUtil.criar()
            elif escolha == 2:
                ProdutoUtil.menuAtualizar()
            elif escolha == 3:
                ProdutoUtil.remover()
            elif escolha == 4:
                ProdutoUtil.menuPesquisa()
            elif escolha == 5:
                print(f"Total de lucro presumido: {ProdutoUtil.formatarValorMonetario(ProdutoUtil.produtoService.totalDeLucroPresumidoEmEstoque())}")
            elif escolha == 0:
                pass
            else:
                print("Escolha inválida.")
            escolha = int(GenericUtil.entrarNumero("1 - Criar novo produto\n2 - Atualizar produto\n3 - Remover produto\n4 - Buscar produtos\n5 - Calcular total de lucro presumido em estoque\n0 - Encerrar\nEscolha: "))
        print("Encerrado...")