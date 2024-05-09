import csv

# los calculos chinos los hizo Jere, si tenes dudas hablá con él

INPUT = "../chipi/trackeo-original.csv"
OUTPUT = "../chipi/trackeo-mod.csv"

mul_x = -1
mul_y = -1

def generar_archivo_nuevo(input, output):

    with open(input, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Ignorar la primera fila que contiene los encabezados
        datos = list(reader)

    # Obtener el primer valor de X y de Y
    origen_x = float(datos[0][0])
    origen_y = float(datos[0][1])
    origen = (origen_x, origen_y)

    nuevos_datos = []
    for x, y, tiempo in datos:
        new_x, new_y = change_origen(x,y,origen)
        nuevos_datos.append((str(new_x), str(new_y), tiempo))

    with open(output, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["X", "Y", "Time"])
        writer.writerows(nuevos_datos)

def change_origen(x,y,origen):
    x = float(x)
    y = float(y)
    new_x = round(mul_x * (x - origen[0]), 4)
    new_y = round(mul_y * (y - origen[1]), 4)
    if new_x == -0.0:
        new_x = str(new_x).replace('-0.0', '0.0')
    if new_y == -0.0:
        new_y = str(new_y).replace('-0.0', '0.0')
    return (new_x, new_y)


if __name__ == "__main__":
    generar_archivo_nuevo(INPUT, OUTPUT)