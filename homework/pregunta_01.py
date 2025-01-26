import pandas as pd

def pregunta_01():

    filename = "files/input/clusters_report.txt"
    with open(filename, 'r', encoding='utf-8') as file:
        data_lines = file.readlines()[4:]

    processed_data = []
    temp_data = []

    for line in data_lines:
        line = line.strip()

        if line:
            elements = line.split()
            if len(temp_data) == 0:
                temp_data = [
                    int(elements[0]),
                    int(elements[1]),
                    float(elements[2].replace(',', '.')),
                    " ".join(elements[4:])
                ]
            else:
                temp_data[3] += " " + " ".join(elements)
        else:
            if temp_data:
                temp_data[3] = temp_data[3].replace('.', '')
                processed_data.append(temp_data)
                temp_data = []

    if temp_data:
        temp_data[3] = temp_data[3].replace('.', '')
        processed_data.append(temp_data)

    return pd.DataFrame(processed_data, columns=['cluster', 'cantidad_de_palabras_clave', 'porcentaje_de_palabras_clave', 'principales_palabras_clave'])