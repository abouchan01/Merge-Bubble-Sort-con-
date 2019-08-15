from tkinter import *
#Libreria necesaria para usar las interfaces graficas en python.
 
Grafica= Tk()
#Nos vamos a referir como Grafica a la ventana general de tk
Grafica.minsize(380,600)
#El tamaño minimo de grafica será el definido en pixeles (ancho, alto)
Grafica.title("Algoritmos de ordenamiento, practica 1")
#El titulo de Grafica.
Grafica.configure(background="turquoise")
#Configura el fondo de algun color solido, en este caso escogimos turquesa


def CrearCajas():                 ##En el metodo siguiente le pedimos al usuario que ingrese cuantos numeros va a querer ordenar para que vaya poniendolos 
	restante = (numCajas.get())
	i = restante
	if restante < 5 or restante > 20:
		caja = Label(Grafica,text='Solo se pueden ordenar entre 5 y 20 numeros') .grid(row= i+5,column = 0, padx=15, pady=1, sticky = N)
	else:	
		while i >= 1:
				print ("desc0ontando y prueba"+ str(restante))
				numeroDeArr = IntVar()
				lblElemento = Label(Grafica,text = i ) .grid(row= i+5,column = 0, padx= 10, pady=1, sticky = N)
				caja = Entry(Grafica,text='Teclee el numero a ordenar', textvariable = numeroDeArr) .grid(row= i+5,column = 1, padx=15, pady=1, sticky = N)
				texto = Entry(Grafica)
				i -= 1
		pass


arreglo = {}            #Aquí apilaremoso encolaremos los elementos que vaya dando el usuario
bubbleButton = Button(Grafica,text='Bubble Sort') .grid(row=1 , column= 0, ipadx = 35, padx= 40, pady = 15, sticky = NW)
#Pusimos un boton llamado bubbleButton con la leyenda Bubble sort escrito en el, en la primera fila, columna cero, con 40 pixeles de espaciado en el eje x hacia afuera,35 en x hacia adentro , 15 en el eje y, y con tendencia a expandirse hacie el noroeste. 
mergeButton = Button(Grafica, text='Merge Sort') .grid(row=1 , column = 1 ,ipadx = 35,padx= 40 ,pady = 15, sticky= NE)
#Pusimos un boton llamado mergeButton con la leyenda Merge sort escrito en el, en la primera fila, sexta columna, con 50 pixeles de espaciado en el eje x, 15 en el eje y, y con tendencia a expandirse hacie el este. 

lblPregunta = Label(Grafica,text='¿Cuantos números deseas ordenar? (Minimo 5,máximo 20)') .grid(row= 2, padx= 180, pady=20, sticky = N)
numCajas = IntVar()      #tenemos que decirle de que tipo va a ser lo que vamos a escribir dentro para que nos deje obtenerlo

textNum = Entry(Grafica, text= 'número', textvariable=numCajas).grid(row=3,ipadx=30, padx= 70, pady=5, sticky = N)

aceptar = Button(Grafica, text= 'aceptar', command= CrearCajas) .grid(row=4,ipadx=30, padx= 70, pady=5, sticky = N)
#prueba= Label(Grafica, int=numeroTotal) .grid(row= 5, padx= 180, pady=20, sticky = N)
cadenaOrdenada = Label(Grafica, text='El arreglo ordenado es:+""arrOrd""',) .grid(row=5,ipadx=30, padx= 70, pady=5, sticky = N)     #Aqui va el arreglo ordenado






Grafica.mainloop()
#Pusimos el loop para que	la ventana de grafica no se cierre sola







##Bubble sort y merge sort deben definirse como metodos que regresen el array de caracteres ordenados

