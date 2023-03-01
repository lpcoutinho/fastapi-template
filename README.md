# fastapi-template
###  🏗️ Em Construção
<!-- ![GitHub repo size](https://img.shields.io/github/repo-size/lpcoutinho/smart-home)
![GitHub language](https://img.shields.io/github/languages/top/lpcoutinho/smart-home?style=for-the-badge) -->

>O objetivo é desenvolver um template básico para se construir APIs. Nele haverá uma tabela de usuários com senhas criptografadas, além de autenticação por token, recuperação de login, etc.

## Tecnologias utilizadas
- FastAPI
- Uvicorn
- PostgreSQL
- Docker

### Obejetivos
- [x] Docker compose para rodar um banco de dados em produção e outro de testes
- [ ] Testar Conexão construindo a tabela de usuários
- [ ] Construir Models e Schemas


### 💻 Pré-requisitos

Antes de começar, verifique se você atendeu aos seguintes requisitos:

* Python >= 3.11  
* Docker
* Insomnia
* PostgreSQL

## 🚀 Instalando o Projeto

### 1. Rode os bancos de dados

```bash
### Setup two databases
docker-compose up -d
```

### 2. Inicie um ambiente virtual

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

### 3. ☕ Rodando em ambiente local

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
