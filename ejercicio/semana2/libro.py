class Libro:
    def __init__(self,titulo, autor, portada, contraporada, indice,no_paginas, genero_literario, 
                 editorial, año_publicado, idioma):
        self.titulo=titulo
        self.autor=autor
        self.portada=portada
        self.contraporada=contraporada
        self.indice=indice
        self.no_paginas=no_paginas
        self.genero_literario=genero_literario
        self.editorial=editorial
        self.año_publicado=año_publicado
        self.idioma=idioma
        print(f"titulo {self.titulo}")
        print(f"autor {self.autor}")
        print(f"portada {self.portada}")
        print(f"contraporada {self.contraporada}")
        print(f"indice {self.indice}")
        print(f"no_paginas {self.no_paginas}")
        print(f"genero_literario {self.genero_literario}")
        print(f"editorial {self.editorial}")
        print(f"año_publicado {self.año_publicado}")
        print(f"idioma {self.idioma}")
caperusita=Libro("Caperucita Roja", "Charles Perrault", True, True, False, 30, "cuentos infatiles", "Editorial Océano", 2000, "español")