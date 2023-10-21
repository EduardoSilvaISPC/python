import os
import requests
from bs4 import BeautifulSoup
import csv
import mysql.connector

# Definir la ruta completa donde deseas guardar el archivo CSV
ruta_completa = r'C:\Users\delfe\Desktop\BSoup\scrap'

# URL de la página
url = 'https://datosmacro.expansion.com/demografia/migracion/inmigracion/argentina'

# Realizar la solicitud GET
response = requests.get(url)

# Parsear el contenido HTML con BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

# Encontrar la tabla por su clase
table = soup.find('table', class_='tabledat')

# Verificar si la tabla se ha encontrado
if table:
    # Inicializar listas para almacenar los datos
    years = []
    inmigration_men = []
    inmigration_women = []
    total_inmigration = []

    # Encontrar todas las filas de datos en la tabla
    rows = table.find_all('tr')

    # Iterar a través de las filas, comenzando desde la segunda fila (índice 1) para omitir el encabezado
    for row in rows[1:]:
        # Encontrar todas las columnas de datos en la fila
        columns = row.find_all('td')

        # Extraer los datos y almacenarlos en las listas correspondientes
        year = columns[0].text.strip()
        men = columns[1].text.strip().replace('.', '')
        women = columns[2].text.strip().replace('.', '')
        total = columns[3].text.strip().replace('.', '')

        years.append(year)
        inmigration_men.append(men)
        inmigration_women.append(women)
        total_inmigration.append(total)

    # Crear un archivo CSV en la ubicación especificada y escribir los datos en él
    csv_filename = os.path.join(ruta_completa, 'argentina_inmigrantes_totales_tabla1.csv')
    with open(csv_filename, 'w', newline='', encoding='utf-8') as csv_file:
        fieldnames = ['Year', 'Inmigration Men', 'Inmigration Women', 'Total Inmigration', 'Percentage Emigration']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()

        for i in range(len(years)):
            writer.writerow({
                'Year': years[i],
                'Inmigration Men': inmigration_men[i],
                'Inmigration Women': inmigration_women[i],
                'Total Inmigration': total_inmigration[i],
            })
else:
    print("La tabla no se encontró en la página.")

print("Datos extraídos y guardados en el archivo CSV en la ubicación especificada:", csv_filename)

# Creación de la conexión con el servidor
try:
    connection = mysql.connector.connect(
        host='127.0.0.1',
        port=3306,
        user='root',
        password='root'
    )

    if connection.is_connected():
        print("Conexión exitosa")

    # Crear o eliminar la base de datos según tus necesidades
    cursor = connection.cursor()
    delete_database_query = "DROP DATABASE IF EXISTS inmigra"
    cursor.execute(delete_database_query)
    create_database_query = "CREATE DATABASE inmigra"
    cursor.execute(create_database_query)
    cursor.close()

    # Reconectar a la nueva base de datos
    connection = mysql.connector.connect(
        host='127.0.0.1',
        port=3306,
        user='root',
        password='root',
        database='inmigra'
    )
    if connection.is_connected():
        print("Conexión a la base de datos exitosa")

except Exception as ex:
    print(ex)

# Creación del cursor para recorrer la base
cursor = connection.cursor()

# Crear una tabla si no existe
create_table_query = """
CREATE TABLE IF NOT EXISTS inmigracion (
    id INT AUTO_INCREMENT PRIMARY KEY,
    year INT,
    inmigration_men INT,
    inmigration_women INT,
    total_inmigration INT
)
"""
cursor.execute(create_table_query)

# Insertar datos en la tabla
insert_query = """
INSERT INTO inmigracion (year, inmigration_men, inmigration_women, total_inmigration)
VALUES (%s, %s, %s, %s)
"""

for i in range(len(years)):
    data = (
        years[i],
        int(inmigration_men[i]),
        int(inmigration_women[i]),
        int(total_inmigration[i]),
    )
    cursor.execute(insert_query, data)

# Commit los cambios
connection.commit()
print("Datos insertados en la base de datos SQL.")
cursor.execute("SELECT * FROM inmigracion")
result1 = cursor.fetchall()
print(result1)

# Cerrar la conexión
connection.close()
