import math
import sys
from pprint import pp

def triangulo(num: int, valores):

    num_elemntos = (num*(num + 1))/2
    num_combinaciones = math.factorial(num_elemntos)
    matriz_trin = []
    matriz_trin.append(valores)
    for i in range(num-1):
        matriz_trin.append([])
        for j in range(len(matriz_trin[i])-1):
            n = abs(matriz_trin[i][j]-matriz_trin[i][j+1])
            for w in matriz_trin:
                if n in w:
                    raise Exception("combinacion no valida")
            # print(matriz_trin)
            matriz_trin[i+1].append(n)
    return matriz_trin


def obtener_variaciones_sin_repeticion(set, k, result):

    n = len(set)
    obtener_variaciones_sin_repeticion_rec(set, [], n, k, result)


def obtener_variaciones_sin_repeticion_rec(set, prefix, n, k, result):

    # En caso de que tengamos una variacion (subconjunto) validos
    # de k elementos distintos.
    if (k == 0):
        result.append(prefix)
        return

    # One by one add all characters
    # from set and recursively
    # call for k equals to k-1
    for i in range(n):

        # Comprobamos si no existe el elemento en el subconjunto
        # en caso que exista saltamos a la siguiente iteración
        if set[i] in prefix:
            continue
        # Añadimos el elemento al subconjunto
        lista = [set[i]]
        newPrefix = prefix + lista

        # De decrementamos k en la llamada recursiva ya que
        # tenemos un nuevo elemento añadido al subconjunto
        obtener_variaciones_sin_repeticion_rec(set, newPrefix, n, k - 1,result)




def resultado(matriz):
# imprimimos los resultados.
    for lista in matriz:
        #pp(lista)
        try:
            resultado = triangulo(len(lista),lista)
            pp(resultado)
        except Exception:
            pass



def main(argv):
    try:
        if len(argv) < 2:
            num = int(input("Introduzca el número n de T sub n"
                            +"\n(el numero de bolas por lado): "))
        else:

            num = int(argv[1])
    except Exception:
        print("Error introduzca un numero como parametro")
        return

    # ecuación numero triangular para sacar el numero de elementos (bolas)
    # que tendra nuestro triangulo a partir del numero de bolas por lado.
    # ref: https://es.wikipedia.org/wiki/N%C3%BAmero_triangular
    num_elemntos = int((num*(num + 1))/2)

    num_variaciones = int(math.factorial(num_elemntos)/math.factorial(num_elemntos - num))
    if num > 5:
        print(f"CUIDADO: el número introducido {num} "
              + f"genera {num_variaciones} variaciones (subconjuntos) posibles.\n"
              + "Todo numero introducido mayor de 5 va a tardar"
              + " un buen rato, en función del valor y tu máquina, más vale que"
              + " tengas una buena máquina")
        if input("¿Deseas continuar? (y/n): ") != "y":
            print("adios")
            return
    print("Calculando.....(Ctrl+c para matar el proceso)")


    # inicializamos nuestra matriz que contendra los resultados
    result= []

    # obtenemos una lista de los todos los números de elementos (bolas)
    lista_elementos = list(range(1,num_elemntos+1))

    obtener_variaciones_sin_repeticion(lista_elementos, num, result)

    pp("=============Resultados Validos========")
    resultado(result)

# punto de entrada
if __name__ == "__main__":
    main(sys.argv)
