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

    ''' criar novo estado inicial que empilha X0'''
    ''' p0, E, X0 / Z0 X0 '''
    '''transitions.append('p0 E X0 Z0 X0')'''

'''def pilhavazia():'''
'''criar estado novo
adicionar loop no novo estado pra esvaziar pilha  E,any /E
para todos estados finais gerar transicoes  E,any /E para o estado novo
escrever isso num novo arquivo'''


'''def estadoaceitacao():'''
'''criar estado novo
para todos estados gerar transicoes E, X0 /E para o estado novo
definir estado novo como estado de aceitacao
escrever isso num novo arquivo'''
