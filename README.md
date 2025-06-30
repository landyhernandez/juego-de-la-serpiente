# juego-de-la-serpiente
 Objetivo del Proyecto
Este proyecto tiene como propósito diseñar y desarrollar un videojuego interactivo utilizando la librería Turtle de Python. El reto consiste en programar el clásico juego de la serpiente, integrando movimiento controlado por el teclado, crecimiento dinámico del cuerpo al comer, detección de colisiones, y un sistema de puntaje que se actualiza en tiempo real. Además, se busca mejorar la estética visual del juego mediante el uso de colores personalizados y una interfaz amigable.
Librerías Utilizadas
- Python 3: lenguaje de programación interpretado y de alto nivel.
- turtle: módulo gráfico para construir objetos visuales de forma sencilla y visualmente atractiva.
- random: permite posicionar la comida en ubicaciones aleatorias.
- time: útil para controlar los tiempos de espera y dar fluidez al juego.

 Estructura y Componentes del Código
1. Ventana del Juego
Se configura una pantalla con fondo negro, dimensiones de 600x600 píxeles, y se activa el modo de animación manual con tracer(0) para optimizar el rendimiento gráfico.
 2. Cabeza de la Serpiente
Representada por un círculo color fucsia. Es el único elemento que el jugador controla directamente con las teclas direccionales.
 3. Comida
Elemento rojo que aparece en posiciones aleatorias. Si la serpiente lo toca, se genera un nuevo segmento en el cuerpo y se incrementa el puntaje.
 4. Cuerpo
Se añade una nueva pieza cada vez que la serpiente come. Cada segmento tiene un color pastel aleatorio, lo que genera una apariencia vibrante y amigable para el usuario.
 5. Puntaje
Se utiliza una función que actualiza el puntaje actual y el récord máximo en pantalla, utilizando tipografía tipo Courier y texto alineado al centro superior.

 Funciones Principales del Código

➤ Movimiento:
Las funciones arriba, abajo, izquierda, y derecha modifican la dirección de la serpiente. Luego, la función movimiento() actualiza su posición según la dirección seleccionada.

➤ Detección de Colisiones con la Comida
La función colisionComida() evalúa si la cabeza está lo suficientemente cerca de la comida. Si hay colisión:
- La comida se mueve a una nueva ubicación aleatoria.
- Se suma un nuevo segmento al cuerpo.
- Se incrementa el puntaje.
  
➤ Movimiento del Cuerpo
Se logra que los segmentos del cuerpo sigan a la cabeza de manera sincronizada. Esto se hace recorriendo la lista de segmentos de atrás hacia adelante y actualizando su posición con respecto al anterior.

➤ Reinicio por Colisión
- Si la cabeza choca con el borde (borde()), el juego se reinicia: la serpiente se reinicia en el centro, se borran los segmentos, y el puntaje vuelve a cero.
- Si la serpiente choca consigo misma (mordida()), se activa la misma lógica.

Bucle Principal del Juego
El juego se ejecuta dentro de un while True que:
- Actualiza la pantalla cada iteración
- Evalúa colisiones con comida, bordes y el cuerpo
- Ejecuta el movimiento de la serpiente y su cuerpo
- Controla la velocidad mediante time.sleep(posponer)

 Aspectos de Diseño y Personalización
- Colores pastel en el cuerpo de la serpiente hacen el juego más visualmente agradable.
- Textos claros para el puntaje, con fuente legible y bien posicionada.
- Animación fluida gracias al uso eficiente de update() y tracer(0).
- Interfaz minimalista, centrada en la jugabilidad.

 Conclusiones
El desarrollo de este juego permitió aplicar múltiples conceptos de programación como listas, ciclos, eventos, funciones, manipulación de coordenadas y estructuras gráficas. Además, fomentó la creatividad mediante el diseño estético del juego.
Esta experiencia me ayudó a comprender la importancia de la lógica estructurada, la interacción con el usuario y cómo construir una interfaz visual simple pero efectiva. El juego puede servir como base para futuros desarrollos más complejos, como agregar niveles, sonidos o incluso integrar un sistema de logros.

