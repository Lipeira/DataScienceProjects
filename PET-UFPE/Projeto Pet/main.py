#Bibliotecas importadas

import matplotlib.pyplot as plt
import numpy

def main():
    
    #Tratamento dos dados - etapa 1

    #abertura dos arquivos
    fifa2006 = open("/content/gdrive/MyDrive/Colab Notebooks/FIFA - 2006.csv","r")
    fifa2010 = open("/content/gdrive/MyDrive/Colab Notebooks/FIFA - 2010.csv","r")
    fifa2014 = open("/content/gdrive/MyDrive/Colab Notebooks/FIFA - 2014.csv","r")
    fifa2018 = open("/content/gdrive/MyDrive/Colab Notebooks//FIFA - 2018.csv","r")

    #definição das listas das variáveis de interesse
    listagoalsfor = []
    listagoalsagainst = []

    with fifa2006,fifa2010,fifa2014,fifa2018:
        
        #Manipulação do arquivo de 2006
        for line in fifa2006:
            if line[0] == "P":
                pass
            else:
                infotemp = line.split(",")
                if infotemp[0] == "15":
                    listagoalsfor.append(int(infotemp[6]))
                    listagoalsagainst.append(int(infotemp[7]))
                    break
                else:
                    listagoalsfor.append(int(infotemp[6]))
                    listagoalsagainst.append(int(infotemp[7]))


        #Manipulação do arquivo de 2010
        for line in fifa2010:
            if line[0] == "P":
                pass
            else:
                infotemp = line.split(",")
                if infotemp[0] == "15":
                    listagoalsfor.append(int(infotemp[6]))
                    listagoalsagainst.append(int(infotemp[7]))
                    break
                else:
                    listagoalsfor.append(int(infotemp[6]))
                    listagoalsagainst.append(int(infotemp[7]))
        

        #Manipulação do arquivo de 2014
        for line in fifa2014:
            if line[0] == "P":
                pass
            else:
                infotemp = line.split(",")
                if infotemp[0] == "15":
                    listagoalsfor.append(int(infotemp[6]))
                    listagoalsagainst.append(int(infotemp[7]))
                    break
                else:
                    listagoalsfor.append(int(infotemp[6]))
                    listagoalsagainst.append(int(infotemp[7]))
        

        #Manipulação do arquivo de 2018
        for line in fifa2018:
            if line[0] == "P":
                pass
            else:
                infotemp = line.split(",")
                if infotemp[0] == "15":
                    listagoalsfor.append(int(infotemp[6]))
                    listagoalsagainst.append(int(infotemp[7]))
                    break
                else:
                    listagoalsfor.append(int(infotemp[6]))
                    listagoalsagainst.append(int(infotemp[7]))


    # Análise estatística - etapa 2

    #Variável 1

    Mgoalsfor = numpy.average(listagoalsfor)
    DPgoalsfor = numpy.std(listagoalsfor)
    LSgoalsfor = 3 * DPgoalsfor + Mgoalsfor
    LIgoalsfor = Mgoalsfor - 3 * DPgoalsfor

    #Variável 2

    Mgoalsagainst = numpy.average(listagoalsagainst)
    DPgoalsagainst = numpy.std(listagoalsagainst)
    LSgoalsagainst = 3 * DPgoalsagainst + Mgoalsagainst
    LIgoalsagainst = Mgoalsagainst - 3 * DPgoalsagainst


    # Plotagem de gráficos - etapa 3

    # Goals For Plotagem
    listaXgoalsfor = []
    listaLSgoalsfor = []
    listaLIgoalsfor = []

    for i in range(1,len(listagoalsfor) + 1):
        listaXgoalsfor.append(i)
        listaLSgoalsfor.append(LSgoalsfor)
        listaLIgoalsfor.append(LIgoalsfor)

    plt.plot(listaXgoalsfor,listagoalsfor,label = "Valores Goals For")
    plt.plot(listaXgoalsfor,listaLSgoalsfor,label = "Limite Superior")
    plt.plot(listaXgoalsfor,listaLIgoalsfor,label = "Limite Inferior")
    plt.title("Goals For")
    plt.xlabel("Quantidade de Times")
    plt.ylabel("Valores Goals For")
    plt.legend()
    plt.show()

    # Goals Against Plotagem

    listaXgoalsagainst = []
    listaLSgoalsagainst = []
    listaLIgoalsagainst = []

    for i in range(1,len(listagoalsagainst) + 1):
        listaXgoalsagainst.append(i)
        listaLSgoalsagainst.append(LSgoalsagainst)
        listaLIgoalsagainst.append(LIgoalsagainst)

    plt.plot(listaXgoalsagainst,listagoalsagainst,label = "Valores Goals Against")
    plt.plot(listaXgoalsagainst,listaLSgoalsagainst,label = "Limite Superior")
    plt.plot(listaXgoalsagainst,listaLIgoalsagainst,label = "Limite Inferior")
    plt.title("Goals Against")
    plt.xlabel("Quantidade de Times")
    plt.ylabel("Valores Goals Against")
    plt.legend()
    plt.show()



if __name__ == "__main__":
    main()