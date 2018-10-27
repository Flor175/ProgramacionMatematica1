class Matrix(object):
    _n = 0
    _m = 0
    _elementos = None

    def __init__(self, n, m):
        #Inicia la matriz con valor 0 en cada posición
        self._n = n
        self._m = m
        self._elementos = []
        for i in range(self._n):
            self._elementos.append([])
            for j in range(self._m):
                self._elementos[i].append(0)

    def define_elementos(self, i, j, v):
        #Sobreescribe el valor de una celda
        self._elementos[i][j] = v

    def show_matrix(self):
        #Imprime los valores almacenados en la matriz
        for i in range(self._n):
            for j in range(self._m):
                # Imprime en forma de matriz
                print("| {0} ".format(self.get_value_of_position(i, j)), sep=',', end='')
            print('|\n')

    def get_cols(self):
        #Devuelve el número de columnas en la matriz
        return self._m

    def get_rows(self):
        #Devuelve el número de filas en la matriz
        return self._n

    def get_value_of_position(self, i, j):
        #Devuelve el valor en la fila(i), columna(j) de la matriz 
        return self._elementos[i][j]

    def armar_matriz(self, variable_fila, valores):
        for k in range(len(valores)):
            self.define_elementos(variable_fila,k,valores[k])