# 🎵 Music API

## 📖 Descripción

Music API es una aplicación web desarrollada con **Django** y **Django REST Framework** que permite administrar artistas y álbumes mediante una API REST.

El proyecto implementa un CRUD completo para ambas entidades, permite la carga de imágenes para los artistas, protege los endpoints mediante autenticación OAuth 2.0 y ofrece una API lista para ser consumida por un frontend desarrollado en React o por herramientas como Postman.

El desarrollo se realizó siguiendo una arquitectura **Backend First**, priorizando la construcción y validación de la API antes de implementar la interfaz de usuario.

---

## 🎯 Objetivo

Desarrollar una API REST para la gestión de artistas y álbumes aplicando buenas prácticas de desarrollo backend, autenticación mediante OAuth 2.0, manejo de relaciones entre entidades y pruebas de funcionamiento utilizando Postman.

---

## 🚀 Funcionalidades

- Gestión de artistas (CRUD)
- Gestión de álbumes (CRUD)
- Relación Uno a Muchos (1:N) entre artistas y álbumes
- Carga de imágenes para artistas
- Autenticación mediante OAuth 2.0
- Protección de endpoints con Bearer Token
- Configuración de CORS para integración con React
- Pruebas de la API mediante Postman

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

artists-album-api/
│
├── config/
├── music/
├── artist_images/
├── manage.py
├── requirements.txt
└── README.md
```

---

## 🗄️ Modelo de Base de Datos

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
- Artista (Clave Foránea)

Relación:

```text
Artista (1) ───────────< Álbum (N)
```

---

## 🔐 Autenticación

La API utiliza **OAuth 2.0** mediante **Django OAuth Toolkit**.

Para acceder a los endpoints protegidos es necesario enviar un **Bearer Token** válido en cada petición.

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

## 🧪 Pruebas realizadas

La API fue validada mediante:

- Django REST Framework Browsable API
- Postman

Se probaron correctamente las siguientes operaciones:

- GET
- POST
- PUT
- PATCH
- DELETE
- Autenticación OAuth 2.0
- Autorización mediante Bearer Token

---

## 🌍 Configuración CORS

Se configuró CORS para permitir la comunicación entre el backend desarrollado en Django y el frontend desarrollado en React durante el entorno de desarrollo.

---

## 👨‍💻 Autor

**Sebastián Salazar**

Estudiante de Ingeniería en Software

QA Engineer