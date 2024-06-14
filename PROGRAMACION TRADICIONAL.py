def ingresar_temperaturas():
    temperaturas = {}
    dias = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo']
    for dia in dias:
        temp = float(input(f"Ingrese la temperatura para el {dia}: "))
        temperaturas[dia] = temp
    return temperaturas

def calcular_promedio(temperaturas):
    return sum(temperaturas.values()) / len(temperaturas)

def mostrar_temperaturas(temperaturas):
    for dia, temp in temperaturas.items():
        print(f"{dia}: {temp}°C")

def main():
    temperaturas = ingresar_temperaturas()
    promedio = calcular_promedio(temperaturas)
    mostrar_temperaturas(temperaturas)
    print(f"\nLa temperatura promedio semanal es: {promedio:.2f}°C")

if __name__ == "__main__":
    main()
