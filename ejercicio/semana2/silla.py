class Silla:
    def __init__(self,No_patas,Altura,Peso,material,tamaño,
                 ergonomia,portabilidad,diseño,color,reclinable):
        self.No_patas=No_patas
        self.Altura=Altura
        self.Peso=Peso
        self.material=material
        self.tamaño=tamaño
        self.ergonomia=ergonomia
        self.portabilidad=portabilidad
        self.diseño=diseño
        self.color=color
        self.reclinable=reclinable
        print(f"Numero de patas {self.No_patas}")
        print(f"Altura del perro {self.Altura}")
        print(f"Peso que tiene el perro {self.Peso}")
        print(f"tipo de material {self.material}")
        print(f"Tamaño {self.tamaño}")
        print(f"ergonomia {self.ergonomia}")
        print(f"portabilidad {self.portabilidad}")
        print(f"Tipo de diseño {self.diseño}")
        print(f"color {self.color}")
        print(f"tiene reclinable {self.reclinable}")
plastico=Silla(4, "40cm", "5kg", "plastico", "100cm", true, true, "robusto", "negro", true)