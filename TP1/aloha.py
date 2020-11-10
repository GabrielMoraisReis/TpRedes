import random 
import time 
class aloha: 
    def __init__(self,node,slot): 
        #numero de nos na rede
        self.node =   node  
        self.timeslot  = [1 for x in range(self.node)]
        #slot de tempo definido ex: 51,2 microsegundos  
        self.slot = slot    
        self.total_time = 0   
        self.nodes_done = [] 
        self.messages_delivered = 0  
                

    def message_sending(self):  
        
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
            if num_nodes_done > 1: 
                #colision   
                self.total_time += self.slot
                
                for i in self.nodes_done:  
                        self.timeslot[i] = random.randint(t_slot+1 , self.node+t_slot)          
                
                       
                               
                ## envio da mensagem  
            if num_nodes_done == 1 : 
                self.total_time += self.slot 

                print("\nnode {} is sending - Time: {}".format(self.nodes_done,self.total_time))
                self.messages_delivered += 1 
                for i in range(len(self.timeslot)): 
                    if i == self.nodes_done:  
                        self.timeslot.pop(i) 
            print("\nnodes restantes:",self.timeslot[:])   
            print("mensagens entregues: ",self.messages_delivered)
            self.nodes_done.clear()
            t_slot +=1  
            if self.messages_delivered == self.node: break   
                 
    def simulate(self):
        self.message_sending() 
a = aloha(100,0.0000512)  
a.simulate()
print(a.total_time)


