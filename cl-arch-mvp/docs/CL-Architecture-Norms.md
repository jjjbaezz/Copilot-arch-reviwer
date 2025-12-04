# Core Library Architecture Norms

## Capa de Dominio
- Los casos de uso deben estar en `ios/Core/UseCases/` y `android/core/usecases/`.
- Cada caso de uso tiene un protocolo/interface, una implementación que delega en un interactor, y un coordinator que ensambla dependencias.
- El interactor implementa la lógica real y puede extenderse para separar la lógica del protocolo.

## Capa de Acceso a Datos
- Los modelos de entrada (Request) y salida (Response) deben ser públicos y tener inicializadores públicos.
- Los modelos privados deben ser `Codable` y no exponerse fuera del módulo.
- Los repositorios deben implementar un protocolo y abstraer el acceso a datos.
- Las fuentes remotas deben implementar un protocolo y encargarse de la comunicación HTTP.

## Prohibido
- Acceso directo a red desde el caso de uso.
- Uso de librerías externas no aprobadas.
- Lógica de negocio fuera de los interactores.

## Tests
- Cada caso de uso debe tener un test asociado en la ruta correcta.
- Los tests deben verificar el comportamiento esperado del caso de uso.
