from model.produto import Produto
def lerCSV(string: str):
    return [linha for linha in string.split("#")]
def criarListaEstoque(linhas: list[str]):
    return [Produto(produto.split(";")[0],int(produto.split(";")[1]),int(produto.split(";")[2]),float(produto.split(";")[3]),float(produto.split(";")[4])) for produto in linhas]
def entrarNumero(mensagem: str):
    while True:
        try:
            numero = float(input(mensagem))
            return numero
        except ValueError:
            print("Erro: número inválido!")
def entrarTexto(mensagem: str):
    while True:
        texto = input(mensagem)
        if not (texto == None or texto.strip() == ""):
            return texto
        print("Erro: texto nulo ou vazio!")