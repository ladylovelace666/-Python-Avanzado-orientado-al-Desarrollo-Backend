'''
#CREACIÓN DE CLASE
class Coche ():
#declaración atributos 
    largo = 250
    ancho = 120
    color = "rojo"
    ruedas  = 4 
    peso= 900
    is_enMarcha = False
    
    #declaracion de métodos 
    def arrancar (self):
        #self hacer refencia a la instancia de clase
        self.is_enMarcha = True 
        #es como si pusieramos mi coche is.enMarcha = True 
    def estado (self):
        if ( self.is_enMarcha == True):
            return "El coche está arrancado"
        else:
            return "El coche está parado"
            #declaración de una instacia de clase, objeto de clase o ejemplar de calse

#acceso a un atributo de la clase coche. Nomenclatura del punto
miCoche = Coche()
miCoche2= Coche()
print("El largo del coche es de ", miCoche.largo, "cm")    
miCoche.arrancar()
print(miCoche.estado())

#Acceso a un método del la clase Coche. Nomenclatura del punto
print("El coche está arrancando:", miCoche.arrancar())

#Modificamos el valor de una propiedad 
miCoche2.ruedas = 10
print("El número de ruedas del coche es: ", miCoche2.ruedas)

#CREACIÓN DE CLASE USUARIO 
class Usuario ():
    nombre = "Juan"
    apellido = "Perez"
    edad = 30
    login = "administrador"
    password = "1234"
    email = "juan.perez@example.com"
    telefono = "666666666"

    def resumen(self):
        #self hace refencia a la instancia de clase
        print(f'Los datos del usuario son:\n'
            f'Nombre: {self.nombre}\n'
            f'Apellido: {self.apellido}\n'
            f'Edad: {self.edad}\n'
            f'Login: {self.login}\n'
            f'Email: {self.email}\n'
            f'Telefono: {self.telefono}')
    def cambiaEdad(self):
        edadIntroducida = int(input("Introduce edad entre 18-100:"))
        if 18 <= edadIntroducida <= 100:
            self.edad = edadIntroducida
            print(f'La edad del usuario ha sido actualizada a: {self.edad}')
        else:
            print("Edad no válida. Por favor, introduce una edad entre 18 y 100.")  
            self.cambiaEdad()  # Llamada recursiva para solicitar una edad válida   
            return ""
    def muestraEdad(self):
        print(f'La edad del usuario es: {self.edad}')   
        return ""
administrador = Usuario()
administrador.resumen()
print (administrador.cambiaEdad())
print (administrador.muestraEdad())

#declaración del método constructor, se ejecuta automáticamente al crear una instancia de clase Coche

def __init__(self):
    self.largo = 250
    self.ancho = 120
    self.color = "rojo"
    self.ruedas  = 4
    self.peso= 900
    self.is_enMarcha = False
#declaracion de métodos
def arrancar(self): #self hace refencia a la instacia de clase/ es como si pusiesemos miCoche.is enMarcha = True
    self.is_enMarcha = True
    def estado(self):
        if self.is_enMarcha == True:
            return "El coche está arrancado"
        else:
            return "El coche está parado"
#declaración de una instacia de clse objeto o ejemplar de clase
coche_1 = Coche()
#acceso a un atributo de la clase Coche. Nomenclatura del punto
print("El largo del coche es de ", coche_1.largo, "cm")
coche_1.arrancar()
print(coche_1.estado())
#acceso a un método de la clase coche. Nomenclatura del punto
print("El coche está arrancando:", coche_1.arrancar())

'''
#declaración del constructor con parámetros
class Coche():

    def __init__(self, largo, ancho, color, ruedas, peso, is_enMarcha):
        self.largo = largo
        self.ancho = ancho
        self.color = color
        self.ruedas  = ruedas
        self.peso= peso
        self.is_enMarcha = is_enMarcha 

coche_1 = Coche(250, 120, "rojo", 4, 900, True)
coche_2 = Coche(300, 150, "azul", 4, 1200, False)

class Book():
    def __init__(self, title, author = "", electronic = False):
        self.title = title
        self.author = author
        self.electronic = electronic
        

    def  __del__(self):
        print("Acabas de llamar al método destructor El objeto ha sido destruido")  
        book = Book("Lazarillo de Toremes")
        print(book.title)
        del book

#herencia de clase/ Se heredan atributos y métodos, incluido el constructor.

class Vehiculo(): 
    def __init__(self, marca, modelo): 
        self.marca = marca 
        self.modelo = modelo 
        self.color = "Negro" 
        self.arrancado = False 
        self.parado = True 
         
    def arrancar(self): 
        self.arrancado = True 
        self.parado = False 
 
    def parar(self): 
        self.parado = True 
        self.arrancado = False 
         
    def resumen(self): 
        print("Marca:", self.marca, "\n", 
              "Modelo:", self.modelo, 
                "\n",
                "Color:", self.color, "\n", 
                "Está arrancado:", 
                self.arrancado,"\n", 
                "Está parado:", self.parado 
                ) 
 
         
miCoche = Vehiculo("Renault", "Megane") 
 
miCoche.arrancar() 
 
miCoche.resumen() 
 
class Moto(Vehiculo): 
    pass 
 
miMoto = Moto("Kawasaki", "Ninja") 
 
miMoto.resumen() 

class Vehiculo(): 
    def __init__(self, marca, modelo): 
        self.marca = marca 
        self.modelo = modelo 
        self.color = "negro" 
        self.arrancado = False 
        self.parado = True
    def arrancar(self): 
        self.arrancado = True 
        self.parado = False 
 
    def parar(self): 
        self.parado = True 
        self.arrancado = False 
         
    def resumen(self): 
        print("El modelo es un coche", 
             "\n", 
             "Marca:", self.marca, "\n", 
             "Modelo:", self.modelo, 
              "\n", 
              "Color:", self.color, "\n", 
              "Está arrancado:", 
             self.arrancado,"\n", 
              "Está parado:", self.parado 
              ) 
  
         
miCoche = Vehiculo("Renault", "Megane") 
 
miCoche.arrancar() 
 
miCoche.resumen() 
 
class Moto(Vehiculo): 
    is_carenado = False 
     
      #Método propio de la clase Moto, no heredado del padre. 
    def poner_carenado(self): 
        self.is_carenado = True 
 
      #La clase Moto sobrescribe el método resumen() heredado del padre 
    def resumen(self): 
        print("El modelo es una moto", 
        "\n", 
            "Marca:", self.marca, "\n", 
            "Modelo:", self.modelo, "\n", 
            "Color:", self.color, "\n", 
            "Está arrancado:", 
            self.arrancado,"\n", 
            "Está parado:", self.parado, 
            "\n", 
            "Tiene carenado:", 
            self.is_carenado   
           ) 
         
miMoto = Moto("Kawasaki", "Ninja") 
 
miMoto.resumen() 
 
class kwad(Moto): 
    pass 
 
miKwad = kwad("Linhai", "LH 500") 
 
miKwad.resumen() 


class B_electrica(Vehiculo, V_electricos):
    pass
def estado(self): 
print("Marca", self.marca,"Modelo", 
self.modelo) 