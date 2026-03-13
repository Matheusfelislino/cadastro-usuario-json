# 🗂️ Cadastro de Usuários com JSON

Segundo projeto da minha jornada de portfólio Python.  
Este projeto foca na manipulação de arquivos externos, persistência de dados e organização de código em módulos.

---

## 🚀 Objetivo

Criar um sistema de linha de comando (CLI) que permita cadastrar, listar e buscar usuários, garantindo que os dados não sejam perdidos ao fechar o programa.

O sistema simula um pequeno gerenciador de usuários utilizando **persistência em arquivo JSON**, em vez de armazenamento apenas em memória.

---

## 📌 Status do Projeto

Este projeto está em evolução e faz parte do meu portfólio de estudos em Python.

Melhorias planejadas:

- aprimorar validações de dados
- melhorar tratamento de erros
- adicionar novos tipos de busca
- evoluir a estrutura do projeto

---

## 🛠️ Tecnologias Utilizadas

- **Python 3.x**
- **JSON** (armazenamento de dados)
- **Bibliotecas nativas do Python**
  - `json`
  - `os`

---

## 🧠 O que eu aprendi neste projeto

- **Persistência de Dados:** Como salvar e ler informações em arquivos `.json`.
- **Modularização:** Divisão do código em `main.py` (interface) e `funcoes.py` (lógica).
- **Validação de Dados:** Tratamento de entradas inválidas (idade não numérica, e-mails duplicados, etc.).
- **Manipulação de Listas e Dicionários:** Estruturas fundamentais para organizar os dados antes de salvar.

---

## 📂 Estrutura do Projeto
cadastro-usuario-json/
├── main.py # Interface do sistema e menu principal
├── funcoes.py # Funções de leitura, escrita e validação
├── usuarios.json # Arquivo de persistência de dados
└── README.md # Documentação do projeto

---

## ▶️ Como Executar

1. Clone o repositório
git clone https://github.com/Matheusfelislino/cadastro-usuario-json.git

2. Entre na pasta do projeto
cd cadastro-usuario-json

3. Execute o sistema
python3 main.py

---

## 💻 Exemplo de Uso
--- SISTEMA DE CADASTRO ---
Cadastrar Usuário
Listar Todos
Buscar por E-mail
Sair

O usuário pode cadastrar novas pessoas, visualizar todos os registros ou buscar um usuário específico pelo e-mail.

---

## 📈 Possíveis Melhorias Futuras

- criação de interface gráfica
- integração com banco de dados
- testes automatizados
- organização do projeto em camadas

---

## 👨‍💻 Autor

Projeto desenvolvido por **Matheus Felis Lino** como parte do portfólio de estudos em desenvolvimento Python.