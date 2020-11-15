import random
import sys
class Estacao():
    def __init__(self, id):
        self.id = id
        self.p = 0.01
        self.msg = True
        self.tfim = 0
        self.colisoes = 0
        self.slot = 1

n = int(sys.argv[1]) #numero de estações é passado como argumento na execução
nos = []
for i in range(n):
    nos.append(Estacao(i))

nos_envio = []
nos_final = []
nos_nao_enviados = []
slot = 0 #valor de posição do slot atual
count = 0 #numero de estações que tentam transmitir no slot
pos = 0
while(nos != []):
    for j in nos:
        if j.slot == slot:
            nos_envio.append(j) # cria a lista de nós que desejam enviar uma mensagem nesse slot
            count += 1
            pos = j.id #salva a posição da ultima estação que quer enviar
    if count == 1: #somente uma estação deveria transmitir nesse slot de tempo 
        for y in nos_envio:
            for a in nos:
                if pos == a.id: #atualiza os valores do nó que foi transmitido
                    a.msg = False
                    a.tfim = slot * 0.0000512
                    nos_final.append(a)
                    nos.remove(a)
            
    elif(nos_envio != []): #indica que houve colisão
        for x in nos_envio:
            for b in nos: #atualiza o valor das estações que colidiram
                if x.id == b.id: #define o novo slot no qual que as estações devem tentar enviar
                    b.colisoes += 1
                    b.slot += random.randint(1, ((2**b.colisoes) - 1 ))
                if b.colisoes > 16: #atingiu o limite de tentativas e não tentará enviar novamente
                    nos_nao_enviados.append(b)
                    nos.remove(b)
    nos_envio.clear() 
    slot += 1
    count = 0 
f = open(str(sys.argv[2]), "a")
f.write("Inicio " + str(nos_final[0].tfim) + "\n")
f.write("Final " + str(nos_final[len(nos_final)-1].tfim) + "\n") 

 

    
