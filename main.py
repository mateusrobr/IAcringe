ambiente = [["sujo", "sujo", "limpo"],
            ["limpo", "aspirador", "sujo"],
            ["sujo", "limpo", "sujo"]]


lista_movimentos = []
lista_Percepcao = []
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
    for i in ambiente:
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
    global lista_movimentos
    global lista_Percepcao
    flag_limpou = False
    lista_Percepcao.append("Quadrado Limpo")
    if(matriz[coordenada[0] ][coordenada[1] ] == "sujo"):
        lista_sujos.pop(lista_sujos.index(coordenada))
        flag_limpou = True
        lista_Percepcao.append("Quadrado Sujo")

    posicao_aspirador = get_posicao_aspirador(matriz)
    matriz[coordenada[0] ][coordenada[1] ] = "aspirador"
    print("Posição do aspirador: ", posicao_aspirador)
    print("-" * 40)
    matriz[posicao_aspirador[0][0]][posicao_aspirador[0][1]] = "limpo"
    print("Estado atual do ambiente")
    for i in matriz:
        print(i)
    return flag_limpou



def isSujo(matriz):
    for i  in ambiente:
        for j in i:
            if j == "sujo":
                #print(j)
                #print(linha,coluna)
                return True
    
    return False


lista_sujos = percorrer_e_pegar_sujos(ambiente,1,1)
flag_limpou = False
#print(lista_sujos)
print("Ambiente inicial")
for row in ambiente:
    print(row)
#print(ambiente)
while len(lista_sujos) > 0:
    while get_posicao_aspirador(ambiente)[0][0] != lista_sujos[0][0] or get_posicao_aspirador(ambiente)[0][1] != lista_sujos[0][1]:
        if(flag_limpou):
            print("Limpa o quadrado sujo")
            lista_movimentos.append("Limpou quadrado sujo")
            flag_limpou = False
        

        if(get_posicao_aspirador(ambiente)[0][0] > lista_sujos[0][0]):

            flag_limpou = trocar_Posicao(ambiente, [get_posicao_aspirador(ambiente)[0][0] - 1, get_posicao_aspirador(ambiente)[0][1]],lista_sujos)
            print("Move-se para cima")
            lista_movimentos.append("Move-se para cima")
        elif get_posicao_aspirador(ambiente)[0][0] < lista_sujos[0][0]:

            flag_limpou = trocar_Posicao(ambiente, [get_posicao_aspirador(ambiente)[0][0] + 1 , get_posicao_aspirador(ambiente)[0][1]], lista_sujos)
            print("Move-se para baixo") 
            lista_movimentos.append("Move-se para baixo")
        elif(get_posicao_aspirador(ambiente)[0][1] > lista_sujos[0][1]):
            flag_limpou = trocar_Posicao(ambiente,[get_posicao_aspirador(ambiente)[0][0], get_posicao_aspirador(ambiente)[0][1] - 1], lista_sujos)
            print("Move-se para esquerda")
            lista_movimentos.append("Move-se para esquerda") 
        elif get_posicao_aspirador(ambiente)[0][1] < lista_sujos[0][1]:
            flag_limpou = trocar_Posicao(ambiente,[get_posicao_aspirador(ambiente)[0][0], get_posicao_aspirador(ambiente)[0][1] + 1], lista_sujos)
            print("Move-se para direita") 
            lista_movimentos.append("Move-se para direita")
        
        if(len(lista_sujos) < 1):
            if(flag_limpou):
                print("Limpa o quadrado sujo")
                lista_movimentos.append("Limpou quadrado sujo")
                flag_limpou = False
            i = 0
            while i < 3:
                print("-" * 40)
                for row in ambiente:
                    print(row)
                print("Nao fez Nada") 
                lista_movimentos.append("Nao fez Nada")
                lista_Percepcao.append("Quadrados limpos")
                i += 1

            print("Posição do aspirador: ", get_posicao_aspirador(ambiente))
            break
    #print(ambiente)
    


print("\n{:^15} | {:^15} | {:^15}".format("Sequência", "Percepção", "Ação"))
print("-"*60)

for i in range(len(lista_movimentos)):

    
    print("{:^15} | {:^15} | {:^15}".format(i + 1, lista_Percepcao[i], lista_movimentos[i]))
    