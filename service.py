import repository
import util
def validarCodigo(codigo):
    return not repository.buscarPorCodigo(codigo)
def validarQuantidade(quantidade):
    return quantidade >= 0
def validarPrecoVenda(precoVenda, custoItem):
    return precoVenda >= custoItem
def entrarCodigo():
    while True:
        codigo = int(util.entrarNumero("Entre com o código do produto: "))
        if validarCodigo(codigo):
            return codigo
        print("Erro: código já cadastrado!")
def entrarQuantidade():
    while True:
        quantidade = int(util.entrarNumero("Entre com a quantidade do produto: "))
        if validarQuantidade(quantidade):
            return quantidade
        print("Erro: quantidade não pode ser negativa")
def entrarPrecoVenda(custoItem):
    while True:
        precoVenda = util.entrarNumero("Entre com o preço de venda do produto: ")
        if validarPrecoVenda(precoVenda, custoItem):
            return precoVenda
        print("Erro: preço de venda não pode ser menor que o custo do item!")
def criar():
    descricao = util.entrarTexto("Entre com a descrição do produto: ").strip()
    codigo = entrarCodigo()
    quantidade = entrarQuantidade()
    custoItem = util.entrarNumero("Entre com o custo do produto: ")
    precoVenda = entrarPrecoVenda(custoItem)
    produto = {"descricao": descricao, "codigo": codigo, "quantidade": quantidade, "custoItem": custoItem, "precoVenda": precoVenda}
    repository.criar(produto)
def exibirProdutos():
    for produto in repository.listar():
        print(f"Código: {produto["codigo"]}\nDescrição: {produto["descricao"]}\nQuantidade: {produto["quantidade"]}\nCusto do Item: {produto["custoItem"]}\nPreço de Venda: {produto["precoVenda"]}\n************")