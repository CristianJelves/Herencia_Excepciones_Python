# Herencia Y Excepciones En Python

## Descripción
Propósito: Implementar una jerarquía de clases con herencia, polimorfismo y manejo de excepciones personalizadas en Python.  
Enfoque: Mostrar de forma simple cómo heredar, sobrescribir métodos, usar polimorfismo y capturar errores con `try/except/finally`.

## Objetivos
- Herencia: Crear clases base y subclases con atributos y métodos propios.
- Polimorfismo: Usar funciones que operen con distintas clases de la jerarquía.
- Excepciones: Definir y manejar excepciones personalizadas junto a excepciones estándar.
- Comprensión: Mostrar el orden de resolución de métodos (MRO).
 
## Requisitos
- Python: 3.10 o superior.
- Dependencias: No requiere librerías externas.

## Diseño De Clases (Resumen)
- `Usuario`: Clase base con `nombre`, `correo` y método `presentarse()`.
- `Administrador(Usuario)`: Agrega `permisos` (lista), sobrescribe `presentarse()` y define operaciones de administración (p. ej., `agregar_permiso`, `eliminar_usuario`).
- `Soporte`: Clase independiente con comportamiento de soporte técnico.
- `SuperUsuario(Administrador, Soporte)`: Hereda de ambas (herencia múltiple) y expone el **MRO**.

## Polimorfismo Y Sobrecarga (Idea)
- Polimorfismo: Funciones que aceptan cualquier instancia de la jerarquía (p. ej., `mostrar_usuario(usuario)` para `Usuario`, `Administrador`, `SuperUsuario`, etc.).  
- Parámetros por defecto / `*args`: Simulan sobrecarga de métodos en Python cuando se necesitan firmar comportamientos distintos.

## Excepciones Personalizadas
- `UsuarioNoEncontrado(Exception)`: Se lanza cuando se intenta operar sobre un usuario inexistente (p. ej., eliminar).  
- Bloques de manejo:  
  - `try/except`: Captura `UsuarioNoEncontrado` y muestra un mensaje claro.  
  - `finally`: Ejecuta un mensaje de cierre de operación.

## Ejecución De Ejemplo
- Crear un `Administrador`, agregar permisos y presentarlo.
- Intentar eliminar un usuario inexistente para activar la excepción personalizada.
- Mostrar el **MRO** de `SuperUsuario` para evidenciar el orden de búsqueda de métodos.
