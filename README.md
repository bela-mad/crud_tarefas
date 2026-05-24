# Gerenciador de Tarefas de Estudo com TDD

<p align="justify">Este projeto é um pequeno sistema de CRUD de tarefas de estudo desenvolvido com a metodologia TDD (Test Driven Development) pela discente Isabela Madureira Argolo para a disciplina de DEC095 - Engenharia de Software.

<p align="justify">O objetivo principal é demonstrar, de forma prática, como escrever testes antes da implementação das funcionalidades, seguindo o ciclo Red, Green e Refactor.

## Descrição do projeto

<p align="justify">O sistema permite gerenciar tarefas de estudo de forma simples. Cada tarefa possui:

- ID;
- Título;
- Descrição;
- Status.

<p align="justify">Os dados são armazenados em memória, sem uso de banco de dados, pois o foco da atividade é a aplicação da metodologia TDD.

## Funcionalidades

<p align="justify">O projeto possui as seguintes funcionalidades:

- Criar tarefa de estudo;
- Buscar todas as tarefas;
- Buscar tarefa por ID;
- Atualizar tarefa existente;
- Remover tarefa;
- Retornar `null` quando uma tarefa inexistente for buscada.

## Tecnologias utilizadas

- **Python**: linguagem utilizada para implementação;
- **unittest**: biblioteca padrão do Python utilizada para os testes automatizados;
- **Git**: ferramenta de controle de versão;
- **GitHub**: plataforma para hospedagem do repositório;
- **Docstrings**: recurso usado para documentar o código fonte.

## Estrutura do projeto

```
crud_tarefas/
│
├── src/
│   ├── __init__.py
│   └── tarefa_service.py
│
├── tests/
│   ├── __init__.py
│   └── test_tarefa_service.py
│
└── README.md
```

## Metodologia TDD

<p align="justify">O desenvolvimento foi realizado utilizando a metodologia TDD, que consiste em escrever os testes antes da implementação do código funcional. O ciclo utilizado foi:

1. **Red**: criação de um teste para uma funcionalidade ainda não implementada, fazendo o teste falhar;
2. **Green**: implementação do código mínimo necessário para o teste passar;
3. **Refactor**: melhoria e organização do código, mantendo todos os testes funcionando.

## Como instalar o projeto

Clone o repositório:

```
git clone https://github.com/bela-mad/crud_tarefas.git
```

Acesse a pasta do projeto:

```
cd crud_tarefas
```

Como o projeto utiliza apenas bibliotecas padrão do Python, não é necessário instalar dependências externas.

## Como executar os testes

Para executar os testes automatizados, utilize o comando:

``` 
python -m unittest discover -s tests
```

## Testes implementados

Foram implementados testes para os seguintes cenários:

- Deve criar uma tarefa de estudo;
- Deve listar todas as tarefas;
- Deve buscar uma tarefa por ID;
- Deve atualizar uma tarefa;
- Deve remover uma tarefa;
- Deve retornar None ao buscar uma tarefa inexistente;
- Deve retornar None ao atualizar uma tarefa inexistente;
- Deve retornar False ao remover uma tarefa inexistente.

## Como visualizar a documentação

A documentação do código fonte foi criada utilizando docstrings em Python. 
Para visualizar a documentação pelo terminal, execute:

```
python
```

Depois, dentro do terminal interativo do Python, execute:

```
from src.tarefa_service import TarefaService
help(TarefaService)
```

Esse comando apresenta a documentação dos métodos e da classe responsável pelo gerenciamento das tarefas.