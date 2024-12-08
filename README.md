# Sistema de Gestão de Estoque

Este projeto implementa um sistema de gestão de estoque, com funcionalidades para adicionar, listar, atualizar, remover, e manipular o estoque de itens, como produtos de informática (notebooks, mouses, teclados, etc.). O sistema é organizado com as classes de Produto, ProdutoService, ProdutoRepository, e outras utilitárias, proporcionando uma interface simples para o gerenciamento de um estoque.

# Tecnologias Utilizadas

- Python 3.x
- Estrutura baseada em POO (Programação Orientada a Objetos)
- Arquitetura: MVC (Model-View-Controller)
- Exceções customizadas para validação de dados

# Funcionalidades

## Produto

A classe Produto é a representação de um produto no sistema, contendo os seguintes atributos:

- descricao: Descrição do produto (ex: "Notebook Dell").
- codigo: Código único do produto (ex: 201).
- quantidade: Quantidade disponível do produto no estoque.
- custoItem: Custo do produto.
- precoVenda: Preço de venda do produto.

Além disso, a classe oferece métodos para:

- Calcular o valor total de um produto (calcularValorTotal).
- Calcular o lucro presumido do produto (calcularLucroPresumido).

## ProdutoRepository

O ProdutoRepository atua como um repositório intermediário entre a fonte de dados e a aplicação, oferecendo as seguintes funcionalidades:

- criar: Adiciona um novo produto ao estoque.
- listar: Retorna todos os produtos cadastrados no estoque.
- buscarPorCodigo: Busca um produto pelo código.
- buscarPorDescricao: Busca produtos com base na descrição.
- ordenarPorQuantidade: Ordena os produtos pela quantidade em estoque (crescente ou decrescente).
- consultarProdutosEsgotados: Consulta todos os produtos esgotados (quantidade = 0).
- filtrarPorLimiteDeQuantidade: Filtra produtos cuja quantidade seja menor ou igual ao limite especificado.
- remover: Remove um produto do estoque.
- aumentarQuantidade: Aumenta a quantidade de um produto em estoque.
- diminuirQuantidade: Diminui a quantidade de um produto em estoque.
- atualizarPreco: Atualiza o preço de venda de um produto.

## ProdutoService

O ProdutoService oferece uma camada de lógica de negócios, utilizando o ProdutoRepository para:

- Criar, listar, buscar e manipular produtos no estoque.
- Validar regras de negócio, como: código do produto, quantidade e preço de venda.
- Gerar relatórios, como o lucro presumido total dos produtos em estoque.

## ProdutoUtil

A classe ProdutoUtil provê métodos utilitários para interagir com o sistema, incluindo:

- formatarValorMonetario: Formata um valor monetário para o formato brasileiro (R$).
- criar: Interage com o usuário para criar um novo produto.
- atualizarPreco: Permite ao usuário atualizar o preço de venda de um produto.
- aumentarQuantidade e diminuirQuantidade: Permitem ao usuário aumentar ou diminuir a quantidade de produtos no estoque.
- menu: Exibe o menu principal de operações, permitindo ao usuário escolher diferentes opções de interação com o sistema.

## Mock

A classe Mock fornece dados iniciais de estoque para o sistema. Ela utiliza uma string formatada com informações de produtos, criando uma lista de objetos Produto com esses dados. Esse estoque simula a entrada de dados em um banco de dados.

## Estrutura do Projeto

```bash
/project-root
│
├── /model
│ └── produto.py # Contém a classe Produto
│
├── /repositories
│ └── produtoRepository.py # Contém a classe ProdutoRepository
│
├── /services
│ └── produtoService.py # Contém a classe ProdutoService
│
├── /utils
│ ├── produtoUtil.py # Contém a classe ProdutoUtil
│ └── genericUtil.py # Contém a classe GenericUtil
│
├── /exceptions
│ └── produtoExceptions.py # Contém a classe ProdutoException
│
└── /mock
└── mock.py # Contém a classe Mock
```

## Como Usar

1. Criação de Produtos:

   Você pode criar um produto utilizando a classe `ProdutoUtil` que interage com o usuário para obter os dados necessários (descrição, código, quantidade, custo e preço de venda).

   Exemplo:

   ```python
   produto = ProdutoUtil.criar()
   ```

2. Atualização de Preço de Venda

   Você pode atualizar o preço de venda de um produto existente:

   ```python
   ProdutoUtil.atualizarPreco()
   ```

3. Aumento ou Diminuição de Quantidade

   Você pode aumentar ou diminuir a quantidade de um produto no estoque:

   ```python
   ProdutoUtil.aumentarQuantidade()
   ProdutoUtil.diminuirQuantidade()
   ```

4. Buscar e Listar Produtos

   Você pode listar todos os produtos ou realizar buscas por descrição ou código:

   ```python
   ProdutoUtil.menuPesquisa()
   ```

5. Remover Produto

   Se desejar remover um produto, utilize:

   ```python
   ProdutoUtil.remover()
   ```

6. Relatório de Lucro Presumido

   O sistema pode gerar um relatório de lucro presumido com base nos produtos em estoque:

   ```python
   ProdutoUtil.formatarValorMonetario(ProdutoUtil.produtoService.totalDeLucroPresumidoEmEstoque())
   ```

7. Iniciar o Sistema

   Para iniciar o sistema de gerenciamento de produtos, basta rodar o seguinte código:

   ```python
   from utils.produtoUtil import ProdutoUtil
   ProdutoUtil.menu()
   ```

## Exceções

O sistema utiliza a classe `ProdutoException` para lançar exceções relacionadas a erros de validação, como:

- Código do produto já cadastrado.
- Preço de venda menor que o custo do item.
- Quantidade negativa ou inválida.

Exemplo de uso:

```python
try:
    produto = ProdutoUtil.criar()
except ProdutoException as e:
    print(e)
```
