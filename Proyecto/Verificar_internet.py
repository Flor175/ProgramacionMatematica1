import urllib.request, json 
import sys
import os 

current = os.getcwd()

def internet():

    if os.path.isfile(current+'\\concurso_2016_copia.json') :
        pass
    else:
        try:
            with urllib.request.urlopen("https://datos.minfin.gob.gt/dataset/9f0e7cc9-807e-4c4a-ac85-6b8d93bf59b2/resource/1deca1ff-c0e1-4cd6-8f55-a96b29f802db/download/concursos_2016_terminado_adjudicado.json") as url:
                data = json.loads(url.read().decode())
            with open(current+'\\concurso_2016.json', 'w') as outfile:
                json.dump(data, outfile) 
        except:
            pass

    if os.path.isfile(current+'\\concurso_2017_copia.json') :
        pass
    else:
        try:
            with urllib.request.urlopen("https://datos.minfin.gob.gt/dataset/9f0e7cc9-807e-4c4a-ac85-6b8d93bf59b2/resource/e63d48a7-fae3-4969-b28e-9df08064fc3f/download/concursos-publicados-2017-finalizados-adjudicados.json") as url:
                data = json.loads(url.read().decode())
            with open(current+'\\concurso_2017.json', 'w') as outfile:
                json.dump(data, outfile) 
        except:
            pass

    if os.path.isfile(current+'\\concurso_2018_copia.json') :
        pass
    else:
        try:
            with urllib.request.urlopen("https://datos.minfin.gob.gt/dataset/9f0e7cc9-807e-4c4a-ac85-6b8d93bf59b2/resource/7067b36e-3d0f-49e2-919d-534a66652041/download/concursos-publicados-2018-finalizados-adjudicados.json") as url:
                data = json.loads(url.read().decode())
            with open(current+'\\concurso_2018.json', 'w') as outfile:
                json.dump(data, outfile) 
        except:
            pass






