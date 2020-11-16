def latencia(nome):
    arq = open( nome ,'r') #abre arquivo na variavel arq
    texto = arq.readlines() #le as linhas do arquivo e enfileira
    media_inicio = 0
    media_fim = 0
    for linha in texto:
        linha = linha.replace("\n","")
        if len(linha)>0:
            spl = linha.split('  ') #.split parte string no caracter
            if (spl[0] == 'Inicio'):
                media_inicio += float(spl[1])
            elif(spl[0] == 'Final'):
                media_fim += float(spl[1])
    print("Media inicio = ", media_inicio/34)
    print("Media fim =", media_fim/34)



sizes = [20, 40, 100]
print("Slotted Aloha")
for size in sizes: 
    
    latencia('aloha' + str(size) + '.txt') 
    



##em x tempo eu envio 1 pacote. 1 pacotes tem 819 bytes.  se eu envio 1 pacote de 819 bytes por tempo, então eu envio 819 x 
#0.01 1 
#1 x