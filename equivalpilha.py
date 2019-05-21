import sys
import string
import random
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
        self.pf = "pf"
        self.p0 = "p0"
        self.x0 = "x"

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
            self.transitions.append('{} {} {} {} {}'.format(self.pf,self.epsilon,i,self.pf,self.epsilon).split())
        
        #para todos estados finais gerar transicoes  E,any /E para o estado final novo
        for i in self.final_states:
            if i != self.pf:
                for j in t:
                    self.transitions.append('{} {} {} {} {}'.format(i,self.epsilon,j,self.pf,self.epsilon).split())
        
        #escrever isso em um novo arquivo
        self.escreveArq()


    def estadoaceitacao(self):        
        #para todos estados gerar transicoes E, X0 /E para o estado final novo
        for i in self.states: 
            if ((i != self.initial_state) and (i!= self.pf)):
                self.transitions.append('{} {} {} {} {}'.format(i,self.epsilon,self.z_inicial_pilha,self.pf,self.epsilon).split())
        
        #definir estado final novo como estado de aceitacao
        self.final_states.append(self.pf)
        
        #escrever isso em um novo arquivo
        self.escreveArq()

    def Equivalencia(self):
        #descobrir primeiro estado do automatoA
        x = self.initial_state
        
        #gerando varias combinacoes de possiveis nomes de estados
        alfab = list(string.ascii_lowercase)
        st =list()
        for i in alfab:
            for j in range(0,100):
                st.append('{}{}'.format(i,j))
        st.append(self.pf)
        
        #criar estado inicial novo
        pp = True
        p_ini = self.p0
        while(pp == True):
            if(self.p0 in self.states):
                pp =True
                self.p0 = random.choice(st)
            elif(self.p0 not in self.states):
                pp = False
                st.pop(st.index(self.p0))
        
        if p_ini != self.p0:
            print('P0 {} ja existia'.format(p_ini))
        print('P0 definido como => {}'.format(self.p0))
        self.states.append(self.p0)
        self.initial_state = self.p0
        
        #criar estado final novo
        pp = True
        fp = self.pf
        while(pp == True):
            if(self.pf in self.states):
                pp =True
                self.pf = random.choice(st)
            elif(self.pf not in self.states):
                pp = False
                st.pop(st.index(self.pf))
 
        if fp != self.pf:
            print('PF {} ja existia'.format(fp))
        print('PF definido como => {}'.format(self.pf))
        self.states.append(self.pf)
        
        #reconhecer todas letras que podem estar no topo da pilha
        t = list()
        for i in self.stack_alphabet:
            for j in i:
                if(j not in t):
                    t.append(j)  

        #definir X0
        pp = True
        xx = self.x0
        while(pp == True):
            if(self.x0 in t):
                pp =True
                self.x0 = random.choice(alfab)
            elif(self.x0 not in t):
                pp = False
                alfab.pop(alfab.index(self.x0))
        
        if xx != self.x0:
            print('X0 {} ja existia'.format(xx))
        print('X0 definido como => {}'.format(self.x0))
        
        #adicionar X0 como parte do alfabeto da pilha e como z_inicial
        zz = self.z_inicial_pilha
        self.z_inicial_pilha = self.x0
        self.stack_alphabet.append(self.x0)  
        
        #empilhar X0 e Z0
        self.transitions.append('{} {} {} {} {}{}'.format(self.initial_state,self.epsilon,self.z_inicial_pilha,x,zz,self.z_inicial_pilha).split()) 

        if(sys.argv[2]=="-p"):
            #transforma para aceitar por pilha vazia
            self.pilhavazia()
            print("Arquivo convertido com sucesso, agora aceita por pilha vazia")
        else:
            #transforma para aceitar por estado de aceitacao
            self.estadoaceitacao()
            print("Arquivo convertido com sucesso, agora aceita por estado de aceitação")
        exit()

if __name__ == "__main__":
    if(sys.argv[2] == "-p" or sys.argv[2] == "-e"):
        p = Convert()
        p.abreArq()
        p.Equivalencia()
    print("Usagem incorreta, utilize \"-p\" para transformar para pilha vazia, ou \"-e\" para transformar para estado de aceitação")
    exit()
    