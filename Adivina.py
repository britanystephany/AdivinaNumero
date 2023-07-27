import random 

def jugar_nuevo():
    print("\nVolver a jugar el juego (s/n)")
    respuesta = input ().lower()
    return respuesta == "s"

minNumero = 0
maxNumero = 15

print ("Hola, hoy vamos a jugar a adivinar numeros")
print("Cual es tu nombre?")
username = input()

print("Mucho gusto " + username + ". " + "Comencemos el juego!")

while True:
    number = random.randint(minNumero,maxNumero) 
    print("Estoy pensando en un numero entre el " + str(minNumero) + " y el " + str(maxNumero))
    guessesTaken = 0
    limIntentos = 5

    while guessesTaken < limIntentos:
        print ("Inserta tu prediccion de numero: ")
        print ("Tus numero de intentos son : " + str(guessesTaken) + "/" + str(limIntentos)+".")
        guess = input ()
        guess = int (guess)

        guessesTaken = guessesTaken + 1

        if guess < number:
            print ("El numero es muy chico")
        if guess > number:
            print ("El numero es muy grande")
        if guess == number:
            print ("Muchas felicidades " +username+ " acertaste el numero con: " + str(guessesTaken) + " intentos.")
            break
    if guessesTaken >= limIntentos:
        print ("El numero que estaba pensando era: " + str(number) + ". Puedes volver a intentarlo.")

    if not jugar_nuevo ():
        print ("Gracias por jugar, vuelve pronto!")
        break