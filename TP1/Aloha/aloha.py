####################################### imports ############################################################
import random 
import time 
import sys 
####################################### classes ############################################################
class aloha: 
    def __init__(self,node,slot): 
        #numero de nos na rede
        self.node =   node   
        #todos os nos não poderão enviar no primeiro slot (0)
        self.timeslot  = [1 for i in range(node)]
        #slot de tempo definido ex: 51,2 microsegundos  
        self.slot = slot   
        #tempo total   
        self.total_time = 0 
        #vetor de nos que competem por um slot em especifico   
        self.nodes_done = []  
        # quantidade de mensagens entregues
        self.messages_delivered = 0    
        #tempo de entrega de mensagem da primeira  estação
        self.tempo_primeira_estacao = 0
                

    def message_sending(self):
        t_slot  = 0
        print("nos:",self.timeslot[:])
        #while(self.messages_delivered <= self.node)
        while(self.messages_delivered <= self.node):
            
            #sorteia um no para enviar mensagem 
            # no tempo t_slot que será multiplicado pelo slot padrão   

            #verifica quantos nos desejam enviar mensagens nesse slot 
            for i in range(len(self.timeslot)): 
                # se o slot demarcado no vetor for igual ao atual slot, 
                if self.timeslot[i] == t_slot:   
                    #  inclui o numero relacionado a posicao que equivale à estacao 
                    self.nodes_done.append(i)  
           # calcula quantos nos querem enviar nesse slot 
            num_nodes_done  = len(self.nodes_done)
            print("\nTamanho do vetor de nos competindo pelo timeslot {}: {}".format(t_slot,num_nodes_done)) 
            print("\nNos competindo pelo slot:",self.nodes_done) 
            #só entrará na colisão se no slot em questão mais de um nó estiverem disputando o uso desse slot
            if num_nodes_done > 1: 
                #colision   
                
                for i in self.nodes_done:   
                        #sorteia em  slots, maior que o atual, para serem atribuidos aos nós em colisão  
                        self.timeslot[i] = random.randint(t_slot+1 , self.node+t_slot)          
                               
            ## envio da mensagem   
            #só ocorrerá envio da mensagem se apenas 1 no estiver enviando nesse slot
            if num_nodes_done == 1 : 
                
                print("\nnode {} is sending - Time: {}".format(self.nodes_done,self.total_time)) 
                #quanto maior o numero de mensagens mais proximo do fim a simulação estará
                self.messages_delivered += 1    
                # guarda o tempo de entrega da primeira mensagem correspondendo a primeira estação
                if (self.messages_delivered == 1) : self.tempo_primeira_estacao = self.slot * t_slot
                for i in range(len(self.timeslot)):  
                    if i == self.nodes_done[0]:
                        self.timeslot.pop(i)  
            
            print("\nSlot dos nos restantes:",self.timeslot[:])   
            print("Mensagens entregues: ",self.messages_delivered) 
           
             
            #limpa o vetor de nos competindo pelo slot, pq o slot vai mudar e com isso novos nós podem competir por esse novo slot
            self.nodes_done.clear()
            t_slot +=1    
            # se a quantidade de mensagens entregues for igual a quantidade de nos na rede, a simulação foi executada
            if self.messages_delivered == self.node: break   
        self.total_time = t_slot * self.slot
    
    def simulate(self):
        self.message_sending()  

####################################### main #################################################################
n = int(sys.argv[1])
if n == 10: 
    f = open("aloha10.txt", "a")
elif n == 20:  
    f = open("aloha20.txt", "a")
elif n == 100:      
    f = open("aloha100.txt", "a")
  
a = aloha(n,0.0000512)   
f = open(str(sys.argv[2]), "a")
a.simulate()  
f.write("Inicio {}\n".format(a.tempo_primeira_estacao))
f.write("Final  {}\n".format(a.total_time)) 



