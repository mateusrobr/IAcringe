ambiente = [["sujo", "sujo", "limpo"],
            ["limpo", "aspirador", "sujo"],
            ["sujo", "limpo", "sujo"]]



def percorrer_e_pegar_sujos(matriz, startx, starty):
    coluna = 0
    linha = 0
    lista_sujos = []
    for i  in ambiente:
        for j in i:
            if j == "sujo":
                #print(j)
                #print(linha,coluna)
                lista_sujos.append([linha,coluna])
            coluna += 1
            
        linha += 1
        coluna = 0
    
    return lista_sujos

def get_posicao_aspirador(matriz):
    coluna = 0
    linha = 0
    lista_aspirador = []
    for i  in ambiente:
        for j in i:
            if j == "aspirador":
                #print(j)
                #print(linha,coluna)
                lista_aspirador.append([linha,coluna])
            coluna += 1
            
        linha += 1
        coluna = 0
    
    return lista_aspirador
    
def trocar_Posicao(matriz, coordenada ,lista_sujos):
    
    if(matriz[coordenada[0] ][coordenada[1] ] == "sujo"):
        print(lista_sujos)
        print(coordenada)
        lista_sujos.pop(lista_sujos.index(coordenada))

    posicao_aspirador = get_posicao_aspirador(matriz)
    matriz[coordenada[0] ][coordenada[1] ] = "aspirador"

    matriz[posicao_aspirador[0][0]][posicao_aspirador[0][1]] = "limpo"
    for i in matriz:
        print(i)




def isSujo(matriz):
    for i  in ambiente:
        for j in i:
            if j == "sujo":
                #print(j)
                #print(linha,coluna)
                return True
    
    return False

lista_sujos = percorrer_e_pegar_sujos(ambiente,1,1)
print(lista_sujos)

print(ambiente)
while len(lista_sujos) > 0:
    while get_posicao_aspirador(ambiente)[0][0] != lista_sujos[0][0] or get_posicao_aspirador(ambiente)[0][1] != lista_sujos[0][1]:
        if(get_posicao_aspirador(ambiente)[0][0] > lista_sujos[0][0]):

            trocar_Posicao(ambiente, [get_posicao_aspirador(ambiente)[0][0] - 1, get_posicao_aspirador(ambiente)[0][1]],lista_sujos)
            print("A")
        elif get_posicao_aspirador(ambiente)[0][0] < lista_sujos[0][0]:

            trocar_Posicao(ambiente, [get_posicao_aspirador(ambiente)[0][0] + 1 , get_posicao_aspirador(ambiente)[0][1]], lista_sujos)
            print("B")
        elif(get_posicao_aspirador(ambiente)[0][1] > lista_sujos[0][1]):
            trocar_Posicao(ambiente,[get_posicao_aspirador(ambiente)[0][0], get_posicao_aspirador(ambiente)[0][1] - 1], lista_sujos)
            print("C")
        elif get_posicao_aspirador(ambiente)[0][1] < lista_sujos[0][1]:
            trocar_Posicao(ambiente,[get_posicao_aspirador(ambiente)[0][0], get_posicao_aspirador(ambiente)[0][1] + 1], lista_sujos)
            print("D")
        
        if(len(lista_sujos) < 1):
            break
    #print(ambiente)
    
    #lista_sujos.remove(lista_sujos[0])
    if(len(lista_sujos) == 0):
        break

