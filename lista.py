def __criterio(dato, criterio):
    if(criterio is None):
        return dato
    else:
        return dato[criterio]

def quicksort(vector, inicio, fin, criterio):
    primero = inicio
    ultimo = fin -1
    pivote = fin
    while(primero < ultimo):
        while(__criterio(vector[primero], criterio) <= __criterio(vector[pivote], criterio) and primero <= ultimo):
            primero += 1
        while(__criterio(vector[ultimo], criterio) > __criterio(vector[pivote], criterio) and ultimo >= primero):
            ultimo -= 1
        if(primero < ultimo):
            vector[primero], vector[ultimo] = vector[ultimo], vector[primero]
    if(__criterio(vector[pivote], criterio) < __criterio(vector[primero], criterio)):
        vector[primero], vector[pivote] = vector[pivote], vector[primero]

    if(inicio < primero):
        quicksort(vector, inicio, primero -1, criterio)
    if(fin > primero):
        quicksort(vector, primero + 1, fin, criterio)

class Lista(object):
    """crea un objeto de tipo lista"""

    def __init__(self):
        self.__elementos = []
    
    def __criterio(self, dato, criterio):
        if(criterio == None):
            return dato
        else:
            return dato[criterio]

    def insertar(self, dato, criterio= None): #! tener en cuenta que la insercion es ordenada
        if(len(self.__elementos) == 0):
            self.__elementos.append(dato)
        elif(self.__criterio(dato, criterio) < self.__criterio(self.__elementos[0], criterio)):
            self.__elementos.insert(0, dato)
        else:
            pos = 0
            while(pos < len(self.__elementos) and self.__criterio(dato, criterio)>=self.__criterio(self.__elementos[pos], criterio)):
                pos +=1 
            self.__elementos.insert(pos, dato) 


    def eliminar(self, dato, criterio=None, clave=None, criterio_clave=None):
        pos = self.busqueda(dato, criterio, clave, criterio_clave)
        if(pos != -1):
            return self.__elementos.pop(pos)
        else:
            return None


    def modificar_elemento(self, pos, nuevo_valor, criterio=None):
        self.__elementos.pop(pos)
        self.insertar(nuevo_valor, criterio)

    def busqueda(self, buscado, criterio=None, clave=None, criterio_clave=None):
        pos = -1
        primero = 0
        ultimo = len(self.__elementos) -1
        while(primero <= ultimo and pos == -1):
            medio = (primero + ultimo) // 2
            if(self.__criterio(self.__elementos[medio], criterio) == buscado):
                pos = medio
            elif(self.__criterio(self.__elementos[medio], criterio) > buscado):
                ultimo = medio -1
            else:
                primero = medio + 1

        if(pos != -1 and clave is not None and self.__elementos[pos][criterio_clave] != clave):
            while(self.__criterio(self.__elementos[pos], criterio) == self.__criterio(self.__elementos[pos-1], criterio)):
                pos -= 1
            
            while(self.__elementos[pos][criterio_clave] != clave and 
                self.__criterio(self.__elementos[pos], criterio) == self.__criterio(self.__elementos[pos+1], criterio)):
                pos += 1
            
            if(self.__elementos[pos][criterio_clave] != clave):
                pos = -1

        return pos

        # [1, 2, 3, 4, 4, 4, 5, 6,7]
    
    def obtener_elemento(self, pos):
        if(pos >= 0 ):
            return self.__elementos[pos]
        else:
            return None

    def lista_vacia(self):
        return len(self.__elementos) == 0
    
    def tamanio(self):
        return len(self.__elementos)

    def barrido(self):
        for elemento in self.__elementos:
            print(elemento)
    
    def barrido_inicial(self):
            for elemento in self.__elementos:
                if (elemento[0]=='C' or elemento[0]=='S'):
                    print(elemento)
    
    def barrido_jedi(self):
        for elemento in self.__elementos:
            print(elemento['name'], elemento['species'])
    
    def barrido_green(self):
        for elemento in self.__elementos:
            if('green' in elemento['lightsaber_color']):
                print(elemento['name'])
    def barrido_palabra(self):
        for elemento in self.__elementos:
            if(('traje' in elemento['Biografia']) or ('armadura' in elemento['Biografia'])):
                print(elemento['name'])

    def barrido_valor(self):
        for elemento in self.__elementos:
            if((elemento['a??o_aparicion'] <= 1963)):
                print(elemento['name'])
    
    def barrido_lista_autos(self):
        for elemento in self.__elementos:
            print(elemento)
            print('autos:')
            elemento['autos'].barrido()

    # def barrido(self):
    #     for elemento in self.__elementos:
    #         for valor in elemento.values():
    #             print(valor)
        
    def barrido_eliminando(self, datos_eliminar):

        for elemento in self.__elementos:
            if(elemento in datos_eliminar):
                self.__elementos.remove(elemento)
    
    def ordenar(self, criterio):
        quicksort(self.__elementos, 0, len(self.__elementos)-1, criterio)

from lista import Lista

personajes = ['Dr. Stephen','Mesera','Thor','Scalet Witch',]
lista_personas = Lista()

for nombres in personajes:
    lista_personas.insertar(personajes)
lista_personas.barrido()


