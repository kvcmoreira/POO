class Clima:
    def ingresar_temperatura(self, dia):
        raise NotImplementedError("Este método debe ser implementado por subclases")

    def calcular_promedio_semanal(self):
        raise NotImplementedError("Este método debe ser implementado por subclases")

class ClimaDiario(Clima):
    def __init__(self):
        self._temperaturas = []

    def ingresar_temperatura(self, dia):
        temp = float(input(f"Ingrese la temperatura para el día {dia + 1}: "))
        self._temperaturas.append(temp)

    def calcular_promedio_semanal(self):
        return sum(self._temperaturas) / len(self._temperaturas)

class ClimaDetallado(ClimaDiario):
    def __init__(self):
        super().__init__()
        self._detalles = []

    def ingresar_temperatura(self, dia):
        temp = float(input(f"Ingrese la temperatura para el día {dia + 1}: "))
        detalle = input(f"Ingrese detalles adicionales para el día {dia + 1}: ")
        self._temperaturas.append(temp)
        self._detalles.append(detalle)

    def mostrar_detalles(self):
        for dia in range(7):
            print(f"Día {dia + 1}: {self._temperaturas[dia]}°C, Detalles: {self._detalles[dia]}")

def main():
    clima = ClimaDetallado()
    for dia in range(7):
        clima.ingresar_temperatura(dia)
    clima.mostrar_detalles()
    promedio = clima.calcular_promedio_semanal()
    print(f"La temperatura promedio semanal es: {promedio:.2f}°C")

if __name__ == "__main__":
    main()
