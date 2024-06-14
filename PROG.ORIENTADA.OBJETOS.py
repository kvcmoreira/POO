class ClimaDiario:
    def __init__(self):
        self.temperaturas = []

    def ingresar_temperatura(self, dia):
        temp = float(input(f"Ingrese la temperatura para el día {dia + 1}: "))
        self.temperaturas.append(temp)

    def calcular_promedio_semanal(self):
        return sum(self.temperaturas) / len(self.temperaturas)

class ClimaDetallado(ClimaDiario):
    def __init__(self):
        super().__init__()
        self.detalles = []

    def ingresar_temperatura(self, dia):
        temp = float(input(f"Ingrese la temperatura para el día {dia + 1}: "))
        detalle = input(f"Ingrese detalles adicionales para el día {dia + 1}: ")
        self.temperaturas.append(temp)
        self.detalles.append(detalle)

    def mostrar_detalles(self):
        for dia in range(7):
            print(f"Día {dia + 1}: {self.temperaturas[dia]}°C, Detalles: {self.detalles[dia]}")

def main():
    clima = ClimaDetallado()
    for dia in range(7):
        clima.ingresar_temperatura(dia)
    clima.mostrar_detalles()
    promedio = clima.calcular_promedio_semanal()
    print(f"La temperatura promedio semanal es: {promedio:.2f}°C")

if __name__ == "__main__":
    main()
