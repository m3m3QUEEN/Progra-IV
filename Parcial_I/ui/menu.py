def pedir_datos():
    Departamento = input("Ingrese departamento: ")
    Municipio = input("Ingrese Municipio: ")
    Cultivo = input("Ingrese cultivo: ")
    num_registros = input("Ingrese numero de registros a consultar: ")
    return Departamento, Municipio, Cultivo, num_registros


def mostrar(result_df):
    print(result_df.to_string(index=False))