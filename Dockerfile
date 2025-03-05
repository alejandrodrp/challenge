FROM python:3.10

WORKDIR /challenge

# Copia primero las dependencias para no tener que reinstalar las depencias si cambia el codigo
COPY requirements.txt ./

# Instala las dependencias
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

COPY . .

# Expone el puerto en el que corre FastAPI (por defecto, 8000)
EXPOSE 8000

# Comando para ejecutar la aplicación con Uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
