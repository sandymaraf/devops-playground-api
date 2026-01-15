FROM python:3.10-slim

WORKDIR /app

# Copia dependências primeiro (pra aproveitar cache)
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Copia o resto do código
COPY . .

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
