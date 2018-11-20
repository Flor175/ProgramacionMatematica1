import json
import pandas as pd
import numpy as np
import urllib.request, json 

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
        with urllib.request.urlopen("https://datos.minfin.gob.gt/dataset/9f0e7cc9-807e-4c4a-ac85-6b8d93bf59b2/resource/1deca1ff-c0e1-4cd6-8f55-a96b29f802db/download/concursos_2016_terminado_adjudicado.json") as url:
            data = json.loads(url.read().decode())
    if año == 2017:
        with urllib.request.urlopen("https://datos.minfin.gob.gt/dataset/9f0e7cc9-807e-4c4a-ac85-6b8d93bf59b2/resource/e63d48a7-fae3-4969-b28e-9df08064fc3f/download/concursos-publicados-2017-finalizados-adjudicados.json") as url:
            data = json.loads(url.read().decode())
    if año == 2018:
        with urllib.request.urlopen("https://datos.minfin.gob.gt/dataset/9f0e7cc9-807e-4c4a-ac85-6b8d93bf59b2/resource/7067b36e-3d0f-49e2-919d-534a66652041/download/concursos-publicados-2018-finalizados-adjudicados.json") as url:
            data = json.loads(url.read().decode())

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
        with urllib.request.urlopen("https://datos.minfin.gob.gt/dataset/9f0e7cc9-807e-4c4a-ac85-6b8d93bf59b2/resource/1deca1ff-c0e1-4cd6-8f55-a96b29f802db/download/concursos_2016_terminado_adjudicado.json") as url:
            data = json.loads(url.read().decode())
    if año == 2017:
        with urllib.request.urlopen("https://datos.minfin.gob.gt/dataset/9f0e7cc9-807e-4c4a-ac85-6b8d93bf59b2/resource/e63d48a7-fae3-4969-b28e-9df08064fc3f/download/concursos-publicados-2017-finalizados-adjudicados.json") as url:
            data = json.loads(url.read().decode())
    if año == 2018:
        with urllib.request.urlopen("https://datos.minfin.gob.gt/dataset/9f0e7cc9-807e-4c4a-ac85-6b8d93bf59b2/resource/7067b36e-3d0f-49e2-919d-534a66652041/download/concursos-publicados-2018-finalizados-adjudicados.json") as url:
            data = json.loads(url.read().decode())

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
        with urllib.request.urlopen("https://datos.minfin.gob.gt/dataset/9f0e7cc9-807e-4c4a-ac85-6b8d93bf59b2/resource/1deca1ff-c0e1-4cd6-8f55-a96b29f802db/download/concursos_2016_terminado_adjudicado.json") as url:
            data = json.loads(url.read().decode())
    if año == 2017:
        with urllib.request.urlopen("https://datos.minfin.gob.gt/dataset/9f0e7cc9-807e-4c4a-ac85-6b8d93bf59b2/resource/e63d48a7-fae3-4969-b28e-9df08064fc3f/download/concursos-publicados-2017-finalizados-adjudicados.json") as url:
            data = json.loads(url.read().decode())
    if año == 2018:
        with urllib.request.urlopen("https://datos.minfin.gob.gt/dataset/9f0e7cc9-807e-4c4a-ac85-6b8d93bf59b2/resource/7067b36e-3d0f-49e2-919d-534a66652041/download/concursos-publicados-2018-finalizados-adjudicados.json") as url:
            data = json.loads(url.read().decode())


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
        with urllib.request.urlopen("https://datos.minfin.gob.gt/dataset/9f0e7cc9-807e-4c4a-ac85-6b8d93bf59b2/resource/1deca1ff-c0e1-4cd6-8f55-a96b29f802db/download/concursos_2016_terminado_adjudicado.json") as url:
            data = json.loads(url.read().decode())
    if año == 2017:
        with urllib.request.urlopen("https://datos.minfin.gob.gt/dataset/9f0e7cc9-807e-4c4a-ac85-6b8d93bf59b2/resource/e63d48a7-fae3-4969-b28e-9df08064fc3f/download/concursos-publicados-2017-finalizados-adjudicados.json") as url:
            data = json.loads(url.read().decode())
    if año == 2018:
        with urllib.request.urlopen("https://datos.minfin.gob.gt/dataset/9f0e7cc9-807e-4c4a-ac85-6b8d93bf59b2/resource/7067b36e-3d0f-49e2-919d-534a66652041/download/concursos-publicados-2018-finalizados-adjudicados.json") as url:
            data = json.loads(url.read().decode())


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
