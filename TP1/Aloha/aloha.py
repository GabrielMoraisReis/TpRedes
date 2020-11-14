import random 
import time
class aloha: 
    def __init__(self,node,slot): 
        #numero de nos na rede
        self.node =   node  
        self.timeslot  = [1 for i in range(node)]
        #slot de tempo definido ex: 51,2 microsegundos  
        self.slot = slot    
        self.total_time = 0   
        self.nodes_done = [] 
        self.messages_delivered = 0   
        self.tempo_primeira_estacao = 0
                

    def message_sending(self):  
        aux_slot_colision = 0
        t_slot  = 0 
        print("nodes:",self.timeslot[:])
        #while(self.messages_delivered <= self.node)
        while(self.messages_delivered <= self.node):
            
            #sorteia um no para enviar mensagem 
            # no tempo t_slot que será multiplicado pelo slot padrão 
        
            for i in range(len(self.timeslot)): 
                if self.timeslot[i] == t_slot:   
                    self.nodes_done.append(i)  
            #print(self.nodes_done[:])
            num_nodes_done  = len(self.nodes_done)
            print("\nTamanho do vetor de nos competindo pelo timeslot {}: {}".format(t_slot,num_nodes_done)) 
            print("\nnos competindo pelo slot:",self.nodes_done) 
            #so entra na colisão se no slot em questão mais de um nó estiverem disputando por esse slotframe
            if num_nodes_done > 1: 
                #colision   
                #self.total_time += self.slot * t_slot
                
                for i in self.nodes_done:  
                        self.timeslot[i] = random.randint(t_slot+1 , self.node+t_slot)          
                
                       
                               
                ## envio da mensagem   
            #só ocorrerá envio da mensagem se apenas 1 no estiver enviando nesse slot
            if num_nodes_done == 1 : 
                
                print("\nnode {} is sending - Time: {}".format(self.nodes_done,self.total_time)) 
                self.messages_delivered += 1 
                for i in range(len(self.timeslot)):  
                    if i == self.nodes_done[0]:
                        self.timeslot.pop(i)  
            
            print("\nnodes restantes:",self.timeslot[:])   
            print("mensagens entregues: ",self.messages_delivered) 
           
            if (self.messages_delivered == 1) : self.tempo_primeira_estacao = self.slot * t_slot 
            #limpa o vetor de nos competindo pelo slot, pq o slot vai mudar e com isso novos nós podem competir por esse novo slot
            self.nodes_done.clear()
            t_slot +=1    
            # se a quantidade de mensagens entregues for igual a quantidade de nos na rede, a simulação foi executada
            if self.messages_delivered == self.node: break   
        print("total de slots",t_slot)
        self.total_time = t_slot * self.slot
    def simulate(self):
        self.message_sending()  

############### main ############### 
n = int(input(""))  
if n == 10: 
    f = open("aloha10.txt", "a")
elif n == 20:  
    f = open("aloha20.txt", "a")
elif n == 100:      
    f = open("aloha100.txt", "a")
  
a = aloha(n,0.0000512)  
a.simulate()  
f.write("=======================NOVA SIMULACAO=======================\n")
f.write("Tempo de entrega da mensagem da primeira estação {}\n".format(a.tempo_primeira_estacao))
f.write("Tempo final: {}\n".format(a.total_time)) 



