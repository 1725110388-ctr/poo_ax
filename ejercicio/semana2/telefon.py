class Telefono:
    def __init__(self, gama, color, tamaño, sistema, compania, ram, capacidad, no_camaras, nombre, no_modelo):
        self.gama=gama
        self.color=color
        self.tamaño=tamaño
        self.sistema=sistema
        self.compania=compania
        self.ram=ram
        self.capacidad=capacidad
        self.no_camaras=no_camaras
        self.nombre=nombre
        self.no_modelo=no_modelo
        print(f"tipo de gama {self.gama}")
        print(f"color {self.color}")
        print(f"tamaño del telefono {self.tamaño}")
        print(f"tipo de sistema operativo {self.sistema}")
        print(f"compania {self.compania}")
        print(f"tamaño de ram {self.ram}")
        print(f"capacidad del telefono {self.capacidad}")
        print(f"numero de camaras {self.no_camaras}")
        print(f"nombre {self.nombre}")
        print(f"numero de modelo {self.no_modelo}")
sansung=Telefono("alta", "verde", "grande", "android", "telcel", "12gb", "256gb", "4", "samsung ultra", "22")