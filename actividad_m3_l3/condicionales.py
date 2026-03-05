# FUNDAMENTOS DE PROGRAMACION EN PYTHON
# ACTIVIDAD N°3 - CONTROL DE FLUJO CON SENTENCIAS CONDICIONALES
# -------------------------------------------------------------

# 1. DECISIÓN SIMPLE
num = int(input('Ingrese un número: ')) # Se solicita al usuario ingresar un número
if num >= 18: # Condición si es mayor igual a 18
    print('Eres mayor de edad') # si es mayor de edad imprime por pantalla el mensaje
else: # Condición si es menor a 18 
    print('Eres menor de edad') # si es menor de edad imprime por pantalla el mensaje

# 2. DECISIÓN MULTIPLE CON ELIF
nota = float(input("Ingresa una calificación entre 1 y 7: "))  # pide al usuario una nota y la guarda como número decimal
if nota == 7:             # si la nota es exactamente 7
    print("Excelente")    # muestra Excelente
elif nota == 6:           # si la nota es exactamente 6
    print("Muy bien")     # muestra Muy bien
elif nota == 5:           # si la nota es exactamente 5
    print("Bien")         # muestra Bien
elif nota == 4:           # si la nota es exactamente 4
    print("Suficiente")   # muestra Suficiente
elif nota < 4:               # si la nota es menor que 4
    print("Insuficiente")    # muestra Insuficiente

# 3. CONDICIONES ANIDADAS
numero = int(input("Ingresa un número entero: "))   # pide un número entero al usuario
if numero >= 0:                                     # primer if: verifica si el número es 0 o positivo
    if numero == 0:                                 # segundo if dentro del primero
        print("Es cero")                            # si es 0 muestra este mensaje  
    else:                                           # si no es 0 pero sí es >= 0
        print("Número positivo")                    # entonces es positivo
else:                                               # si no es >= 0 entonces es negativo
    print("Número negativo")                        # muestra que es negativo

# 4. CONDICION DE BORDE
numero_usuario = int(input("Ingresa un número entre 1 y 100: "))  # pedimos un número al usuario y lo guardamos
# Bloque que verifica si el número está exactamente en los límites permitidos
if numero_usuario == 1 or numero_usuario == 100:   # si el número es 1 o 100
    print("Estás en un límite permitido")          # mensaje para los extremos
# Bloque que verifica si el número está dentro del rango pero no es extremo
elif numero_usuario > 1 and numero_usuario < 100:  # si está entre 2 y 99
    print("Dentro del rango")                      # mensaje para números dentro del rango
# Bloque que captura cualquier otro caso fuera del rango permitido
else:                                              # si no cumple ninguna condición anterior
    print("Fuera del rango")                       # mensaje si el número está fuera del rango