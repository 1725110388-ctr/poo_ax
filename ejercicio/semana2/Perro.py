class Perro:
    def __init__(self,No_patas,Altura,Peso,Raza,T_pelaje,
                 No_orificios,Sexo,T_hosico,Largo_cola):
        self.No_patas=No_patas
        self.Altura=Altura
        self.Peso=Peso
        self.Raza=Raza
        self.T_pelaje=T_pelaje
        self.No_orificios=No_orificios
        self.Sexo=Sexo
        self.T_hosico=T_hosico
        self.Largo_cola=Largo_cola
        print(f"Numero de patas {self.No_patas}")
        print(f"Altura del perro {self.Altura}")
        print(f"Peso que tiene el perro {self.Peso}")
        print(f"Raza del perro {self.Raza}")
        print(f"Tipo de pelaje del perro {self.T_pelaje}")
        print(f"Numero de orificios del perro {self.No_orificios}")
        print(f"Sexo del perro {self.Sexo}")
        print(f"Tipo del hosico del perro {self.T_hosico}")
        print(f"que tan larga es su cola {self.Largo_cola}")
pitbull=Perro(4,"35 cm","65 kg","pitbul","pelaje corto","2 orificios","Masculino","Chato","20 cm")