# E-Commerce API (Django Ninja)

API RESTful para e-commerce desenvolvida com Django, Django Ninja e autenticação JWT, gerenciada com `uv` e suporte a Docker.

## 🚀 Tecnologias

- **Linguagem:** Python 3.12+
- **Framework:** Django & Django Ninja
- **Autenticação:** JWT (JSON Web Tokens) com UUID nativo para usuários
- **Gerenciador de Ambientes e Dependências:** [uv](https://github.com/astral-sh/uv)
- **Containerização:** Docker & Docker Compose

---

## 🛠️ Como Rodar Localmente (com `uv`)

### 1. Pré-requisitos
Certifique-se de ter o `git` e o `uv` instalados na sua máquina:
```bash
# Instalação do uv (se ainda não possuir)
curl -LsSf [https://astral.sh/uv/install.sh](https://astral.sh/uv/install.sh) | sh
```

### 2. Clonar e sincronizar o ambiente
```bash
git clone [https://github.com/andersonsimplicio/e-commerce.git](https://github.com/andersonsimplicio/e-commerce.git)
cd e-commerce

# Instala a versão correta do Python e todas as dependências travadas no uv.lock
uv sync
```

### 3. Configurar variáveis de ambiente
```bash
cp .env.example .env
```

### 4. Executar migrações e testes
```bash
uv run python manage.py migrate
uv run python manage.py test
```

### 5. Iniciar o servidor de desenvolvimento

```bash
uv run python manage.py runserver
```

#### Acesse a documentação interativa (Swagger OpenAPI) em:

#### 👉 http://127.0.0.1:8000/api/docs

### Como Rodar com Docker
#### Se preferir rodar toda a aplicação e serviços auxiliares via contêineres:

```bash
docker compose up -d --build
docker compose exec web python manage.py migrate
docker compose exec web python manage.py test
```

#### Como Rodar com Docker

##### Rodar todos os testes

```bash
uv run python manage.py test
```
#### Rodar apenas testes de autenticação/usuários

```bash
uv run python manage.py test apps.users
```