class GenericUtil:
    @staticmethod
    def entrarNumero(mensagem: str):
        """
        Solicita ao usuário que insira um número válido.

        Este método exibe a mensagem fornecida e aguarda uma entrada numérica do usuário. 
        Caso o usuário insira um valor inválido (não numérico), uma mensagem de erro será exibida 
        e a entrada será solicitada novamente até ser válida.

        Args:
            mensagem (str): A mensagem a ser exibida ao solicitar a entrada do usuário.

        Returns:
            float: O valor numérico (float) inserido pelo usuário.

        Example:
            numero = GenericUtil.entrarNumero("Digite um número: ")
        """
        while True:
            try:
                numero = float(input(mensagem))
                return numero
            except ValueError:
                print("Erro: número inválido!")
    @staticmethod
    def entrarTexto(mensagem: str):
        """
        Solicita ao usuário que insira um texto válido.

        Este método exibe a mensagem fornecida e aguarda uma entrada textual do usuário. 
        Não são aceitos valores nulos ou vazios, e a entrada será solicitada novamente 
        até ser válida.

        Args:
            mensagem (str): A mensagem a ser exibida ao solicitar a entrada do usuário.

        Returns:
            str: O texto não vazio inserido pelo usuário.

        Example:
            texto = GenericUtil.entrarTexto("Digite uma descrição: ")
        """
        while True:
            texto = input(mensagem)
            if texto and texto.strip():
                return texto
            print("Erro: texto nulo ou vazio!")