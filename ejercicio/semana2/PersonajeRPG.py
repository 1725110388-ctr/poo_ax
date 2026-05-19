class PersonajeRPG:
    def __init__(self,altura,edad,sexo,no_extremidades,nombre,especialidad,
                 raza,tipo_magia,cantidad_magia,tipo_arma):
        self.altura=altura
        self.edad=edad
        self.sexo=sexo
        self.no_extremidades=no_extremidades
        self.nombre=nombre
        self.especialidad=especialidad
        self.raza=raza
        self.tipo_magia=tipo_magia
        self.cantidad_magia=cantidad_magia
        self.tipo_arma=tipo_arma
        print(f"altura del personaje {self.altura}")
        print(f"edad del personaje {self.edad}")
        print(f"sexo del personaje {self.sexo}")
        print(f"extremidades que tiene el personaje {self.no_extremidades}")
        print(f"nombre del personaje {self.nombre}")
        print(f"en que se especializa el personaje {self.especialidad}")
        print(f"la raza del persomaje {self.raza}")
        print(f"el tipo de magia del personaje {self.tipo_magia}")
        print(f"cantidad de magia que posee {self.cantidad_magia}")
        print(f"que arma maneja {self.tipo_arma}")
artur=PersonajeRPG("230 cm","23 años","masculino",3,"Artur","Tanque","ogro","Ataque","media","escudo gigante")