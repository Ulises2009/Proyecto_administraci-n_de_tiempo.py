import random
import datetime
import math
import statistics
import matplotlib.pyplot as plt

# ARREGLOS (3)
actividades = []
horas = []
dias = []

# FUNCION 1: ingresar datos con manejo de errores
def pedir_datos():
    while True:
        try:
            n = int(input("¿Cuántas actividades deseas registrar? "))
            if n <= 0:
                print("Debe ser mayor a 0")
                continue
            break
        except:
            print("Ingresa un número válido")

    for i in range(n):
        act = input(f"Actividad {i+1}: ")
        dia = input("Día: ")

        while True:
            try:
                h = float(input("Horas: "))
                if h < 0:
                    print("No puede ser negativo")
                    continue
                break
            except:
                print("Ingresa un número válido")

        actividades.append(act)
        dias.append(dia)
        horas.append(h)

# FUNCION 2
def total_horas():
    try:
        return sum(horas)
    except:
        return 0

# FUNCION 3
def promedio():
    try:
        return statistics.mean(horas)
    except:
        return 0

# FUNCION 4
def mostrar_datos():
    print("\n--- Registro ---")
    for i in range(len(actividades)):
        print(actividades[i], "-", dias[i], ":", horas[i], "horas")

# FUNCION 5 (evaluación)
def evaluar_tiempo():
    total = total_horas()
    exceso = total > 24  # bool

    if exceso:
        print("⚠ Exceso de horas")
    elif total < 10:
        print("⚠ Muy pocas actividades")
    else:
        print("✔ Buen uso del tiempo")

# FUNCION 6 (nueva)
def recomendaciones():
    print("\n--- Recomendaciones ---")
    for i in range(len(horas)):
        if horas[i] > 6:
            print("Reduce tiempo en", actividades[i])
        elif horas[i] < 2:
            print("Aumenta tiempo en", actividades[i])

# FUNCION 7 (nueva con math)
def analisis_avanzado():
    try:
        print("\nMayor tiempo:", max(horas))
        print("Menor tiempo:", min(horas))
        print("Desviación estándar:", round(statistics.stdev(horas),2))
    except:
        print("No hay suficientes datos")

# FUNCION 8 (gráfico)
def grafico():
    try:
        plt.bar(actividades, horas)
        plt.title("Uso del tiempo")
        plt.xlabel("Actividades")
        plt.ylabel("Horas")
        plt.show()
    except:
        print("Error al generar gráfico")

# FUNCION 9 (uso de datetime)
def fecha_actual():
    print("\nFecha del análisis:", datetime.datetime.now())

# FUNCION 10 (uso de random)
def consejo_random():
    consejos = [
        "Organiza mejor tu día",
        "Descansa al menos 7 horas",
        "Evita distracciones",
        "Prioriza actividades importantes"
    ]
    print("Consejo:", random.choice(consejos))

# MAIN
def main():
    pedir_datos()
    mostrar_datos()

    print("\nTotal horas:", total_horas())
    print("Promedio:", promedio())

    evaluar_tiempo()
    recomendaciones()
    analisis_avanzado()

    fecha_actual()
    consejo_random()

    grafico()

main()
