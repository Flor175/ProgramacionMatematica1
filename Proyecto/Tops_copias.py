
import json
import pandas as pd
import numpy as np
import os 

current = os.getcwd()

def get_variables(sabana,variables):
    salida = []
    for i in range(len(sabana)):
        fila={}
        for j in variables:
            fila[str(j)] = sabana[i][str(j)]
        salida.append(fila)
    return(salida)


def get_elegidos(sabana,indices):
    salida = []
    for i in indices:
        salida.append(sabana[i])
    return(salida)

def topmes(año):

    if año == 2016:
        with open(current + '\\concurso_2016_copia.json') as f:
            data = json.load(f)
    if año == 2017:
        with open(current + '\\concurso_2017_copia.json') as f:
            data = json.load(f)
    if año == 2018:
        with open(current + '\\concurso_2018_copia.json') as f:
            data = json.load(f)

    variables_elegidas = ['ENTIDAD COMPRADORA','MONTO','MES DE PUBLICACIÓN','NOMBRE']
    data_columnas = get_variables(data,variables_elegidas)

    data_columnas_pd = pd.DataFrame(data_columnas)
    data_columnas_pd['MONTO']=pd.to_numeric(data_columnas_pd['MONTO'])

    maximos_mes = data_columnas_pd.groupby(['MES DE PUBLICACIÓN'])['MONTO'].max()

    pivote_maximos_mes = []
    for mes in maximos_mes.index:
        valor=maximos_mes[mes]
        #print(str(mes))
        for i in range(len(data_columnas)):
            if data_columnas[i]['MES DE PUBLICACIÓN'] == mes:
                #print(float(data_columnas[i]['MONTO']),valor)
                #print(data_columnas[i]['MONTO'],i)
                if data_columnas[i]['MONTO'] == '':
                    pass
                elif float(data_columnas[i]['MONTO']) == valor:
                    pivote_maximos_mes.append(i)

    maximos_topmes = get_elegidos(data_columnas,pivote_maximos_mes)
    topmes_lista =[]
    for i in range(len(maximos_topmes)):
        topmes_lista.append([maximos_topmes[i]['MES DE PUBLICACIÓN'],maximos_topmes[i]['NOMBRE'],maximos_topmes[i]['ENTIDAD COMPRADORA'],maximos_topmes[i]['MONTO']])
    return topmes_lista

def top10(año):

    if año == 2016:
        with open(current + '\\concurso_2016_copia.json') as f:
            print("Usando copia 2016")
            data = json.load(f)
            print(data[len(data)-1])  
    if año == 2017:
        with open(current + '\\concurso_2017_copia.json') as f:
            data = json.load(f)
    if año == 2018:
        with open(current + '\\concurso_2018_copia.json') as f:
            data = json.load(f)

    data_MONTO = get_variables(data,['MONTO'])

    data_MONTO_np=[]
    for i in range(len(data_MONTO)):
        data_MONTO_np.append( pd.to_numeric(data_MONTO[i]['MONTO']))
    data_MONTO_np = np.array(data_MONTO_np)
    data_MONTO_np_sorted = np.sort(data_MONTO_np)

    variables_elegidas = ['ENTIDAD COMPRADORA','MONTO']

    data_columnas = get_variables(data,variables_elegidas)
    elegidos_top10 = np.where(data_MONTO_np >= data_MONTO_np_sorted[np.logical_not(np.isnan(data_MONTO_np_sorted))][-10])[0].astype(int)
    maximos_top10 = get_elegidos(data_columnas,elegidos_top10)
    top10_lista =[]
    for i in range(len(maximos_top10)):
        top10_lista.append([maximos_top10[i]['ENTIDAD COMPRADORA'],maximos_top10[i]['MONTO']])
    return top10_lista

def top10_USAC(año):

    if año == 2016:
        with open(current + '\\concurso_2016_copia.json') as f:
            data = json.load(f)
    if año == 2017:
        with open(current + '\\concurso_2017_copia.json') as f:
            data = json.load(f)
    if año == 2018:
        with open(current + '\\concurso_2018_copia.json') as f:
            data = json.load(f)

    variables_elegidas = ['ENTIDAD COMPRADORA','MONTO']
    data_columnas = get_variables(data,variables_elegidas)

    elegidos_USAC = []
    for i in range(len(data_columnas)):
        if 'USAC' in data_columnas[i]['ENTIDAD COMPRADORA']:
            elegidos_USAC.append(i)

    data_USAC = get_elegidos(data_columnas,elegidos_USAC)

    data_MONTO = get_variables(data_USAC,['MONTO'])
    data_MONTO_np=[]
    for i in range(len(data_MONTO)):
        data_MONTO_np.append( pd.to_numeric(data_MONTO[i]['MONTO']))
    data_MONTO_np = np.array(data_MONTO_np)
    data_MONTO_np_sorted = np.sort(data_MONTO_np)

    elegidos_top10 = np.where(data_MONTO_np >= data_MONTO_np_sorted[np.logical_not(np.isnan(data_MONTO_np_sorted))][-10])[0].astype(int)
    maximos_top10_USAC = get_elegidos(data_USAC,elegidos_top10)
    top10_USAC_lista =[]
    for i in range(len(maximos_top10_USAC)):
        top10_USAC_lista.append([maximos_top10_USAC[i]['ENTIDAD COMPRADORA'],maximos_top10_USAC[i]['MONTO']])
    return top10_USAC_lista

def top10_prov(año):

    if año == 2016:
        with open(current + '\\concurso_2016_copia.json') as f:
            data = json.load(f)
    if año == 2017:
        with open(current + '\\concurso_2017_copia.json') as f:
            data = json.load(f)
    if año == 2018:
        with open(current + '\\concurso_2018_copia.json') as f:
            data = json.load(f)

    variables_elegidas = ['NOMBRE','MONTO']
    data_columnas = get_variables(data,variables_elegidas)
    data_columnas_pd = pd.DataFrame(data_columnas)
    data_columnas_pd['MONTO']=pd.to_numeric(data_columnas_pd['MONTO'])
    data_columnas_pd = data_columnas_pd.round({'MONTO':2})
    maximos_nombre = data_columnas_pd.groupby(['NOMBRE'])['MONTO'].sum()
    maximos_nombre = maximos_nombre.round(2)
    maximos_nombre = maximos_nombre [ np.logical_not(np.logical_not(maximos_nombre.index))]
    data_MONTO = maximos_nombre.values
    data_MONTO_np = np.array(data_MONTO)
    data_MONTO_np_sorted = np.sort(data_MONTO_np)

    elegidos_top10 = np.where(data_MONTO_np >= data_MONTO_np_sorted[np.logical_not(np.isnan(data_MONTO_np_sorted))][-10])[0].astype(int)
    maximos_nombre_lista = []
    for nombre in maximos_nombre[elegidos_top10].index:
        valor=maximos_nombre[elegidos_top10][nombre]
        #print(str(mes))
        for i in range(len(data_columnas)):
            if nombre in data_columnas[i]['NOMBRE']:
                maximos_nombre_lista.append([nombre,valor])
                break
    return maximos_nombre_lista

