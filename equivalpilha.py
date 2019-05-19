import sys
class Convert:
    def __init__(self):
        self.input_alphabet = list()
        self.stack_alphabet =  list()
        self.epsilon=  list()
        self.z_inicial_pilha=  list()
        self.states =  list()
        self.initial_state =  list()
        self.final_states =  list()
        self.transitions =  list()

    def abreArq(self):    
        #abre em modo de leitura o arquivo com a definicao do automato de pilha
        fp = open(sys.argv[1], "r") 
        lines_cmd = fp.readlines()
        lines = []
        for line in lines_cmd:
            lines.append(line.rstrip())
        number_of_lines  = len(lines)
        
        self.input_alphabet   = lines[0].split()
        self.stack_alphabet   = lines[1].split()
        self.epsilon          = lines[2]
        self.z_inicial_pilha  = lines[3]
        self.states           = lines[4].split()
        self.initial_state    = lines[5]
        self.final_states     = lines[6].split()                     
        self.transitions      = []
        self.addTrans(number_of_lines,lines)


    def addTrans(self,qntlinhas,lines):
        for i in range(7, qntlinhas):
            self.transitions.append(lines[i].split())

    
    def escreveArq(self):
        arq = open('Out.txt','w+')
        for i in self.input_alphabet:
            arq.write(i)
            arq.write(' ')
        arq.write('\n')
        for i in self.stack_alphabet:
            arq.write(i)
            arq.write(' ')
        arq.write('\n')
        arq.write(self.epsilon)
        arq.write('\n')
        arq.write(self.z_inicial_pilha) 
        arq.write('\n')
        for i in self.states:
            arq.write(i)
            arq.write(' ') 
        arq.write('\n')
        arq.write(self.initial_state) 
        arq.write('\n')
        for i in self.final_states:
            arq.write(i)
            arq.write(' ')    
        arq.write('\n')
        for i in self.transitions:
            for j in i:
                arq.write(j)
                arq.write(' ')
            arq.write('\n')
        arq.close()    

    def pilhavazia(self):        
        #adicionar loop no novo estado final pra esvaziar pilha  E,any /E 
        self.transitions.append('pf {} any pf {}'.format(self.epsilon,self.epsilon).split())
        #para todos estados finais gerar transicoes  E,any /E para o estado final novo
        for i in self.final_states:
            self.transitions.append('{} {} any pf {}'.format(i,self.epsilon,self.epsilon).split())
        #escrever isso em um novo arquivo
        self.escreveArq()


    def estadoaceitacao(self):        
        #para todos estados gerar transicoes E, X0 /E para o estado final novo
        for i in self.states: 
            self.transitions.append('{} {} {} pf {}'.format(i,self.epsilon,self.z_inicial_pilha,self.epsilon).split())
        #definir estado final novo como estado de aceitacao
        self.final_states.append('pf')
        #escrever isso em um novo arquivo
        self.escreveArq()

    def Equivalencia(self):
    
        #criar estado inicial novo
        self.states.append('p0')
        self.initial_state = 'p0'
        #criar estado final novo
        self.states.append('pf')
        #definir novo zinicial como X0       
        zz = self.z_inicial_pilha
        self.z_inicial_pilha = 'X0'
        #descobrir primeiro estado do automatoA
        x = self.states[0]
        #empilhar X0 e Z0
        self.transitions.append('{} {} {} {} {} {}'.format(self.initial_state,self.epsilon,self.z_inicial_pilha,x,zz,self.z_inicial_pilha).split()) 

        #significa que existe estado de aceitacao
        if len(self.final_states)>0:
            ''' transforma para aceitar por pilha vazia'''
            self.pilhavazia()
        else:
            ''' transforma para aceitar por estado de aceitacao'''
            self.estadoaceitacao()

if __name__ == "__main__":
    p = Convert()
    p.abreArq()
    p.Equivalencia()