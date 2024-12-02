def lerCSV(string):
    return [linha for linha in string.split("#")]
def criarListaEstoque(linhas):
    return [{"descricao": produto.split(";")[0], "codigo": produto.split(";")[1], "quantidade": produto.split(";")[2], "custoItem": produto.split(";")[3],"precoVenda": produto.split(";")[4]} for produto in linhas]