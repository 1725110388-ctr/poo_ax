class Banco:
    def __init__(self,seguridad,fiabilidad,accesible,tamano,
                 altura,no_trabajadores,no_cuentas,no_puertas,
                 no_sucursales):
        self.seguridad=seguridad
        self.fiabilidad=fiabilidad
        self.accesible=accesible
        self.tamano=tamano
        self.altura=altura
        self.no_trabajadores=no_trabajadores
        self.no_cuentas=no_cuentas
        self.no_puertas=no_puertas
        self.no_sucursales=no_sucursales
        print(f"seguridad del banco {self.seguridad}")
        print(f"qeu tan fiable es {self.fiabilidad}")
        print(f"que tan accesible es el banco {self.accesible}")
        print(f"tamaño del banco {self.tamano}")
        print(f"altura del banco {self.altura}")
        print(f"trabajadores con los que cuenta {self.no_trabajadores}")
        print(f"cuentas que tiene registradas el banco {self.no_cuentas}")
        print(f"puertas con las que cuenta el banco {self.no_puertas}")
        print(f"sucursales con las que cuenta el banco {self.no_sucursales}")
acme=Banco("alta seguridad",True,False,"Grande","6 metros","5 mil trabajadores","50 mil cuentas",
           "150 puertas","13 mil sucursales")