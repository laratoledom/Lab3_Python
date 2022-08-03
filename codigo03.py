#Entrada
Sexo = str(input())
Peso = int(input())
Altura = int(input())

#Leitura dos dados
if Sexo == "F":
    if Altura <= 140:
        print("LX-38")
    elif 140 < Altura <= 155:
        if Peso <= 90:
            print("BW-03")
        else:
            print("CX-101")
    elif 155 < Altura <= 170:
        if Peso <= 70:
            print("BW-03")
        else:
            print("CX-101")
    else:
        if Peso <= 90:
            print("BW-02")
        else:
            print("CX-102")
#Saída
if Sexo == "M":
    if Altura <= 165:
        if Peso <= 70:
            print("LX-39")
        elif 70 < Peso <= 100:
            print("LX-40")
        else:
            print("CX-102")
    elif 165 < Altura <= 190:
        if Peso <= 80:
            print("BW-02")
        elif 80 < Peso <= 100:
            print("MM-107")
        else:
            print("CX-102")
    else:
        if Peso <= 100:
            print("MM-107")
        else:
            print("CX-102")
