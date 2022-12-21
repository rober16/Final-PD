import random

def bienvenida():
    print("== ♠ ♣ 𝓑𝓵𝓪𝓬𝓴𝓙𝓪𝓬𝓴 ♥ ♦ ==")
    nombre = input('Por favor ingrese su nombre:')
    nombre = str(nombre)
    return nombre

def generarMazo():
    numeros = list(range(2,11)) + ['J', 'Q', 'K', 'A']
    simbolos = ['♠', '♣', '♥', '♦']
    mazo = [(str(n) + s) for n in numeros for s in simbolos]
    random.shuffle(mazo)
    return mazo
    
def repartirCartas(mazo):
    mano = []
    list(map(lambda c: mano.append(c), mazo[0:2]))
    quitarCartas(mazo, mazo[0:2])
    return mano

def quitarCartas(mazo, cartas):
    for n in cartas:
        mazo.remove(n)

def getValor(valor):
    if(valor in ['J', 'Q', 'K']):
        return 10
    else:
        return valor

def obtenerNumero(m):
    new_m = m[:-1]
    return new_m

def contar_mano(mano):
    new_mano = list(map(obtenerNumero, mano))
    contador = 0
    cont_ases = 0
        
    for m in new_mano:
        if(m == "A"):
            cont_ases += 1
        else:
            contador += int(getValor(m))
    contador += cont_ases
    #ases_usados = 0
    #while(contador <= 11 and ases_usados < cont_ases):
    #    contador += 10
    #    ases_usados += 1
        
    return contador

def mostrar_mano(mano, nombre):
        print('\tCartas de ' + nombre + ": " + str(mano), end=" ")    
        print(" - " + str(contar_mano(mano)))

def proxima_carta(mazo, mano):
    list(map(lambda c: mano.append(c), mazo[0:1]))
    quitarCartas(mazo, mazo[0:1])
    return mano

def main():
    jugador = bienvenida()
    banca = "La Banca"
    turnoPC = False
    mazo = generarMazo()   
   
    manoJugador = repartirCartas(mazo)
    manoBanca = repartirCartas(mazo)
    
    while(contar_mano(manoJugador) <= 21):
        mostrar_mano(manoJugador, jugador)
        print('¿Que desea hacer?')
        print('\t1- Pedir')
        print('\t2- Plantarse')
        r = int(input())
        if(r == 1):
             proxima_carta(mazo, manoJugador)
        if(r == 2):
            print("El jugador se planto con - " + str(contar_mano(manoJugador)))
            turnoPC = True
            break        
    turnoPC = True
    
    if(turnoPC):
        mostrar_mano(manoBanca, banca)
        while(contar_mano(manoBanca) <= 16):
                proxima_carta(mazo, manoBanca)

    if(contar_mano(manoJugador) > 21 or contar_mano(manoBanca) > contar_mano(manoJugador) and contar_mano(manoBanca) <= 21):
        print(jugador + " queda eliminado!")
        mostrar_mano(manoJugador, jugador)
        mostrar_mano(manoBanca, banca)
    elif(contar_mano(manoJugador) > contar_mano(manoBanca) and contar_mano(manoJugador) <= 21 or contar_mano(manoBanca) > 21):
        if(contar_mano(manoJugador) == 21):
            print(jugador + " gana la ronda con BlackJack!")
        else:
            print(jugador + " gana la ronda!")
        mostrar_mano(manoJugador, jugador)
        mostrar_mano(manoBanca, banca)
    else: 
        print("Empate!")
        mostrar_mano(manoJugador, jugador)
        mostrar_mano(manoBanca, banca)
                       
if __name__ == "__main__":
    main()