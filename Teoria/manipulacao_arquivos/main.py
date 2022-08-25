#Programa que escreve em um arquivo
try:
    file = open("data/dados.txt", "a")
    continuar = True

    while continuar:
        time = input('Time (Vazio para sair): ')
        #Entra no if se a str for vazia
        if not time:
            continuar = False
            continue
        file.write(time+'\n')
    file.close()
except FileNotFoundError:
    print('Arquivo ou diretório não encontrado')
except:
    print('Algo de errado aconteceu!')
finally:
    print('Enfim terminou')