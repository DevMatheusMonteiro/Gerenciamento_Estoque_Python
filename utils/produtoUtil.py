from model.produto import Produto
from services.produtoService import ProdutoService
from utils.genericUtil import GenericUtil
from exceptions.produtoExceptions import ProdutoException
import locale
locale.setlocale(locale.LC_ALL,'pt_BR.UTF-8')
class ProdutoUtil:
    """
    Classe utilitária para operações relacionadas a produtos.

    Atua como camada intermediária entre o usuário e o serviço de produto,
    oferecendo métodos estáticos para criação, manipulação, pesquisa e exibição de relatórios.
    """
    produtoService = ProdutoService()
    @staticmethod
    def formatarValorMonetario(valor: float):
        """
        Formata um valor numérico como moeda no padrão brasileiro.

        Args:
            valor (float): O valor a ser formatado.

        Returns:
            str: O valor formatado em reais (R$).
        """
        return locale.currency(valor,grouping=True)
    @staticmethod
    def criar():
        """
        Cria um novo produto solicitando os dados ao usuário via terminal.

        Valida as entradas e lida com exceções de produto.

        Returns:
            Produto: O produto criado.
        """
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
        """
        Atualiza o preço de venda de um produto existente.

        Solicita ao usuário o código do produto e o novo preço, validando as entradas.

        Raises:
            ProdutoException: Caso ocorra erro na validação do produto.
        """
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
        """
        Solicita uma quantidade ao usuário, garantindo que seja maior que zero.

        Args:
            mensagem (str): Mensagem exibida ao usuário.

        Returns:
            int: A quantidade válida fornecida pelo usuário.
        """
        quantidade = int(GenericUtil.entrarNumero((mensagem)))
        while quantidade < 1:
            if quantidade < 1:
                print("Entre com um valor maior que 0.")
            quantidade = int(GenericUtil.entrarNumero((mensagem)))
        return quantidade
    @staticmethod
    def aumentarQuantidade():
        """
        Aumenta a quantidade de um produto no estoque.

        Solicita o código do produto e o número de vezes que a quantidade deve ser aumentada.
        """
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
        """
        Diminui a quantidade de um produto no estoque.

        Não diminui a quantidade se o produto já estiver esgotado.
        """
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
        """
        Exibe o menu para atualização de produtos (preço e quantidade) e processa as opções do usuário.
        """
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
        """
        Ordena e exibe os produtos com base na quantidade.

        Args:
            produtos (list[Produto]): Lista de produtos a serem ordenados.
        """
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
        """
        Exibe o menu de pesquisa e filtro de produtos e processa as opções do usuário.
        """
        escolha = int((GenericUtil.entrarNumero("1 - Listar todos\n2 - Buscar por descrição do produto\n3 - Buscar por código\n4 - Filtrar por limite de quantidade\n5 - Consultar produtos esgotados\n0 - Sair\nEscolha: ")))
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
            elif escolha == 5:
                ProdutoUtil.produtoService.relatorioGeral(ProdutoUtil.produtoService.consultarProdutosEsgotados())
            elif escolha == 0:
                pass
            else:
                print("Escolha inválida.")
            escolha = int((GenericUtil.entrarNumero("1 - Listar todos\n2 - Buscar por descrição do produto\n3 - Buscar por código\n4 - Filtrar por limite de quantidade\n0 - Sair\nEscolha: ")))
        print("Saindo da pesquisa...\n")
    @staticmethod
    def remover():
        """
        Remove um produto do estoque pelo código fornecido pelo usuário.
        """
        while True:
            try:
                codigo = int(GenericUtil.entrarNumero("Entre com o código do produto que deseja remover: "))
                ProdutoUtil.produtoService.buscarPorCodigo(codigo)
                ProdutoUtil.produtoService.remover(codigo)
                return print("Produto removido com sucesso!")
            except ProdutoException as e:
                print(e)
    def menu():
        """
        Exibe o menu principal do sistema de gerenciamento de produtos e processa as opções do usuário.
        """
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