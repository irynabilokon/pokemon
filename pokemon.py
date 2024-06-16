import random

class Pokemon:
    def __init__(self, nombre, tipo, vida):
        self.nombre = nombre
        self.tipo = tipo
        self.vida = vida
        self.ataques = {'arañazo': 5}

    def atacar(self, oponente):
        ataque = random.choice(list(self.ataques.keys()))
        print(f"{self.nombre} ataca a {oponente.nombre} con {ataque}")
        oponente.recibir_ataque(self, ataque)

    def recibir_ataque(self, atacante, ataque):
        dano = atacante.ataques[ataque]
        print(f"{self.nombre} recibe {ataque} de {atacante.nombre} causando {dano} puntos de daño")
        self.vida -= dano

    def defenderse(self):
        print(f"{self.nombre}")

    def estado_actual(self):
        print(f"- Puntos de vida de {self.nombre}: {self.vida}")

    def mostrar_ataques(self):
        print(f"Ataques de {self.nombre}: {', '.join(self.ataques.keys())}")


class Agua(Pokemon):
    def __init__(self, nombre, vida=100):
        super().__init__(nombre, "Agua", vida)
        self.ataques['pistola agua'] = 10

    def atacar(self, oponente):
        ataque = random.choice(list(self.ataques.keys()))
        print(f"{self.nombre} ataca a {oponente.nombre} con {ataque}")
        oponente.recibir_ataque(self, ataque)

    def recibir_ataque(self, atacante, ataque):
        dano = atacante.ataques[ataque]
        if atacante.tipo == "Planta":
            self.vida -= 2 * dano
        elif atacante.tipo == "Fuego":
            self.vida -= dano / 2
        else:
            self.vida -= dano
        if atacante.tipo == "Fuego":
            self.defenderse()

    def defenderse(self):
        print(f"{self.nombre} despliega un escudo de agua para defenderse.")


class Fuego(Pokemon):
    def __init__(self, nombre, vida=100):
        super().__init__(nombre, "Fuego", vida)
        self.ataques['lanzallamas'] = 10 

    def atacar(self, oponente):
        ataque = random.choice(list(self.ataques.keys()))
        print(f"{self.nombre} ataca a {oponente.nombre} con {ataque}")
        oponente.recibir_ataque(self, ataque)

    def recibir_ataque(self, atacante, ataque):
        dano = atacante.ataques[ataque]
        if atacante.tipo == "Agua":
            self.vida -= 2 * dano
        elif atacante.tipo == "Planta":
            self.vida -= dano / 2
        else:
            self.vida -= dano
        if atacante.tipo == "Planta":
            self.defenderse()

    def defenderse(self):
        print(f"{self.nombre} crea una barrera de fuego para resistir el ataque.")

class Planta(Pokemon):
    def __init__(self, nombre, vida=100):
        super().__init__(nombre, "Planta", vida)
        self.ataques['látigo cepa'] = 10

    def atacar(self, oponente):
        ataque = random.choice(list(self.ataques.keys()))
        print(f"{self.nombre} ataca a {oponente.nombre} con {ataque}")
        oponente.recibir_ataque(self, ataque)

    def recibir_ataque(self, atacante, ataque):
        dano = atacante.ataques[ataque]
        if atacante.tipo == "Fuego":
            self.vida -= 2 * dano
        elif atacante.tipo == "Agua":
            self.vida -= dano / 2
        else:
            self.vida -= dano
        if atacante.tipo == "Agua":
            self.defenderse()

    def defenderse(self):
        print(f"{self.nombre} se camufla entre las hojas para evitar el ataque.")


squirtle = Agua("Squirtle", 100)
totodile = Agua("Totodile", 100)
mudkip = Agua("Mudkip", 100)
charmander = Fuego("Charmander", 100)
cyndaquil = Fuego("Cyndaquil", 100)
torchic = Fuego("Torchic", 100)
bulbasaur = Planta("Bulbasaur", 100)
chikorita = Planta("Chikorita", 100)
treecko = Planta("Treecko", 100)

pokemones = [squirtle, totodile, mudkip, charmander, cyndaquil, torchic, bulbasaur, chikorita, treecko]

for pokemon in pokemones:
    pokemon.mostrar_ataques()

print("\nEstado actual de los Pokémon:")
for pokemon in pokemones:
    pokemon.estado_actual()
print("\n")

for pokemon in pokemones:
    for oponente in pokemones:
        if pokemon != oponente:
            for _ in range(1):
                pokemon.atacar(oponente)

print("\nEstado actual de los Pokémon:")
for pokemon in pokemones:
    pokemon.estado_actual()
