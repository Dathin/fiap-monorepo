from constantes import UM_MINUTO_EM_MS

def informar_sobre_algoritmo(novo_morador_na_fila_em_ms, nova_distribuicao_em_ms, estacoes_de_distribuicao):
    print('Informações do algoritmo: ')
    print('Tempo para novo morador entrar na fila: {} minutos'.format(int(novo_morador_na_fila_em_ms / UM_MINUTO_EM_MS)))
    print('Tempo para nova distribuição: {} minutos'.format(int(nova_distribuicao_em_ms / UM_MINUTO_EM_MS)))
    print('Quantidade de estações de distribuição: {}'.format(estacoes_de_distribuicao))
    print('------------------------------')