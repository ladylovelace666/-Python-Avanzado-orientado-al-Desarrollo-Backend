""" 
Definir una clase padre llamada Vehiculo y dos clases hijas llamadas Coche y Bicicleta, 
las cuales heredan de la clase Padre Vehiculo. 
La clase padre debe tener los siguientes atributos y métodos 
 
Vehiculo (Clase Padre): -Atributos (color, ruedas) -Métodos ( __init__() y __str__ ) 
 
Coche  (Clase Hija de Vehículo) (Además de los atributos y métodos heredados de 
Vehículo): -Atributos ( velocidad (km/hr) ) -Métodos ( __init__() y __str__() ) 
 
Bicicleta  (Clase Hija de Vehículo) (Además de los atributos y métodos heredados de 
Vehículo): -Atributos ( tipo (urbana/montaña/etc ) -Métodos ( __init__() y __str__() ) 
"""
#Ejercicio 1: Vehiculo Padre, Coche y Bicicleta Hijas
class Vehiculo():
    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas
    def __str__(self):
       # return f"El vehiculo es de color {self.color} y tiene {self.ruedas} ruedas"
        return 'Color:' + self.color +', Ruedas:' +str(self.ruedas)
class Coche(Vehiculo):
    def __init__(self,color,ruedas,velocidad):
        super().__init__(color,ruedas)
        self.velocidad = velocidad 
    def __str__(self):
        return super().__str__() + ', Velocidad (km/h):' + str(self.velocidad)
        #return f"El coche es de color {self.color}, tiene {self.ruedas} ruedas y una velocidad de {self.velocidad} km/hr"
class Bicicleta(Vehiculo):
    def __init__(self, color, ruedas, tipo):
        super().__init__(color,ruedas)
        self.tipo = tipo
    def __str__(self):
        return super().__str__() + ', Tipo:' + self.tipo
        #return f"La bicicleta es de color {self.color}, tiene {self.ruedas} ruedas y es de tipo {self.tipo}"
    
print(Vehiculo("rojo", 4))
print(Coche("azul", 6, 120))
print(Bicicleta("verde", 2, "urbana"))


#Ejercicio 2 
'''La clase empleado contiene los datos que serán 
compartidos por sus clases hijas. La clase empleado 
contiene un constructor para inicializar sus atributos 
Los datos utilizados son: nombre completo, cedula y 
teléfono. Cada atributo de la clase cuenta con sus 
respectivos get y set.'''

class Empleado():
    def __init__(self, nombre, cedula, telefono):
        self._nombre = nombre
        self._cedula = cedula
        self._telefono = telefono 
    
    def set_nombre(self, nombre):
        self._nombre = nombre
    
    def get_nombre(self):
        return self._nombre
    
    def set_cedula(self, cedula):
        self._cedula = cedula
    
    def get_cedula(self):
        return self._cedula
    
    def set_telefono(self, telefono):
        self._telefono = telefono

    def get_telefono(self):
        return self._telefono
    

'''Clase de empleado por tiempo definido 
Esta clase hereda de la clase empleado. Los nuevos 
atributos son: 
• Número de plaza 
• Salario base 
• Duración de contrato en meses 
Además, cuenta con un método que calcula el salario 
total El empleado recibe un aumento del 2% sobre su  
salario base.'''

class EmpleadoDefinido(Empleado):
    def __init__(self, nombre, cedula, telefono, num_plaza, salario_base, duracion_contrato):
        super().__init__(nombre,cedula, telefono)
        self._num_plaza = num_plaza
        self._salario_base = salario_base
        self._duracion_contrato = duracion_contrato
    def set_num_plaza(self, num_plaza):
        self._num_plaza = num_plaza
    def get_num_plaza(self):
        return self._num_plaza
    def set_salario_base(self, salario_base):
        self._salario_base = salario_base
    def get_salario_base(self):
        return self._salario_base
    def set_duracion_contrato(self, duracion_contrato):
        self._duracion_contrato = duracion_contrato
    def get_duracion_contrato(self):
        return self._duracion_contrato
    
    def cacular_salario_total(self):
        return self._salario_base + (self._salario_base * 0.02)
    
'''Clase de empleado por tiempo 
indefinido 
Esta clase hereda de la clase empleado. Los nuevos 
atributos son: 
• Número de plaza 
• Salario base 
• Categoría (1, 2, 3) 
Además, cuenta con un método que calcula el salario 
total Los empleados recieb un aumento de acuerdo a 
su categoría: 
• Categoría 1: 3% 
• Categoría 2: 5% 
• Categoría 3: 8% '''

class  EmpleadoIndefinido (Empleado):
    def __init__(self, nombre,cedula, telefono, num_plaza,salario_base, categoria):
        super().__init__(nombre, cedula,telefono)

        self._num_plaza = num_plaza
        self._salario_base = salario_base
        self._categoria = categoria
    
    def set_num_plaza(self, num_plaza):
        self._num_plaza = num_plaza
    
    def get_num_plaza(self):
        return self._num_plaza
    
    def set_salario_base(self, salario_base):
        self._salario_base = salario_base
    def get_salario_base(self):
        return self._salario_base
    def set_categoria(self, categoria):
        self._categoria = categoria
    def get_categoria(self):
        return self._categoria
    

    def calcular_salario_total(self):
        if self._categoria ==1:
            return self._salario_base + (self._salario_base * 0.03)
        elif self._categoria == 2:
            return self._salario_base + (self._salario_base * 0.05)
        elif self._categoria == 3:
            return self._salario_base + (self._salario_base * 0.08)
        else:
            return self._salario_base
        

    