import turtle                           #La libreria turtle ayuda a construir la interfaz gráfica
import time                             #Para obtenier el tiempo
import random                           #Para usar numeros random

posponer = 0.1
puntaje = 0
maxPuntaje = 0

#Configuración
window = turtle.Screen()                #Crea una ventana nueva
window.title('Juego de la serpiente')                   #Ponemos titulo
window.bgcolor("#040404")               #Color de fondo
window.setup(width=600,height=600)      #Redimensionar pantalla
window.tracer(0)                        #Ayuda a hacer la animación 

#Cabeza de la serpiente
cabeza = turtle.Turtle()                #Crea un objeto para mostrar en pantalla
cabeza.speed(0)                         #Se muestra al inciar
cabeza.shape('circle')                  #Se le asigna forma de cuadrado, por defecto es 20x20 pixeles
cabeza.color("#FA159E")                 #Color a la cabeza
cabeza.penup()                          #Elimina el rastro del objeto
cabeza.goto(0,0)                        #Centra el objeto
cabeza.direction = 'stop'               #Asigna direccion, en este caso estatico

#Comida
comida = turtle.Turtle()
comida.speed(0)
comida.shape('circle')
comida.color('#D12D2D')
comida.penup()
comida.goto(0,100)

#Texto para el puntaje
texto = turtle.Turtle()
texto.speed(0)
texto.color('white')
texto.penup()
texto.hideturtle()
texto.goto(0,260)
texto.write('Puntaje:0     Máximo puntaje: 0', align='center', font=('Courier', 20, 'normal'))

#Cuerpo de la serpiende
cuerpo = []  # Lista que almacena cada segmento de la serpiente
colores = [
    (255, 209, 220),  # Rosa pastel
    (167, 199, 231),  # Azul pastel
    (178, 224, 178),  # Verde pastel
    (249, 228, 183),  # Amarillo pastel
    (186, 145, 227),  # Lila pastel
    (175, 238, 238),  # Turquesa pastel
    (255, 218, 185),  # Melocotón pastel
    (230, 230, 250),  # Lavanda pastel
    (152, 255, 152),  # Menta pastel
    (245, 245, 220)   # Beige pastel
]