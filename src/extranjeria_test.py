from extranjeria import*

def test_lee_datos_extranjeria(datos):
    print("\ntest_lee_datos_extranjeria")
    print(f"leidos {len(datos)} registros.")
    print("los tres primeros son:")
    for i in range(0,3,1):    
        print(datos[i])
    print("los tres ultimos son:")
    for i in range(-3,0,1):
        print(datos[i])

def test_numero_nacionalidades_distintas(datos):
    print("\ntest_numero_nacionalidades_distintas")
    print(f"hay {numero_nacionalidades_distintas(datos)} nacionalidades distintas en los datos")

def test_secciones_distritos_con_extranjeros_nacionalidades(datos):
    print("\ntest_secciones_distritos_con_extranjeros_nacionalidades")
    lista_paises = ["ALEMANIA", "ITALIA"]
    res = secciones_distritos_con_extranjeros_nacionalidades(datos,  lista_paises)
    print(f"hay {len(res)} secciones de distritos con residentes cuya procedencia es {lista_paises}")
    print(res[:3])

def test_total_extranjeros_por_pais(datos):
    print("\ntest_total_extranjeros_por_pais")
    d = total_extranjeros_por_pais(datos)
    mostrar_iterable([it for it in d.items()][:3])

def mostrar_iterable(it)->None:
    for elem in it:
        print(elem)

def test_top_n_extranjeria(datos):
    print("\ntest_top_n_extranjeria")
    n = 5
    print(top_n_extranjeria(datos,n))

def test_barrio_mas_multicultural(datos):
    print("\ntest_barrio_mas_multicultural")
    print("el barrio mas mulricultural del sevilla es: ",barrio_mas_multicultural(datos))

def test_barrio_con_mas_extranjeros(datos):
    print("\ntest_barrio_con_mas_extranjeros")
    print("El barrio con más residentes extranjeros es: ",barrio_con_mas_extranjeros(datos))
    print("El barrio con más hombres residentes extranjeros es: ",barrio_con_mas_extranjeros(datos, "HOMBRES"))
    print("El barrio con más mujeres residentes extranjeras es: ",barrio_con_mas_extranjeros(datos, "MUJERES"))

def test_pais_mas_representado_por_distrito(datos):
    print("\ntest_pais_mas_representado_por_distrito")
    print("Los países con más residentes en cada distrito son los siguientes:")
    for i in pais_mas_representado_por_distrito(datos).items():
        print("Dstrito:",i)

if __name__=="__main__":
    datos = lee_datos_extranjeria("Proyectos Python\WSPython\git\lp06-extranjeria-hadiminou-main\data\extranjeriaSevilla.csv")
    #test_lee_datos_extranjeria(datos)
    #test_numero_nacionalidades_distintas(datos)
    #test_secciones_distritos_con_extranjeros_nacionalidades(datos)
    #test_total_extranjeros_por_pais(datos)
    #test_top_n_extranjeria(datos)
    #test_barrio_mas_multicultural(datos)
    #test_barrio_con_mas_extranjeros(datos)
    test_pais_mas_representado_por_distrito(datos)