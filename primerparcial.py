#EJERCICIO1
#from recursividad import quicksort

Personajes = ['Leia','Yoda','Luke','Obi','Conde','Mace']



for nombre in Personajes:
        print (nombre) 
    

def Busqueda(Personajes, pos):
    if(pos<len(Personajes)):
        if(Personajes[pos]=='Yoda'):
            return pos
        else:
            return Busqueda(Personajes, pos+1)
    else:
        return -1

print('Yoda esta en el vector en la posicion:',Busqueda(Personajes, 0))
    


#EJERCICIO2
from cola import Cola
from pila import Pila

#cola_notificacion = Cola()

class Notificacion(object):
    
    
    def __init__(self,hora,aplicacion,mensaje):
        self.hora = hora
        self.aplicacion = aplicacion
        self.mensaje = mensaje
        


    def __str__(self):
            return str(self.hora) +'-'+ str(self.aplicacion)+ '-'+str(self.mensaje)

cola_notificacion =Cola()

notif= Notificacion(12,'Twitter','hola')
cola_notificacion.arribo(notif)
notif= Notificacion(8,'Facebook','Tienes una notificacion del curso de Python')
cola_notificacion.arribo(notif)
notif= Notificacion(12,'Facebook','hola')
cola_notificacion.arribo(notif)
notif= Notificacion(3,'Instagram','hola')
cola_notificacion.arribo(notif)
notif= Notificacion(14,'Twitter','hola python')
cola_notificacion.arribo(notif)

pila_notificacion = Pila()
#ejercicio c
cant_elementos = 0
while(cant_elementos < cola_notificacion.tamanio()):
    dato = cola_notificacion.mover_final()
    print(dato)
    cant_elementos +=1
    if (dato.aplicacion == 'Facebook'):
        cola_notificacion.atencion()
        #ejercicio d
    if (dato.aplicacion == 'Twitter' and dato.mensaje =='python'):
        print('Notificaciones de Twitter, cuyo mensaje contiene la palabra Pyhton:',cola_notificacion.atencion())
    #ejercicio e
    if (dato.aplicacion =='Instagram'):
        pila_notificacion.apilar(dato)

while (not pila_notificacion.pila_vacia()):
    datos= pila_notificacion.desapilar()
    print('Notificaciones de instagram:',datos)



#EJERCICIO 3
from lista import Lista

Personajes = ['Chica','Dr. Stephen','Mesera','Thor','Extra','Scalet Witch']
Personajes_aux = ['Black Widow','Hulk','Rocket Racoonn','Loki']

lista_personajes = Lista()


for nombre in Personajes:
    lista_personajes.insertar(nombre)

lista_personajes.barrido()
#ejercicio 3-a
pos = lista_personajes.busqueda('Thor')
if(pos!= -1):
        print(lista_personajes.obtener_elemento(pos),'esta en la lista')
else:
    print('Thor no esta en la lista')
#ejercicio 3-b
pos= lista_personajes.busqueda('Scalet Witch')
lista_personajes.modificar_elemento(pos,'Scarlet Witch')

lista_personajes.barrido()

#ejercicio 3-c

for nombre in Personajes_aux:
    lista_personajes.insertar(nombre)


lista_personajes.barrido()

#ejercicio d

#print('orden ascendente',lista_personajes.barrido()) #orden ascendente
for i in range(lista_personajes.tamanio()-1):#orden descendenete
    print('orden descendente',lista_personajes.obtener_elemento(i))

#ejercicio e

print('elemento de la posicion numero 7',lista_personajes.obtener_elemento(7))


#ejercicio f
print ('Personajes que comienzan con C o S',lista_personajes.barrido_inicial())#funcion creada en TDA LISTA



#ejercicio g 
Personajes2 = [
{'name':'Black Widow','año_aparicion':1986, 'heroe' : 'True'},
{'name':'Chica','año_aparicion':1640, 'heroe' : 'True'},
{'name':'Dr. Stephen','año_aparicion':1900, 'heroe' : 'False'},
{'name':'Extra','año_aparicion':1900, 'heroe' : 'True'},
{'name':'Hulk','año_aparicion':1850, 'heroe' : 'True'},
{'name':'Loki','año_aparicion':1785, 'heroe' : 'False'},
{'name':'Mesera','año_aparicion':1842, 'heroe' : 'True'},
{'name':'Rocket Raconn','año_aparicion':1562, 'heroe' : 'False'},
{'name':'Scarlet Witch','año_aparicion':1244, 'heroe' : 'True'}
]

lista_personajes2= Lista()
for personaje in Personajes2:
    lista_personajes2.insertar(personaje,'name')

lista_personajes.barrido()

for personaje in Personajes2:
    lista_personajes2.insertar(personaje,'año_aparicion')

lista_personajes.barrido()




