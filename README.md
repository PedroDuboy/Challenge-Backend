# Challenge-Backend
Challenge Backend [ Link](https://docs.google.com/document/d/1owcrxQc4OqowWj0k_Q9fTZtSLs0tFuxRNxP0vWsrzSo/edit)

## Desafío y Tareas
Para una mejor comprensión y seguimiento, desglosé el desafío en diversas tareas. Las tareas completas están marcadas con ✅.
## 

construir un servicio que permita a un usuario descubrir qué cursos han tomado sus amigos. ✅

Enumerar todos los usuarios en el sistema. ✅
 
Enumerar todas las amistades registradas en el sistema. ✅

Lista de todos los amigos para un usuario específico. ✅

Lista de lecciones que ha tomado un usuario específico. ✅

Integrar cualquier API gratuita de tu elección. ✅

Agregar pruebas unitarias a tu código (puntos extra).

Agregar un diseño UML de la solución (puntos extra).


# Instrucciones de Ejecución 

- Descargar el ZIP o clonar el repositorio.

- Para poder descargar todas las dependencias creamos un entorno virtual llamado venv.

➖ Code: python3 -m venv venv

- Activar el entorno virtual.

➖ Code: source venv/bin/activate

- Una vez el entono virtual activado, procedemos a descargar todas las dependencias para que el proyecto corra.

➖ Code: pip install -r requirements.txt

- Una vez todas las dependencias descargadas podemos correr el código ejecutando 

➖ Code: python3 manage.py runserver

## Usuario Admin

- Usuario: Administrador
- Clave: prueba123

## Implementación del sistema de Lecciones entre Amigos

La construcción del sistema de lecciones entre amigos lo enfoqué en la gestión de datos de los usuarios, utilizando tres modelos para estructurar la interacción entre estudiantes, cursos y sus inscripciones.


- Modelo de Estudiantes: almacena la información de los estudiantes. Cada estudiante puede seleccionar las materias que cursará durante un trimestre. Esta elección se realiza a través de una relación de muchos a muchos con el modelo de Cursos.

- Modelo de Cursos: Almacena las materias disponibles. Acá se definen los cursos que los estudiantes pueden elegir.


(Después de que un estudiante se ha registrado y seleccionado sus materias, el siguiente paso es la inscripción) ⚠️

- Modelo de Inscripción Lección: almacena las inscripciones de los estudiantes en cursos específicos, permitiendo que un usuario pueda cursar el mismo tema múltiples veces. 

IMPORTANTE: Un usuario puede tener todas las materias seleccionadas, la contabilización efectiva ocurre únicamente al realizar la inscripción. Esto proporciona flexibilidad al usuario, permitiéndole planificar sus estudios de manera personalizada.

En el sistema no implemente la “autenticación JWT.” Simplemente, le pasé como usuario a Joe. 

## Implementacion de API

Implemente la API de [ Open-Meteo](https://open-meteo.com/) mostrando la información del clima actual 