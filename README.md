## FUNDAMENTOS DE CONSUMO Y CONSTRUCCIÓN DE APIs

Este proyecto fue realizado para el curso brindado por [Datapath](https://datapath.teachable.com/).
Se realizó una API que proporciona funcionalidades para gestionar una base de datos de personas. Cada persona en la base de datos tiene atributos como nombre, lenguaje, ID, biografía y versión.

## Funcionalidades Principales

### 1. Obtener Lista de Personas

- **Endpoint:** `/api/people/get_all`
- **Método:** GET
- **Descripción:** Obtiene la lista completa de personas en la base de datos.
- **Respuesta Exitosa:**
![Get_people](/imagenes/get_people.png)

## 2. Obtener Detalles de una Persona

- **Endpoint:** /api/people/{id}
- **Método:** GET
- **Descripción:** Obtiene los detalles de una persona específica según su ID.
- **Respuesta Exitosa:**
![Get_person](/imagenes/get_person.png)

## 3. Agregar Nueva Persona

- **Endpoint:** /api/people
- **Método:** POST
- **Descripción:** Agrega una nueva persona a la base de datos.
- **Respuesta Exitosa:**
- ![Create_person](/imagenes/create_person.png)

## 4. Actualizar Persona Existente

- **Endpoint:** /api/people/{id}
- **Método:** PUT
- **Descripción:** Actualiza los detalles de una persona existente según su ID.
- **Respuesta Exitosa:**
- ![Update_person](/imagenes/update_person.png)

## 5. Eliminar Persona
- **Endpoint:** /api/people/{id}
- **Método:** DELETE
- **Descripción:** Elimina una persona de la base de datos según su ID.
- **Respuesta Exitosa:**
![Delete_person](/imagenes/delete_person.png)

## Deploy

Se realizó el deploy de la API por medio de Render, la misma se puede encontrar [aquí](https://fundamentosapi.onrender.com/docs).
