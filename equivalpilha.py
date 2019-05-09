fp = open(sys.argv[1], "r") #abre em modo de leitura o arquivo com a definicao da maquina de turing
    lines_cmd = fp.readlines()
    lines = []
    for line in lines_cmd:
        lines.append(line.rstrip())
    '''valores de entrada que representam a turing machine de entrada'''
    input_alphabet   = lines[0].split()
    stack_alphabet   = lines[1]
    epsilon          = lines[2]
    z_inicial_pilha  = lines[3].split()
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
'''criar estado inicial novo    states.append('p0')
criar estado final novo    states.append('pf')
adicionar loop no novo estado final pra esvaziar pilha  E,any /E      transitions.append('pf E any E')
para todos estados finais gerar transicoes  E,any /E para o estado novo for i in finalstates transitions.append('i E any E')
escrever isso num novo arquivo'''


'''def estadoaceitacao():'''
'''criar estado inicial novo        states.append('p0')
criar estado final novo    states.append('pf')
para todos estados gerar transicoes E, X0 /E para o estado final novo   for i in states transitions.append('i E X0 E')
definir estado final novo como estado de aceitacao    finalstates.append(pf)
escrever isso num novo arquivo'''
