def lerCSV(string):
    return [linha for linha in string.split("#")]
def criarListaEstoque(linhas):
    return [{"descricao": produto.split(";")[0], "codigo": int(produto.split(";")[1]), "quantidade": int(produto.split(";")[2]), "custoItem": float(produto.split(";")[3]),"precoVenda": float(produto.split(";")[4])} for produto in linhas]
def entrarNumero(mensagem):
    while True:
        try:
            numero = float(input(mensagem))
            return numero
        except ValueError:
            print("Erro: número inválido!")
def entrarTexto(mensagem):
    while True:
        texto = input(mensagem)
        if not (texto == None or texto.strip() == ""):
            return texto
        print("Erro: texto nulo ou vazio!")