#Programa que escreve em um arquivo

file = open("dados.txt", "a")
continuar = True

while continuar:
    time = input('Time (Vazio para sair): ')
    #Entra no if se a str for vazia
    if not time:
        continuar = False
        continue
    file.write(time+'\n')
file.close()