import math
from pprint import pp

def triangulo(num: int, valores):

    num_elemntos = (num*(num + 1))/2
    num_combinaciones = math.factorial(num_elemntos)
    matriz_trin = []
    print("el numero de elementos es: ", num_elemntos)
    matriz_trin.append(valores)
    for i in range(num-1):
        matriz_trin.append([])
        for j in range(len(matriz_trin[i])-1):
            n = abs(matriz_trin[i][j]-matriz_trin[i][j+1])
            for w in matriz_trin:
                if n in w:
                    return "combinacion no valida"
            # print(matriz_trin)
            matriz_trin[i+1].append(n)
    return matriz_trin

def combi(num: int):
    matriz = []
    num_elementos = int((num*(num + 1))/2)
    j=0
    tam=0
    for i in range(num_elementos):
        for a in range(num_elementos):
            matriz.append([])
            matriz[tam].append(i)
            n=a
            c=0
            while c < num:
                if n not in matriz[tam]:
                    matriz[tam].append(n)
                    c +=1
                n +=1
            tam +=1
    return matriz

def main():
    #elementos = [6,1,4]
    pp(combi(3))

    #print(triangulo(len(elementos), elementos))


if __name__ == "__main__":
    main()
