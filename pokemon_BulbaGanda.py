class Pokemon:
    def __init__(self, nombre, tipo, vida):
        self.nombre = nombre
        self.tipo = tipo
        self.vida = vida
        self.ataques = ["arañazo"]

    def atacar(self, oponente):
        ataque = self.ataques[0]
        print(f"{self.nombre} ataca a {oponente.nombre} con {ataque}")
        oponente.recibir_ataque(self, ataque)

    def recibir_ataque(self, atacante, ataque):
        print(f"{self.nombre} recibe {ataque} de {atacante.nombre}")

    def defenderse(self):
        print(f"{self.nombre} se está defendiendo.")

    def estado_actual(self):
        print(f"{self.nombre} - Vida: {self.vida}")

    def mostrar_ataques(self):
        print(f"Ataques de {self.nombre}: {', '.join(self.ataques)}")

class Agua(Pokemon):
    def __init__(self, nombre, vida=100):
        super().__init__(nombre, "Agua", vida)
        self.ataques.append("pistola agua")

    def atacar(self, oponente):
        ataque = self.ataques[1]
        print(f"{self.nombre} ataca a {oponente.nombre} con {ataque}.")
        oponente.recibir_ataque(self, ataque)

    def recibir_ataque(self, atacante, ataque):
        if atacante.tipo in ["Planta", "Planta2", "Planta3"]:
            multiplicador = 2 if atacante.tipo == "Planta" else 3 if atacante.tipo == "Planta3" else 2.5
            self.vida -= 10 * multiplicador
        elif atacante.tipo == "Fuego":
            self.vida -= 10 / 2
        else:
            self.vida -= 10
        if atacante.tipo == "Fuego":
            self.defenderse()

    def defenderse(self):
        print(f"{self.nombre} despliega un escudo de agua para defenderse.")

class Fuego(Pokemon):
    def __init__(self, nombre, vida=100):
        super().__init__(nombre, "Fuego", vida)
        self.ataques.append("lanzallamas")

    def atacar(self, oponente):
        ataque = self.ataques[1]
        print(f"{self.nombre} ataca a {oponente.nombre} con {ataque}.")
        oponente.recibir_ataque(self, ataque)

    def recibir_ataque(self, atacante, ataque):
        if atacante.tipo == "Agua":
            self.vida -= 2 * 10
        elif atacante.tipo in ["Planta", "Planta2", "Planta3"]:
            multiplicador = 0.5 if atacante.tipo == "Planta" else 0.5 if atacante.tipo == "Planta2" else 0.67
            self.vida -= 10 * multiplicador
        else:
            self.vida -= 10
        if atacante.tipo == "Planta" or atacante.tipo == "Planta2" or atacante.tipo == "Planta3":
            self.defenderse()

    def defenderse(self):
        print(f"{self.nombre} crea una barrera de fuego para resistir el ataque.")

class Planta(Pokemon):
    def __init__(self, nombre, vida=100):
        super().__init__(nombre, "Planta", vida)
        self.ataques.append("látigo cepa")

    def atacar(self, oponente):
        ataque = self.ataques[1]
        if oponente.tipo == "Fuego" or oponente.tipo == "Agua":
            print(f"{self.nombre} ataca a {oponente.nombre} con {ataque}.")
            oponente.recibir_ataque(self, ataque)
        else:
            print(f"{oponente.nombre} recibe efecto positivo \"BulbaGanda\" de {self.nombre}")
            oponente.recibir_ataque(self, ataque)

    def recibir_ataque(self, atacante, ataque):
        if atacante.tipo == "Fuego":
            self.vida -= 2 * 10
        elif atacante.tipo == "Agua":
            self.vida -= 10 / 2
        else:
            self.vida += 10
            print(f"¡{self.nombre} recupera 10 puntos de vida, por el efecto de Bulbaganda!")
        if atacante.tipo == "Agua":
            self.defenderse()

    def defenderse(self):
        print(f"{self.nombre} se camufla entre las hojas para evitar el ataque.")

class Planta2(Pokemon):
    def __init__(self, nombre, vida=150):
        super().__init__(nombre, "Planta2", vida)
        self.ataques.append("hoja afilada")

    def atacar(self, oponente):
        ataque = self.ataques[1]
        if oponente.tipo == "Fuego" or oponente.tipo == "Agua":
            print(f"{self.nombre} ataca a {oponente.nombre} con {ataque}.")
            oponente.recibir_ataque(self, ataque)
        else:
            print(f"{oponente.nombre} recibe efecto positivo \"BulbaGanda\" de {self.nombre}")
            oponente.recibir_ataque(self, ataque)

    def recibir_ataque(self, atacante, ataque):
        if atacante.tipo == "Fuego":
            self.vida -= 1.5 * 10
        elif atacante.tipo == "Agua":
            self.vida -= 10 / 1.5
        else:
            self.vida += 10
            print(f"¡{self.nombre} recupera 10 puntos de vida, por el efecto de Bulbaganda!")
        if atacante.tipo == "Agua":
            self.defenderse()

    def defenderse(self):
        print(f"{self.nombre} genera una ráfaga de hojas para bloquear el ataque.")

class Planta3(Pokemon):
    def __init__(self, nombre, vida=200):
        super().__init__(nombre, "Planta3", vida)
        self.ataques.append("hoja mágica")

    def atacar(self, oponente):
        ataque = self.ataques[1]
        if oponente.tipo == "Fuego" or oponente.tipo == "Agua":
            print(f"{self.nombre} ataca a {oponente.nombre} con {ataque}.")
            oponente.recibir_ataque(self, ataque)
        else:
            print(f"{oponente.nombre} recibe efecto positivo \"BulbaGanda\" de {self.nombre}")
            oponente.recibir_ataque(self, ataque)

    def recibir_ataque(self, atacante, ataque):
        if atacante.tipo == "Fuego":
            self.vida -= 1.2 * 10
        elif atacante.tipo == "Agua":
            self.vida -= 10 / 1.2
        else:
            self.vida += 10
            print(f"¡{self.nombre} recupera 10 puntos de vida, por el efecto de Bulbaganda!")
        if atacante.tipo == "Agua":
            self.defenderse()

    def defenderse(self):
        print(f"{self.nombre} se enraíza en el suelo para resistir el ataque.")



squirtle = Agua("Squirtle", 100)
totodile = Agua("Totodile", 100)
mudkip = Agua("Mudkip", 100)
charmander = Fuego("Charmander", 100)
cyndaquil = Fuego("Cyndaquil", 100)
torchic = Fuego("Torchic", 100)
bulbasaur = Planta("Bulbasaur", 100)
ivysaur = Planta2("Ivysaur", 150)
venusaur = Planta3("Venusaur", 200)


pokemones = [squirtle, totodile, mudkip, charmander, cyndaquil, torchic, bulbasaur, ivysaur, venusaur]



for pokemon in pokemones:
    pokemon.mostrar_ataques()


print("\nEstado actual de los Pokémon:")
for pokemon in pokemones:
    pokemon.estado_actual()
print("\n")
for pokemon in pokemones:
    for oponente in pokemones:
        if pokemon != oponente:
            pokemon.atacar(oponente)

print("\nEstado actual de los Pokémon:")
for pokemon in pokemones:
    if pokemon.vida > 0:
        pokemon.estado_actual()
    else:
        print(f"{pokemon.nombre}: RIP")
