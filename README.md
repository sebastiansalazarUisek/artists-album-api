# 🎵 Music API - Backend

## 📖 Descripción

Music API es una API REST desarrollada con **Django** y **Django REST Framework** para la gestión de artistas y álbumes musicales.

La aplicación implementa operaciones CRUD completas, autenticación mediante OAuth 2.0, carga de imágenes para artistas, permisos basados en autenticación y una arquitectura preparada para ser consumida por un frontend desarrollado en React o cualquier otro cliente HTTP.

---

## 🚀 Características

- CRUD completo de artistas.
- CRUD completo de álbumes.
- Relación uno a muchos entre artistas y álbumes.
- Carga de imágenes para artistas.
- Autenticación mediante OAuth 2.0.
- Permisos de acceso según autenticación.
- Serializers anidados para consultas.
- Filtrado de álbumes por artista.
- API preparada para integración con React.

---

## 🛠️ Tecnologías utilizadas

- Python
- Django
- Django REST Framework
- Django OAuth Toolkit
- SQLite
- Pillow
- django-cors-headers
- Postman
- Git
- GitHub

---

## 📂 Estructura del proyecto

```text
artists-album-api/
│
├── config/
├── music/
├── media/
│   └── artist_images/
├── manage.py
├── requirements.txt
└── README.md
```

---

## 🗄️ Modelo de datos

### Artista

- Nombre
- País
- Género
- Fecha de debut
- Imagen

### Álbum

- Título
- Año de lanzamiento
- Número de canciones
- Artista (Foreign Key)

```text
Artista (1)
     │
     └──────────────< Álbum (N)
```

---

## 🔐 Autenticación y permisos

La API utiliza **OAuth 2.0** mediante **Django OAuth Toolkit**.

### Usuarios no autenticados

- Consultar artistas.
- Consultar álbumes.

### Usuarios autenticados

- Crear artistas.
- Editar artistas.
- Eliminar artistas.
- Crear álbumes.
- Editar álbumes.
- Eliminar álbumes.

Las operaciones protegidas requieren enviar un **Bearer Token** válido.

---

## 🌐 Endpoints principales

### Artistas

| Método | Endpoint |
|---------|----------|
| GET | `/api/artists/` |
| POST | `/api/artists/` |
| PUT | `/api/artists/{id}/` |
| PATCH | `/api/artists/{id}/` |
| DELETE | `/api/artists/{id}/` |

### Álbumes

| Método | Endpoint |
|---------|----------|
| GET | `/api/albums/` |
| POST | `/api/albums/` |
| PUT | `/api/albums/{id}/` |
| PATCH | `/api/albums/{id}/` |
| DELETE | `/api/albums/{id}/` |

### OAuth

| Método | Endpoint |
|---------|----------|
| POST | `/o/token/` |

---

## ⚙️ Instalación

Clonar el repositorio:

```bash
git clone https://github.com/sebastiansalazarUisek/artists-album-api.git
```

Crear un entorno virtual:

```bash
python -m venv venv
```

Activar el entorno virtual.

Instalar dependencias:

```bash
pip install -r requirements.txt
```

Aplicar migraciones:

```bash
python manage.py migrate
```

Iniciar el servidor:

```bash
python manage.py runserver
```

---

## 🧪 Pruebas realizadas

La API fue validada utilizando:

- Django REST Framework Browsable API
- Postman

Se verificó el correcto funcionamiento de:

- CRUD de artistas.
- CRUD de álbumes.
- Autenticación OAuth 2.0.
- Permisos de acceso.
- Carga de imágenes.
- Filtrado de álbumes por artista.

---

## 🌍 Configuración CORS

Se configuró **django-cors-headers** para permitir la comunicación entre el backend desarrollado con Django y el frontend desarrollado con React durante el entorno de desarrollo.

---

## 👨‍💻 Autor

**Sebastián Salazar**

Estudiante de Ingeniería en Software

QA Engineer