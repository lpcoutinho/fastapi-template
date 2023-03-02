# fastapi-template
###  🏗️ Em Construção
<!-- ![GitHub repo size](https://img.shields.io/github/repo-size/lpcoutinho/smart-home)
![GitHub language](https://img.shields.io/github/languages/top/lpcoutinho/smart-home?style=for-the-badge) -->

>O objetivo é desenvolver um template básico para se construir APIs. Nele haverá uma tabela de usuários com senhas criptografadas, além de autenticação por token, recuperação de login, etc.

### 💻 Pré-requisitos

Antes de começar, verifique se você atendeu aos seguintes requisitos:

* Python >= 3.11  
* Docker
* Insomnia
* PostgreSQL

## 🚀 Instalando o Projeto

### 1. Inicie um ambiente virtual

Linux e macOS:
```bash
# Instale e rode um ambiente virtual
python3 -m venv venv
. venv/bin/activate

# Instale os requerimentos
pip install -r requirements.txt
```

Windows:
```bash
<!-- TODO INSERIR COMANDOS DE INSTALAÇÃO E EXECUÇÃO DE VENV-->
# Instale os requerimentos
pip install -r requirements.txt
```

### 2. Monte os bancos de dados
Montaremos duas bases de dados com docker compose. Uma para testes e outra para deenvolvimento.

```bash
# Rode os containers em egundo plano
docker-compose up -d
```

Realize as migrações com Alembic para contruir as tabelas

```bash
alembic upgrade head
```

Crie o primeiro usuário e verifique se tudo está ok no banco de dados
```bash
python -m app.initial_data
```

### x. ☕ Rodando em ambiente local

```bash
uvicorn main:app --reload
```
Verifique se a API esá online em  http://127.0.0.1:8000/healthcheck

Para consltar a documentação clique [aqui](http://127.0.0.1:8000/docs)

### 🐋 Rodando com Docker

Nosso docker-compose.yml já está configurado para rodar a API.

```
docker compose up
```

Para rodar em segundo plano

```
docker compose up -d
```

Verifique se a API esá online em  http://127.0.0.1:8000/healthcheck

Para consultar a documentação clique [aqui](http://127.0.0.1:8000/docs)
