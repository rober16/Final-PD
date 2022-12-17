import random

class Carta:
    def __init__(self, s, v):
        self.simbolo = s
        self.valor = v
    
    def get_valor(self):
        if(self.valor in ['J', 'Q', 'K', 'A']):
            return 10
        return self.valor
    
class Mazo:
    def __init__(self):
        self.mazo = []
        for simbolo in ['♠', '♣', '♥', '♦']:
            for valor in range(2, 11):
                self.mazo.append(Carta(simbolo, valor))
            for valor in ['J', 'Q', 'K', 'A']:
                self.mazo.append(Carta(simbolo, valor))
        random.shuffle(self.mazo)
    
    def mostrar_mazo(self):
        for c in self.mazo:
            print(str(c.valor) + c.simbolo)
            
    def proxima_carta(self, j):
        j.recibir_carta(self.mazo[0])
        self.mazo.remove(self.mazo[0])

class Jugador:
    def __init__(self, n):
        self.mano = []
        self.nombre = n
    
    def recibir_carta(self, c):    
        self.mano.append(c)
    
    def mostrar_mano(self):
        print('Cartas de ' + self.nombre +":")    
        for c in self.mano:
            print(str(c.valor) + c.simbolo, end = " ")
        print(" - " + str(self.contar_mano()))
    
    def contar_mano(self):
        contador = 0
        cont_ases = 0
        
        for c in self.mano:
            if(c.get_valor == 'A'):
                cont_ases += 1
            else:
                contador += c.get_valor()
        contador += cont_ases
        ases_usados = 0
        while(contador <= 11 and ases_usados < cont_ases):
            contador += 10
            ases_usados += 1
        return contador
    
mazo = Mazo()
proxTurno = False

print("== ♠ ♣ 𝓑𝓵𝓪𝓬𝓴𝓙𝓪𝓬𝓴 ♥ ♦ ==")
print('Por favor ingrese su nombre:')
jugador = Jugador((input()))

banca = Jugador('La Banca')

mazo.proxima_carta(jugador)
mazo.proxima_carta(jugador)          

mazo.proxima_carta(banca)
mazo.proxima_carta(banca)

while(jugador.contar_mano() <= 21):
    jugador.mostrar_mano()
    print('¿Que desea hacer?')
    print('1- Pedir')
    print('2- Plantarse')
    r = int(input())
    if(r == 1):
        mazo.proxima_carta(jugador)
    if(r == 2):
        proxTurno = True
        break        
proxTurno = True
    
if(proxTurno):
    banca.mostrar_mano()
    while(banca.contar_mano() <= 21):
        mazo.proxima_carta(banca)
  
  
if(jugador.contar_mano() > 21):
    print("El jugador queda eliminado con " + str(jugador.contar_mano()))
    jugador.mostrar_mano()
else:
    print("El jugador gana la ronda con " + str(jugador.contar_mano()))
    jugador.mostrar_mano()
    
if(banca.contar_mano() > 21):
    print("La Banca queda eliminada con " + str(banca.contar_mano()))
    banca.mostrar_mano()
else:
    print("La banca gana la ronda con " + str(banca.contar_mano())) 
    banca.mostrar_mano()