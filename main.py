import csv

class Empleado:
    def __init__(self, nombre, apellido, edad, salario, deducciones, genero):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = int(edad)
        self.salario = float(salario)
        self.deducciones = float(deducciones)
        self.genero = genero

class ProcesadorCSV:
    def __init__(self, archivo_csv):
        self.empleados = self.cargar_datos(archivo_csv)

    def cargar_datos(self, archivo_csv):
        empleados = []
        with open(archivo_csv, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                empleado = Empleado(row['Nombre'], row['Apellido'], row['Edad'], row['Salario'], row['Deducciones'], row['Género'])
                empleados.append(empleado)
        return empleados

    def persona_mayor_edad(self):
        return max(self.empleados, key=lambda empleado: empleado.edad)

    def persona_menor_edad(self):
        return min(self.empleados, key=lambda empleado: empleado.edad)

    def contar_genero(self):
        hombres = sum(1 for empleado in self.empleados if empleado.genero.lower() == 'masculino')
        mujeres = sum(1 for empleado in self.empleados if empleado.genero.lower() == 'femenino')
        return hombres, mujeres

    def promedio_salario(self):
        total_salario = sum(empleado.salario for empleado in self.empleados)
        return total_salario / len(self.empleados)

    def persona_con_mas_deducciones(self):
        return max(self.empleados, key=lambda empleado: empleado.deducciones)

    def persona_con_mayor_salario(self):
        return max(self.empleados, key=lambda empleado: empleado.salario)

procesador = ProcesadorCSV('DatosCSV.csv')

persona_mayor_edad = procesador.persona_mayor_edad()
persona_menor_edad = procesador.persona_menor_edad()
hombres, mujeres = procesador.contar_genero()
promedio_salario = procesador.promedio_salario()
persona_mas_deducciones = procesador.persona_con_mas_deducciones()
persona_mayor_salario = procesador.persona_con_mayor_salario()

print(f"Empleado con mayor edad: {persona_mayor_edad.nombre} {persona_mayor_edad.apellido} ({persona_mayor_edad.edad} años)")
print(f"Empleado con menor edad: {persona_menor_edad.nombre} {persona_menor_edad.apellido} ({persona_menor_edad.edad} años)")
print(f"Cantidad de hombres: {hombres}")
print(f"Cantidad de mujeres: {mujeres}")
print(f"Promedio de salario: {promedio_salario:.2f} Lps")
print(f"Empleado con más deducciones: {persona_mas_deducciones.nombre} {persona_mas_deducciones.apellido}")
print(f"Empleado con mayor salario: {persona_mayor_salario.nombre} {persona_mayor_salario.apellido}")
