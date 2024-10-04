import random

#Menu 
def menu():
    while True:
        print("\nSelecciona un juego:")
        print("1. Adivina Número")
        print("2. Piedra - Papel - Tijeras")
        print("3. Ahorcado")
        print("4. Salir")
        opcion = input("Opción: ")

        if opcion == '1':
            adivina_numero()
        elif opcion == '2':
            piedra_papel_tijeras()
        elif opcion == '3':
            ahorcado()
        elif opcion == '4':
            print("¡Gracias por jugar!")
            break
        else:
            print("Opción no válida.")

#Juego adivinar numeros
def adivina_numero():
    numero_aleatorio = random.randint(1, 10)
    print("Adivina un número entre 1 y 10. Tienes 3 intentos.")
    
    intentos = 0
    max_intentos = 3

    while intentos < max_intentos:
        try:
            apuesta = int(input(f"Intento {intentos + 1}: ")) 
            if apuesta < 1 or apuesta > 10:
                print("Número fuera de rango.")
            if apuesta < numero_aleatorio:
                print("El número es mayor.")
            elif apuesta > numero_aleatorio:
                print("El número es menor.")
            else:
                print("¡Felicidades! Has acertado.")
                return #salir si es correcto
            
            intentos += 1
        except ValueError:
            print("Introduce un número válido.")
    
    print(f"Has perdido. El número era: {numero_aleatorio}")
    return #salir al perder

#Juego PPT
def piedra_papel_tijeras():
    puntos_jugador = 0
    puntos_maquina = 0

    while puntos_jugador < 3 and puntos_maquina < 3:
        jugada_jugador = input("Elige 'piedra', 'papel' o 'tijeras': ").lower()
        jugada_maquina = random.choice(['piedra', 'papel', 'tijeras'])
        print(f"Máquina ha sacado: {jugada_maquina}")

        if jugada_jugador == jugada_maquina:
            print("¡Empate!")
        elif (jugada_jugador == 'piedra' and jugada_maquina == 'tijeras') or \
             (jugada_jugador == 'papel' and jugada_maquina == 'piedra') or \
             (jugada_jugador == 'tijeras' and jugada_maquina == 'papel'):
            print("¡Has ganado!")
            puntos_jugador += 1
        else:
            print("¡Has perdido!")
            puntos_maquina += 1

        print(f"Puntuación: Tú {puntos_jugador} - Máquina {puntos_maquina}")

    if puntos_jugador == 3:
        print("¡Felicidades! Ganaste el juego.")
    elif puntos_maquina == 3:
        print("La máquina ganó.")

#Juego Ahorcado
def ahorcado():
    try:
        with open("palabras.txt", "r", encoding="utf-8") as fichero:
            palabras = fichero.read().splitlines()
    except FileNotFoundError:
        print("No se encontró 'palabras.txt'.")
        return

    palabra = random.choice(palabras)
    letras_palabra = len(palabra)
    intentos_maximos = letras_palabra * 2
    tablero = ['_'] * letras_palabra
    
    print(f"Tu palabra tiene {letras_palabra} letras.")
    print(f"Tienes {intentos_maximos} intentos para adivinar la palabra.")

    while intentos_maximos > 0 and '_' in tablero:
        print(" ".join(tablero))
        entrada = input("Introduce una letra o la palabra completa: ").lower()  # Cambiado

        if len(entrada) == 1 and entrada.isalpha():  # Validación de letra
            letra = entrada  # Asignar la letra si es válida
        elif entrada.isalpha() and len(entrada) == letras_palabra:  # Validación de palabra completa
            if entrada == palabra:  # Si la palabra es correcta
                tablero = list(palabra)  # Mostrar la palabra completa
                break  # Salir del bucle
            else:
                intentos_maximos -= 1  # Reducir intentos si la palabra es incorrecta
                print(f"Incorrecto. Te quedan {intentos_maximos} intentos.")
                continue  # Volver al inicio del bucle
        else:
            print("Introduce solo una letra o la palabra completa.")
            continue

        if letra in palabra:
            print("Correcto!!")
            for i, char in enumerate(palabra):
                if char == letra:
                    tablero[i] = letra
        else:
            intentos_maximos -= 1
            print(f"Incorrecto. Te quedan {intentos_maximos} intentos.")

    if '_' not in tablero:
        print(f"Felicidades!! La palabra es: {palabra}")
    else:
        print(f"Perdiste!! La palabra era: {palabra}")


#Iniciamos el Menu de juegos
if __name__ == "__main__":
    menu()