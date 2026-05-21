class Alumno:
    def __init__(self,nombre,matricula,edad,altura,peso,localidad
                 ,promedio,uniforme,nivel_academico):
        self.nombre=nombre
        self.matricula=matricula
        self.edad=edad
        self.altura=altura
        self.peso=peso
        self.localidad=localidad
        self.promedio=promedio
        self.uniforme=uniforme
        self.nivel_academico=nivel_academico
        print(f"nombre del alumno {self.nombre}")
        print(f"matricula {self.matricula}")
        print(f"edad {self.edad}")
        print(f"altura {self.altura}")
        print(f"peso {self.peso}")
        print(f"localidad {self.localidad}")
        print(f"promedio {self.promedio}")
        print(f"uniforme {self.uniforme}")
        print(f"nivel academico {self.nivel_academico}")
axel=Alumno("axel",1725110388,19,"160cm","80kg","tulancingo",8.0,True,"promedio")