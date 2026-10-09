from api.consulta import consultar
from ui.menu import pedir_datos, mostrar

Departamento, Municipio, Cultivo, num_registros = pedir_datos()

if Departamento and Municipio and Cultivo:
    result_df = consultar(Departamento, Municipio, Cultivo, num_registros)
    mostrar(result_df)
else:
    print("Error: Uno o más de los valores ingresados no son válidos.")