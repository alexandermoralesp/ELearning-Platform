# JKorp
>Plataforma de E-Learning enfocado al uso de subscripciones.

## **1. Requerimientos:**
### **1.1 Requerimientos Funcionales:**

 - La aplicación debe contener un __inicio de sesión__, __cierre de     
   sesión__ y __reistro de cuenta__
- El usuario podrá __inicio de sesión__ y __registrarse__ por las cuentas de Google y Facebook.
- Los usuarios clientes podrán acceder a cada uno de los cursos,
   dependiendo de la subscripción a la que ha adquirido.
- Se tendrá una carro de compras que mantendrá los cursos deseados en
   lista.  
- Al culminar con cada uno de los cursos se generará un certificado
   automáticamente.
- Cada estudiante al llevar un curso sumará una cantidad de puntos en
   cuanto al puntejo adquirido en las prácticas.
- En cada sección se tendrá un quiz de práctica de acuerdo al tema
   principal.
- Se visualizará los cursos en progreso y completados.

  

### **1.2 Requerimientos No Funcionales:**

 - Los usuarios clientes podrán acceder a los cursos dependiendo el tipo
   de subscripción que tenga. Cada usuario tendrá una lista de cursos
   (completado, no completado, en bolsa)
 - Los usuarios administradores tendrá la visibilidad de editar y
   mantener cada uno de los componentes de la plataforma.
 - Los usuarios propietarios son los únicos que visualizarán el flujo de
   información y transacciones dentro de la plataforma. (Los datos se
   encriptaran en todo momento, siendo así imposible de ver la data en
   bruta, sino el flujo en general)
 - La pasarela de pago será implementada por medio de una API de un
   servicio.

## **2. Modelo relacional:**
### Tablas entidad:
- Usuario
- Roadmaps
- Cursos
- Secciones
- Estudiantes
- Docentes
- Exámenes
### Tablas de relacion entre entidades:
- Curso_Progreso()
- Alumno_Curso_Examen()

### Diseño del Sistema en Producción
- 