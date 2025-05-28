# /*
#  * EJERCICIO:
#  * Crea dos variables utilizando los objetos fecha (date, o semejante) de tu lenguaje:
#  * - Una primera que represente la fecha (día, mes, año, hora, minuto, segundo) actual.
#  * - Una segunda que represente tu fecha de nacimiento (te puedes inventar la hora).
#  * Calcula cuántos años han transcurrido entre ambas fechas.
#  *


from datetime import datetime

# Formato de fecha en día/mes/año hora:minuto:segundo
formato_fecha="%d/%m/%Y %H:%M:%S"

fecha1=datetime.now()
fecha2=datetime(2002, 1, 12, 1, 30, 12)

# Imprimir fechas en el formato correcto
print(fecha1.strftime(formato_fecha))
print(fecha2.strftime(formato_fecha))

# Función para calcular los años transcurridos
def calcular_años(fecha_actual, fecha_nacimiento):
    edad = fecha_actual.year - fecha_nacimiento.year

    # Ajustar si aún no ha pasado el cumpleaños en el año actual
    if (fecha_actual.month, fecha_actual.day) < (fecha_nacimiento.month, fecha_nacimiento.day):
        edad -= 1
    
    print("Años transcurridos:", edad)


calcular_años(fecha1, fecha2)


print("_______________________________________________")
#  * DIFICULTAD EXTRA (opcional):
#  * Utilizando la fecha de tu cumpleaños, formatéala y muestra su resultado de
#  * 10 maneras diferentes. Por ejemplo:
#  * - Día, mes y año.
#  * - Hora, minuto y segundo.
#  * - Día de año.
#  * - Día de la semana.
#  * - Nombre del mes.
#  * (lo que se te ocurra...)
#  */
fecha_cumpleaños=datetime(2002, 1, 12, 1, 30, 12)

fecha_dma = fecha_cumpleaños.strftime("%d/%m/%Y")
print(fecha_dma)

fecha_hms=fecha_cumpleaños.strftime("%H:%M:%S")
print(fecha_hms)

dia_año=fecha_cumpleaños.timetuple().tm_yday
print(dia_año)

#de esta forma entrega el numero del dia en la semana
#empezando en 0= Lunes, 1=Martes,... 6=Domingo

dia_semana = fecha_cumpleaños.weekday()
print(dia_semana)

#puedes usar tambien una lista junto con el weekday para determinar el dia en español
dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
print(dias[dia_semana])

#usando %A: este nos da el nombre pero en ingles
dia_semana2  =fecha_cumpleaños.strftime("%A")
print(dia_semana2)

#parecido al weekday pero aqui no empieza en 0 sino en 1
#por lo tanto si quiere usar una lista para que te de el nombre en español restale 1

nombre_mes = fecha_cumpleaños.month
print(nombre_mes)
meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio",
         "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]

print(meses[nombre_mes-1])


#usando %B
nombre_mes2 = fecha_cumpleaños.strftime("%B")
print(nombre_mes2)


semana_año=fecha_cumpleaños.strftime("%U")
print(f"Semana N°:{semana_año} del año {fecha_cumpleaños.year}")

año = fecha_cumpleaños.year
año_bisiesto=(año % 4 == 0 and año %100 !=0) or (año % 400==0)
print(f"Año bisiesto : {'Si' if año_bisiesto else 'No'}")