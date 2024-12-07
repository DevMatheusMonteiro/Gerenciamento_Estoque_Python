class GenericUtil:
    @staticmethod
    def entrarNumero(mensagem: str):
        while True:
            try:
                numero = float(input(mensagem))
                return numero
            except ValueError:
                print("Erro: número inválido!")
    @staticmethod
    def entrarTexto(mensagem: str):
        while True:
            texto = input(mensagem)
            if not (texto == None or texto.strip() == ""):
                return texto
            print("Erro: texto nulo ou vazio!")