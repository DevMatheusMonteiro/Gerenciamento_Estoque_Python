from model.produto import Produto
class Mock:
    """
    Classe responsável por fornecer dados mockados para o estoque de produtos.

    A classe `Mock` contém um método estático que cria uma lista de objetos `Produto`
    a partir de uma string de dados formatada, representando o estoque inicial.

    A string de dados `estoque_inicial` é composta por informações de produtos,
    separados por ponto e vírgula e organizados por hash (`#`), que incluem:
    - Descrição
    - Código
    - Quantidade
    - Custo do item
    - Preço de venda
    """
    estoque_inicial = "Notebook Dell;201;15;3200.00;4500.00#Notebook Lenovo;202;10;2800.00;4200.00#Mouse Logitech;203;50;70.00;150.00#Mouse Razer;204;40;120.00;250.00#Monitor Samsung;205;10;800.00;1200.00#Monitor LG;206;8;750.00;1150.00#Teclado Mecânico Corsair;207;30;180.00;300.00#Teclado Mecânico Razer;208;25;200.00;350.00#Impressora HP;209;5;400.00;650.00#Impressora Epson;210;3;450.00;700.00#Monitor Dell;211;12;850.00;1250.00#Monitor AOC;212;7;700.00;1100.00"
    @staticmethod
    def criarListaEstoque():
        """
        Cria uma lista de objetos `Produto` a partir da string de dados `estoque_inicial`.

        A string `estoque_inicial` contém informações de vários produtos, que são
        processados e transformados em objetos `Produto`.

        Retorna:
            list[Produto]: Uma lista contendo objetos `Produto` construídos com base
            nos dados da string `estoque_inicial`.

        Exemplo de uso:
            lista_produtos = Mock.criarListaEstoque()
        """
        return [Produto(produto.split(";")[0],int(produto.split(";")[1]),int(produto.split(";")[2]),float(produto.split(";")[3]),float(produto.split(";")[4])) for produto in [linha for linha in Mock.estoque_inicial.split("#")]]
    


