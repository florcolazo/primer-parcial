class Cola(object):
    def __init__(self):
        self.__elementos =[]
    
    def arribo(self, dato):
        self.__elementos.append(dato)

    def atencion(self):
        return self.__elementos.pop(0)

    def en_frente(self):
        return self.__elementos[0]

    def mover_final(self):
        dato = self.atencion()
        self.arribo(dato)
        return dato

    def tamanio(self):
        return len(self.__elementos)

    def  cola_vacia(self ):
        return  len ( self.__elementos ) ==  0

    #def arribo_con_prioridad(self,dato,prioridad):

    #def barrido(cola):
        #muestra contenido de una cola sin perder datos
  #barrido
  #cola_aux= Cola()
  #while not cola.cola_vacia():
  #     dato = cola.atencion()
  #     print(dato)
        #coladatos.arribo(dato)
#while not caux.colavacia:
# dato = cola_aux.atencion()
# coladatos.atencion(dato)

