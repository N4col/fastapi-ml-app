# Obraz bazowy z Pythonem
FROM python:3.9-slim

# Katalog roboczy w kontenerze
WORKDIR /app

# Kopiujemy pliki aplikacji do kontenera
COPY . .

# Instalacja zależności
RUN pip install --no-cache-dir -r requirements.txt

# Uruchamianie serwera FastAPI przez Uvicorn
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8080"]
