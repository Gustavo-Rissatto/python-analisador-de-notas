# Analisador de Notas em Python

Projeto desenvolvido para praticar os fundamentos da programação com Python, organização de código, trabalho em equipe e uso do GitHub.

O programa permite cadastrar alunos e suas notas, calcular médias e apresentar informações gerais sobre o desempenho da turma.

## Funcionalidades

* Cadastro do nome dos alunos
* Cadastro de três notas por aluno
* Cálculo da média individual
* Identificação de alunos aprovados e reprovados
* Cálculo da média geral da turma
* Identificação do aluno com a maior média
* Encerramento do cadastro ao digitar `fim`
* Validação das notas informadas

## Tecnologias utilizadas

* Python
* Git
* GitHub
* Visual Studio Code

## Estrutura do projeto

```text
python-analisador-de-notas/
├── README.md
├── diagnostico.py
├── analisador_turma.py
├── requirements.txt
├── .gitignore
└── docs/
    └── aprendizados.md
```

## Como executar o projeto

Primeiro, clone o repositório:

```bash
git clone URL_DO_REPOSITORIO
```

Entre na pasta do projeto:

```bash
cd python-analisador-de-notas
```

Execute o programa individual:

```bash
python diagnostico.py
```

Execute o analisador da turma:

```bash
python analisador_turma.py
```

Em alguns computadores, pode ser necessário usar:

```bash
python3 analisador_turma.py
```

## Exemplo de uso

```text
Digite o nome do aluno: Ana
Digite a primeira nota: 8
Digite a segunda nota: 7
Digite a terceira nota: 9

Aluno: Ana
Média: 8.0
Situação: Aprovado
```

## Regras do projeto

* A média mínima para aprovação é `7.0`.
* Cada aluno possui três notas.
* As notas devem estar entre `0` e `10`.
* O cadastro é encerrado quando o usuário digita `fim`.

## Divisão de tarefas

### Buguelo

* Cadastro dos alunos
* Validação das notas
* Cálculo da média individual

### Marquin

* Cálculo da média geral da turma
* Contagem de aprovados e reprovados
* Identificação do aluno com maior média

### Desenvolvimento em conjunto

* Testes do programa
* Correção de erros
* Organização do código
* Documentação do projeto

## Conceitos praticados

Durante o desenvolvimento, foram praticados os seguintes conceitos:

* Variáveis
* Tipos de dados
* Entrada e saída de informações
* Condições
* Estruturas de repetição
* Listas
* Funções
* Tratamento de erros
* Organização de código
* Git e GitHub
* Trabalho com branches e commits

## Aprendizados

Este projeto ajudou a compreender como dividir um problema maior em funções menores, validar informações digitadas pelo usuário e trabalhar de forma colaborativa usando Git e GitHub.

As dificuldades e soluções encontradas durante o desenvolvimento estão registradas no arquivo:

## Melhorias futuras

* Criar uma interface gráfica
* Salvar os dados dos alunos em arquivo
* Exportar resultados para CSV
* Criar gráficos de desempenho
* Adicionar testes automatizados
* Transformar o projeto em uma aplicação web

## Autores

Desenvolvido por:

* Gustavo Rissatto
* Marco Antonio

Projeto criado como parte dos estudos de Python, Inteligência Artificial e Redes Neurais.
