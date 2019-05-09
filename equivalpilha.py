fp = open(sys.argv[1], "r") #abre em modo de leitura o arquivo com a definicao da maquina de turing
    lines_cmd = fp.readlines()
    lines = []
    for line in lines_cmd:
        lines.append(line.rstrip())
    '''valores de entrada que representam a turing machine de entrada'''
    input_alphabet   = lines[0].split()
    stack_alphabet   = lines[1]
    epsilon          = lines[2]
    z                = lines[3].split()
    states           = lines[4]
    initial_state    = lines[5].split()
    final_states     = lines[6]                     
    transitions      = []


    '''significa que existe estado de aceitacao'''
    #if len(final_states)>0:
        ''' transforma para aceitar por pilha vazia'''
        '''pilhavazia()'''
    #else:
        ''' transforma para aceitar por estado de aceitacao'''
        '''estadoaceitacao()'''

    ''' criar novo estado que empilha X0'''
    ''' p0, E, X0 / Z0 X0 '''
    '''transitions.append()'''

'''def pilhavazia():'''
''' para cada estado de aceitacao criar transicao E,any /E para um estado que esvazia a pilha com loop E,any /E '''

'''def estadoaceitacao():'''
''' para todos estados existentes criar transicoes E, X0 /E para um novo estado de aceitacao '''