import random
import sys
class Estacao():
    def __init__(self, id):
        self.id = id
        self.p = 0.01
        self.msg = True
        self.tfim = 0
        self.slot = 1

n = int(sys.argv[1])
nos = []
for i in range(n):
    nos.append(Estacao(i))

nos_envio = []
nos_final = []
transmite = 0
slot = 0 #valor de posição do slot atual
count = 0 #numero de estações que tentam transmitir no slot
pos = 0
while(nos != []):
    for j in nos:
        if j.slot == slot:
            nos_envio.append(j) # cria a lista de nós que desejam e podem enviar uma mensagem nesse slot
            if (random.randint(0, 100) == 1): #verificaçã de probabilidade
                count += 1
                pos = j.id #salva a posição da estação que satisfaz a condição de probabilidade
    if count == 1: #somente uma estação que deveria transmitir nesse slot de tempo satisfez a probabilidade
        for y in nos_envio:
            for a in nos:
                if pos == a.id: #atualiza os valores do nó que foi transmitido
                    a.msg = False
                    a.tfim = slot * 0.0000512
                    nos_final.append(a)
                    nos.remove(a)
                if y.id == a.id: #atualiza valores dos outros nós que poderiam transmitir nesse slot mas não satisfizeram a probabilidade
                    a.slot += random.randint(1, n) 
            
    elif(nos_envio != []): #indica que houve colisão ou que nenhuma estação satisfez a probabilidade 
        for x in nos_envio:
            for b in nos: #atualiza o valor das estações que deveriam enviar nesse slot e não conseguiram
                if x.id == b.id:
                    b.slot += random.randint(1, n) #define o novo slot no qual que as estações devem tentar enviar

    nos_envio.clear() 
    slot += 1
    count = 0 
f = open(str(sys.argv[2]), "a")  
f.write("Inicio " + str(nos_final[0].tfim) + "\n")
f.write("Final " + str(nos_final[len(nos_final)-1].tfim) + "\n") 


 

    
