# DevOps Playground API

Projeto simples em FastAPI criado para praticar e demonstrar:

- CI/CD com GitHub Actions
- Testes automatizados com Pytest
- Criação de pipelines reutilizáveis
- Boas práticas de DevOps em projetos Python

---

## Objetivo

Este repositório serve como:

- Playground de DevOps
- Base para criação de templates de pipeline reutilizáveis
- Projeto demonstrativo para entrevistas técnicas

---

## Requisitos

Você precisa ter instalado:

- Python 3.10 ou superior
- python3-venv
- python3-pip
- git

No Ubuntu / Pop!_OS:

```bash
sudo apt update
sudo apt install -y python3 python3-venv python3-pip git

Estrutura do Projeto

devops-playground-api/
├── app/
│   ├── __init__.py
│   └── main.py
├── tests/
│   └── test_health.py
├── requirements.txt
└── README.md

Como rodar o projeto localmente
Clonar o repositório

git clone <URL_DO_REPO>
cd devops-playground-api

Criar e ativar o ambiente virtual

python3 -m venv .venv
source .venv/bin/activate

Atualizar o pip

pip install --upgrade pip

Instalar as dependências

pip install -r requirements.txt

Subir a aplicação

uvicorn app.main:app --reload

Acesse no navegador:

http://localhost:8000/health

Rodar os testes

pytest