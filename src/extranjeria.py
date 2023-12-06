from collections import namedtuple
import csv
from typing import*
#RegistroExtranjeria = namedtuple('RegistroExtranjeria', [('distrito', str),('seccion', str),\
# ('barrio', str),('pais', str),('hombres', int),('mujeres', int)])
RegistroExtranjeria = namedtuple('RegistroExtranjeria', 'distrito, seccion, barrio, pais, hombres, mujeres')

def lee_datos_extranjeria(ruta_fichero:str)->list[tuple[RegistroExtranjeria]]:
    res = []
    with open (ruta_fichero, 'rt', encoding = 'utf-8') as f:
        lector = csv.reader(f, delimiter = ',')
        next(lector)
        res = [RegistroExtranjeria(distrito.strip(), seccion.strip(), barrio, pais, int(hombres),\
                    int(mujeres)) for distrito, seccion, barrio, pais, hombres, mujeres in lector]
    return res

def numero_nacionalidades_distintas(registros:list[RegistroExtranjeria])->int:
    res = set()
    res = {i.pais for i in registros}
    return len(res)

def secciones_distritos_con_extranjeros_nacionalidades(registros:list[RegistroExtranjeria],  paises:set[str])->list[tuple[str,str]]:
    res = set()
    res = {(i.distrito, i.seccion) for i in registros if i.pais in paises}
    return sorted(res)

def total_extranjeros_por_pais(registros:list[RegistroExtranjeria])->dict[str, int]:
    res = dict()
    for i in registros:
        if i.pais not in res:
            res[i.pais] = 0
        res[i.pais]+=(i.hombres+i.mujeres)
    return res
    
def top_n_extranjeria(registros:list[RegistroExtranjeria],  n:int=3)->list[tuple[str, int]]:
    res = list()
    dic_aux = total_extranjeros_por_pais(registros)
    res = sorted(dic_aux.items(), key = lambda e:e[1], reverse = True)[:n]
    return res

def barrio_mas_multicultural(registros:list[RegistroExtranjeria])->str:
    res = dict()
    for i in registros:
        if i.barrio not in res:
            res[i.barrio] = set()
        res[i.barrio].add(i.pais)
    #return max(res, key = lambda barrio:len(res.get(barrio)))
    return max(res.items(), key = lambda e:len(e[1]))[0]

    
def barrio_con_mas_extranjeros(registros:list[RegistroExtranjeria], tipo:Optional[str]=None)->str:
    res = dict()
    for i in registros:
        if i.barrio not in res:
            res[i.barrio] = 0
        if tipo == "HOMBRES":
            res[i.barrio] += (i.hombres)
        if tipo == "MUJERES":
            res[i.barrio] += (i.mujeres)
        if tipo == None:
            res[i.barrio] += (i.hombres+i.mujeres)
    return max(res.items(), key = lambda e:e[1])[0]

def pais_mas_representado_por_distrito(registros:list[RegistroExtranjeria])->dict[str,str]:
    res = dict()
    aux = dict()
    for i in registros:
        num_extranjeros = i.hombres + i.mujeres
        if i.distrito not in res:
            res[i.distrito] = list()
        res[i.distrito] += [((i.distrito, i.seccion, i.barrio, i.pais, num_extranjeros))]
    for c,v in res.items():
        aux[c] = max(v, key = lambda e:e[4])[3]
    return aux

# def pais_mas_representado_por_distrito(registros:list[RegistroExtranjeria])->dict[str,str]:
#     d_total = total_extranjeros_por_pais(registros)
#     return max(d_total, key = d_total.get)