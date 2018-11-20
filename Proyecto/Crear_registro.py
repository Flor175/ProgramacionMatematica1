import pickle
registrados1 = {"ECFM":"ECFM"}

archivo = open("proyecto.pas", "wb+")
pickle.dump(registrados1, archivo)
archivo.close()