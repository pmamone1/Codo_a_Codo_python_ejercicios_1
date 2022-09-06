
# Clase Persona
class Persona:
    nombre = ''
    edad = ''
    dni = ''
    
    # Definimos un "constructor" para la clase que recibirá el nombre de la persona
    def __init__(self, nombre):
        self.nombre = nombre
    
    #Definimos los "setters"
    def setNombre(self, nombre):
        self.nombre = nombre
 
    def setEdad(self,edad):
        try:
            self.edad = edad
            #print("guardo la edad")
        except ValueError:
            print("El valor no es un numero!")
        
    
    def setDni(self, dni):
        try:
            self.dni = dni
            #print("guardo el dni")
        except ValueError:
            print("El valor no es un numero!")
        
    #Definimos los "getters"
    def getNombre(self):
        return self.nombre
 
    def getEdad(self):
        return self.edad
    
    def getDni(self):
        return self.dni
    
    def mostrar(self):
        print("Datos de la persona:")
        print("Nombre: " + self.nombre)
        print("La edad es " + str(self.edad))
        print('El Dni es: ' + str(self.dni))
    
    def Es_mayor_de_edad(self):
        if self.edad>=18:
            print("La persona es mayor de edad.")
        else:
            print("La persona es menor de edad.")
            
nombre = input("Ingrese un Nombre:")
try:
    edad = int(input("Ingrese la Edad:"))
except:
    edad = int(input("Ingrese la Edad:"))
try:
    dni = int(input("Ingrese DNI:"))
except:
    dni = int(input("Ingrese DNI:"))

persona = Persona(nombre)
persona.setEdad(edad)
persona.setDni(dni)
persona.mostrar()
persona.Es_mayor_de_edad()

class Cuenta(Persona):
    titular = ''
    cantidad = ''
    
    def __init__(self,persona,cantidad=0):
        self.titular = persona
        self.cantidad = cantidad
    
    def setTitular(self):
        try:
            self.titular = Persona.nombre
            print("guardo la edad")
        except ValueError:
            print("Hubo un error en la seleccion del titular!")
    
    def setCantidad(self,cantidad):
        try:
            self.cantidad += float(cantidad)
        except:
            print("Hubo un error en la cantidad!")
    
    def getTitular(self):
        print("El titular es " + self.titular)
    
    def getCantidad(self):
        print("El saldo es "+ str(self.cantidad))
    
    def mostrarCuenta(self):
        print("El titular es "+ self.titular)
        print("El saldo de la cuenta es "+ str(self.cantidad))     

cuenta = Cuenta(persona.nombre,0)
cuenta.mostrarCuenta()

while True:
    print("*******************")
    a = float(input("Ingrese un valor para la cuenta de {} >>> ".format(persona.nombre)))
    if a == "q" or a == "Q":
        exit()
    else:
        cuenta.setCantidad(a) 
        cuenta.mostrarCuenta()
        
    
    
    