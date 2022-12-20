import random

def bienvenida():
    print("== ♠ ♣ 𝓑𝓵𝓪𝓬𝓴𝓙𝓪𝓬𝓴 ♥ ♦ ==")
    nombre = input('Por favor ingrese su nombre:')
    nombre = str(nombre)
    return nombre

def generarMazo():
    numeros = list(range(2,11)) + ['J', 'Q', 'K', 'A']
    simbolos = ['♠', '♣', '♥', '♦']
    #mazo = list(map(lambda x,y : str(x) + y, numeros, simbolos))
    mazo = [(str(n) + s) for n in numeros for s in simbolos]
    random.shuffle(mazo)
    return mazo
    
def repartirCartas(mazo):
    mano = []
    
    #Se reparten 2 cartas por jugador
    idx1 = random.randint(1, 47)
    mano.append(mazo[idx1])
    mazo.remove(mazo[idx1])
    
    idx2 = random.randint(1, 47)
    mano.append(mazo[idx2])
    mazo.remove(mazo[idx2])
    
    return mano

def getValor(valor):
    if(valor in ['J', 'Q', 'K', 'A']):
        return 10
    return valor

def obtenerNumero(m):
    new_m = m[:-1]
    return new_m

def contar_mano(mano):
    new_mano = list(map(obtenerNumero, mano))
    contador = 0
    cont_ases = 0
        
    for m in new_mano:
        if(m == 'A'):
            cont_ases += 1
        else:
            contador += int(getValor(m))
    contador += cont_ases
    ases_usados = 0
    while(contador <= 11 and ases_usados < cont_ases):
        contador += 10
        ases_usados += 1
    return int(contador)

def mostrar_mano(mano, nombre):
        print('Cartas de ' + nombre +":")    
        print(mano , end = " ")
        print(" - " + str(contar_mano(mano)))

def proxima_carta(mazo, mano):
    idx1 = random.randint(1, 47)
    mano.append(mazo[idx1])
    mazo.remove(mazo[idx1])
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
        print('1- Pedir')
        print('2- Plantarse')
        r = int(input())
        if(r == 1):
             proxima_carta(mazo, manoJugador)
        if(r == 2):
            turnoPC = True
            break        
    proxTurno = True
    
    
    if(proxTurno):
        mostrar_mano(manoBanca, banca)
        while(contar_mano(manoBanca) <= 21):
            proxima_carta(mazo, manoBanca)
    
    
    if(contar_mano(manoJugador) > 21):
        print("El jugador queda eliminado con " + str(contar_mano(manoJugador)))
        mostrar_mano(manoJugador, jugador)
    else:
        print("El jugador gana la ronda con " + str(contar_mano(manoJugador)))
        mostrar_mano(manoJugador, jugador)

    if(contar_mano(manoBanca) > 21):
        print("La Banca queda eliminada con " + str(contar_mano(manoBanca)))
        mostrar_mano(manoBanca, banca)
    else:
        print("La banca gana la ronda con " + str(contar_mano(manoBanca))) 
        mostrar_mano(manoBanca, banca)
                       
if __name__ == "__main__":
    main()