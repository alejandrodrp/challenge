# Challenge FastAPI

Este proyecto es una aplicación web construida con FastAPI, SQLAlchemy y Alembic. La aplicación incluye funcionalidades para manejar usuarios, citas, doctores, especialidades, pacientes, tratamientos, seguros médicos e historiales médicos.

## Requisitos

- Python 3.10
- PostgreSQL
- Docker (opcional)

## Instalación

### Clonar el Repositorio

```sh
git clone https://github.com/tu-usuario/challenge-fastapi.git
cd challenge-fastapi

# Challenge FastAPI

Este proyecto es una aplicación web construida con FastAPI, SQLAlchemy y Alembic. La aplicación incluye funcionalidades para manejar usuarios, citas, doctores, especialidades, pacientes, tratamientos, seguros médicos e historiales médicos.

## Requisitos

- Python 3.10
- PostgreSQL
- Docker (opcional)

## Instalación

### Clonar el Repositorio

```sh
git clone https://github.com/tu-usuario/challenge-fastapi.git
cd challenge-fastapi
```

### Configurar el Entorno Virtual

```sh
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
```

### Instalar Dependencias

```sh
pip install -r requirements.txt
```

### Configurar Variables de Entorno

Crea un archivo .env en el directorio raíz del proyecto con las siguientes variables:

```env
DB_HOST=  # si se usa localhost, dentro de docker debe ponerse `host.docker.internal`
DB_USER=
DB_PASSWORD=
DB_PORT=
DB_NAME=
ACCESS_TOKEN_LIFETIME=
REFRESH_TOKEN_LIFETIME=
SECRET_KEY=
GUEST_HOST=
CONTAINER_HOST=
```

### Configurar la Base de Datos

Asegúrate de tener PostgreSQL instalado y ejecutándose. Luego, crea la base de datos:

```sh
psql -U postgres -c "CREATE DATABASE CHALLENGE;"
```

### Aplicar Migraciones

```sh
alembic upgrade head
```

## Ejecución de la Aplicación

### Usando Uvicorn

```sh
uvicorn app.main:app --reload
```

### Usando Docker

```sh
docker-compose up -d --build
```

### Crear Superusuario

```sh
python3 create_superuser.py <username> <email> <password>
```

## Endpoints

La aplicación expone varios endpoints para manejar las diferentes entidades. Aquí hay una lista de los principales endpoints.
Los metodos `GET /<ruta>` aceptan parametros de paginacion como `limit`, `page_size`, `page`. Los metodos `DELETE` aceptan el 
parametro booleano `soft` que indica si se realiza un `soft delete`:

### Autenticación

- `POST /auth/token`: Obtener un token de acceso (credenciales en `form-urlencoded`)
- `POST /auth/refresh-token`: Refrescar el token de acceso.
- `POST /auth/register`: Registrar un nuevo usuario.

### Usuarios

- `GET /user`: Obtener una lista de usuarios.
- `GET /user/{id}`: Obtener un usuario por ID.
- `POST /user`: Crear un nuevo usuario.
- `PUT /user/{id}`: Actualizar un usuario existente.
- `DELETE /user/{id}`: Eliminar un usuario (solo superusuarios).

### Doctores

- `GET /doctor`: Obtener una lista de doctores.
- `GET /doctor/{id}`: Obtener un doctor por ID.
- `POST /doctor`: Crear un nuevo doctor.
- `PUT /doctor/{id}`: Actualizar un doctor existente.
- `DELETE /doctor/{id}`: Eliminar un doctor.

### Especialidades

- `GET /especialidad`: Obtener una lista de especialidades.
- `GET /especialidad/{id}`: Obtener una especialidad por ID.
- `POST /especialidad`: Crear una nueva especialidad.
- `PUT /especialidad/{id}`: Actualizar una especialidad existente.
- `DELETE /especialidad/{id}`: Eliminar una especialidad.

### Pacientes

- `GET /paciente`: Obtener una lista de pacientes.
- `GET /paciente/{id}`: Obtener un paciente por ID.
- `POST /paciente`: Crear un nuevo paciente.
- `PUT /paciente/{id}`: Actualizar un paciente existente.
- `DELETE /paciente/{id}`: Eliminar un paciente.

### Tratamientos

- `GET /tratamiento`: Obtener una lista de tratamientos.
- `GET /tratamiento/{id}`: Obtener un tratamiento por ID.
- `POST /tratamiento`: Crear un nuevo tratamiento.
- `PUT /tratamiento/{id}`: Actualizar un tratamiento existente.
- `DELETE /tratamiento/{id}`: Eliminar un tratamiento.

### Seguros Médicos

- `GET /seguro_medico`: Obtener una lista de seguros médicos.
- `GET /seguro_medico/{id}`: Obtener un seguro médico por ID.
- `POST /seguro_medico`: Crear un nuevo seguro médico.
- `PUT /seguro_medico/{id}`: Actualizar un seguro médico existente.
- `DELETE /seguro_medico/{id}`: Eliminar un seguro médico.

### Historiales Médicos

- `GET /historial_medico`: Obtener una lista de historiales médicos.
- `GET /historial_medico/{id}`: Obtener un historial médico por ID.
- `POST /historial_medico`: Crear un nuevo historial médico.
- `PUT /historial_medico/{id}`: Actualizar un historial médico existente.
- `DELETE /historial_medico/{id}`: Eliminar un historial médico.

### Citas

- `GET /cita`: Obtener una lista de citas.
- `GET /cita/{id}`: Obtener una cita por ID.
- `POST /cita`: Crear una nueva cita.
- `PUT /cita/{id}`: Actualizar una cita existente.
- `DELETE /cita/{id}`: Eliminar una cita.

### Doctor Especialidad

- `GET /doctor_especialidad`: Obtener una lista de relaciones doctor-especialidad.
- `POST /doctor_especialidad`: Crear una nueva relación doctor-especialidad.
- `DELETE /doctor_especialidad`: Eliminar una relación doctor-especialidad.

## Middleware

La aplicación incluye un middleware para medir el tiempo de procesamiento de las solicitudes:

- `RequestTimePerformanceMiddleware`: Mide el tiempo de procesamiento de cada solicitud y lo registra en los logs.

## Migraciones

Las migraciones de la base de datos se manejan con Alembic. Los scripts de migración se encuentran en el directorio versions.

### Crear una Nueva Migración

```sh
alembic revision --autogenerate -m "Descripción de la migración"
```

### Aplicar Migraciones

```sh
alembic upgrade head
```

### Revertir Migraciones

```sh
alembic downgrade -1
```

## Contribuir

Si deseas contribuir a este proyecto, por favor sigue los siguientes pasos:

1. Haz un fork del repositorio.
2. Crea una nueva rama (`git checkout -b feature/nueva-funcionalidad`).
3. Realiza tus cambios y haz commit (`git commit -am 'Añadir nueva funcionalidad'`).
4. Sube tus cambios a tu rama (`git push origin feature/nueva-funcionalidad`).
5. Abre un Pull Request.

## Licencia

Este proyecto está licenciado bajo la Licencia MIT. Consulta el archivo `LICENSE` para más detalles.
```