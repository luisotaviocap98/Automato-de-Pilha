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
        #recebendo os dados do txt
        self.input_alphabet   = lines[1].split()
        self.stack_alphabet   = lines[2].split()
        self.epsilon          = lines[3]
        self.z_inicial_pilha  = lines[4]
        self.states           = lines[5].split()
        self.initial_state    = lines[6]
        self.final_states     = lines[7].split()                     
        self.transitions      = []
        self.addTrans(number_of_lines,lines)


    def addTrans(self,qntlinhas,lines):
        #adicionando as transicoes 
        for i in range(8, qntlinhas):
            self.transitions.append(lines[i].split())

    
    def escreveArq(self):
        arq = open('Out.txt','w+')
        #escrevendo o tipo de automato
        arq.write('PDA')
        arq.write('\n')
        #escrevendo o alfabeto de entrada
        for i in self.input_alphabet:
            arq.write(i)
            if (self.input_alphabet.index(i)<(len(self.input_alphabet)-1)):
                arq.write(' ')
        arq.write('\n')
        #escrevendo o alfabeto da pilha
        for i in self.stack_alphabet:
            arq.write(i)
            if (self.stack_alphabet.index(i)<(len(self.stack_alphabet)-1)):
                arq.write(' ')
        arq.write('\n')
        #escrevendo o simbolo epsilon
        arq.write(self.epsilon)
        arq.write('\n')
        #escrevendo o simbolo inicial da pilha
        arq.write(self.z_inicial_pilha) 
        arq.write('\n')
        #escrevendo os estados do automato de pilha
        for i in self.states:
            arq.write(i)
            if (self.states.index(i)<(len(self.states)-1)):
                arq.write(' ')
        arq.write('\n')
        #escrevendo o estado inicial
        arq.write(self.initial_state) 
        arq.write('\n')
        #escrevendo os estados finais
        for i in self.final_states:
            arq.write(i)
            if (self.final_states.index(i)<(len(self.final_states)-1)):
                arq.write(' ')    
        arq.write('\n')
        #escrevendo as transicoes
        for i in self.transitions:
            for j in i:
                arq.write(j)
                if (i.index(j)<(len(i)-1)):
                    arq.write(' ')
            if (self.transitions.index(i)<(len(self.transitions)-1)):
                arq.write('\n')
        arq.close()    

    def pilhavazia(self): 
        #reconhecer todas letras que podem estar no topo da pilha
        t = list()
        for i in self.stack_alphabet:
            for j in i:
                if(j not in t):
                    t.append(j)   
        #adicionar loop no novo estado final pra esvaziar pilha  E,any /E
        for i in t: 
            self.transitions.append('pf {} {} pf {}'.format(self.epsilon,i,self.epsilon).split())
        #para todos estados finais gerar transicoes  E,any /E para o estado final novo
        for i in self.final_states:
            if i != 'pf':
                for j in t:
                    self.transitions.append('{} {} {} pf {}'.format(i,self.epsilon,j,self.epsilon).split())
        #escrever isso em um novo arquivo
        self.escreveArq()


    def estadoaceitacao(self):        
        #para todos estados gerar transicoes E, X0 /E para o estado final novo
        for i in self.states: 
            if ((i != self.initial_state) and (i!= 'pf')):
                self.transitions.append('{} {} {} pf {}'.format(i,self.epsilon,self.z_inicial_pilha,self.epsilon).split())
        #definir estado final novo como estado de aceitacao
        self.final_states.append('pf')
        #escrever isso em um novo arquivo
        self.escreveArq()

    def Equivalencia(self):
        #descobrir primeiro estado do automatoA
        x = self.initial_state
        #criar estado inicial novo
        self.states.append('p0')
        self.initial_state = 'p0'
        #criar estado final novo
        self.states.append('pf')
        #definir novo zinicial como X0       
        zz = self.z_inicial_pilha
        self.z_inicial_pilha = 'X'
        #adicionar X0 como parte do alfabeto da pilha
        self.stack_alphabet.append('X')  
        #empilhar X0 e Z0
        self.transitions.append('{} {} {} {} {}{}'.format(self.initial_state,self.epsilon,self.z_inicial_pilha,x,zz,self.z_inicial_pilha).split()) 

        #significa que existe estado de aceitacao
        if len(self.final_states)>0:
            #transforma para aceitar por pilha vazia
            self.pilhavazia()
        else:
            #transforma para aceitar por estado de aceitacao
            self.estadoaceitacao()

if __name__ == "__main__":
    p = Convert()
    p.abreArq()
    p.Equivalencia()