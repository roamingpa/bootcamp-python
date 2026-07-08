from empleado import Empleado


if __name__ == "__main__":
    for x in range(3):
        nombre = input(f"Ingrese nombre del empleado {x+1}")
        edad = input(f"Ingrese edad del empleado {x+1}")
        salario = input(f"Ingrese salario del empleado {x+1}")
        cargo = input(f"Ingrese el cargo del empleado {x+1}")
        empleado = Empleado(
            nombre=nombre,
            edad=int(edad),
            salario=int(salario),
            cargo=cargo,
        )
        empleado.crear_correo_institucional()

        print(f"Empleado {empleado.nombre} tiene un salario de ${empleado.salario}")

        empleado.aumentar_salario(7_000)
        print(f"Empleado {empleado.nombre} tiene un salario de ${empleado.salario}")

        empleado.trabajar(10)

        pago = empleado.calcular_pago()
        print(f"Empleado {empleado.nombre} hay que pagarle ${pago} por sus servicios")

        print(f"Lunes Es día laboral?: {empleado.es_dia_laboral('Lunes')}")
        print(f"Domingo Es día laboral?: {empleado.es_dia_laboral('domingo')}")

        print(f"Lunes Es día laboral?: {Empleado.es_dia_laboral('Lunes')}")
        print(f"Domingo Es día laboral?: {Empleado.es_dia_laboral('domingo')}")

        print(empleado.__dict__)