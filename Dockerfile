FROM python:3.12-slim-bookworm

# Copia o binário oficial do uv
COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/uv

# Configura o PATH para usar automaticamente o venv criado pelo uv
ENV PYTHONUNBUFFERED=1 \
    UV_COMPILE_BYTECODE=1 \
    PATH="/app/.venv/bin:$PATH"

WORKDIR /app

# Copia os arquivos de dependência
COPY pyproject.toml uv.lock ./

# Instala as dependências (cria /app/.venv)
RUN uv sync --frozen --no-dev

# Copia o código da aplicação
COPY . .

EXPOSE 8000

# Executa o manage.py usando o python do ambiente virtual
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]