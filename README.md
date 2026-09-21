# E-Commerce API (Django Ninja)

API RESTful desenvolvida com Django Ninja e gerenciada via `uv`.

## 🚀 Tecnologias
- Python 3.12+
- Django & Django Ninja
- Gerenciador de pacotes: `uv`

## 🛠️ Como rodar localmente

1. Clone o repositório:
   ```bash
   git clone https://github.com/andersonsimplicio/e-commerce
   cd e-commerce
   ```

2. Crie e ative a venv:
   ```bash
   uv venv
   source .venv/bin/activate
   ```

3. Instale as dependências:
   ```bash
    uv pip install django django-ninja
   ```

4. Execute as migrações e o servidor:
   ```bash
   python manage.py migrate
   python manage.py runserver
   ```

Docs interativas disponíveis em: `http://127.0.0.1:8000/api/docs`