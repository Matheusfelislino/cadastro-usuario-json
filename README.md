# 🗂️ Cadastro de Usuários com JSON

Segundo projeto da minha jornada de portfólio Python. Este projeto foca na manipulação de arquivos externos, persistência de dados e organização de código em módulos.

## 🚀 Objetivo
Criar um sistema de linha de comando (CLI) que permita cadastrar, listar e buscar usuários, garantindo que os dados não sejam perdidos ao fechar o programa.

## 🛠️ Tecnologias Utilizadas
* **Python 3.x**
* **JSON** (para armazenamento de dados)
* **OS & JSON Libs** (nativas do Python)

## 🧠 O que eu aprendi neste projeto
* **Persistência de Dados:** Como salvar e ler informações em arquivos `.json`.
* **Modularização:** Divisão do código em `main.py` (interface) e `funcoes.py` (lógica) para melhor manutenção.
* **Validação de Dados:** Tratamento de erros para entradas inválidas (como idade que não é número) e verificação de e-mails duplicados.
* **Manipulação de Listas e Dicionários:** Estruturas fundamentais para organizar os dados antes de salvar.

## 📂 Estrutura do Repositório
* `main.py`: Ponto de entrada que gerencia o menu e a interação com o usuário.
* `funcoes.py`: Contém toda a lógica de leitura, escrita, validação e busca.
* `usuarios.json`: Arquivo gerado automaticamente para guardar os cadastros.