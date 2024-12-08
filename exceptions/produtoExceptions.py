class ProdutoException(Exception):
    """
    Exceção personalizada para erros relacionados a operações com produtos.

    Esta classe estende a classe `Exception` padrão do Python e é utilizada
    para representar erros específicos no contexto de manipulação de produtos.

    Args:
        mensagem (str): A mensagem de erro associada à exceção.

    Example:
        raise ProdutoException("Erro: código do produto já cadastrado.")
    """
    def __init__(self, mensagem: str):
        """
        Inicializa a classe ProdutoException com a mensagem de erro.

        Args:
            mensagem (str): A mensagem que descreve o erro ocorrido.
        """
        super().__init__(mensagem)