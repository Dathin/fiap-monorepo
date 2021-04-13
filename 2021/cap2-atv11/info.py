from constantes import UM_MINUTO_EM_MS
from moradores import tamanho_da_fila_de_moradores, media_permanencia_na_fila

def informar_sobre_algoritmo(novo_morador_na_fila_em_ms, nova_distribuicao_em_ms, estacoes_de_distribuicao):
    print('Informações do algoritmo: ')
    print('Tempo para novo morador entrar na fila: {} minutos'.format(int(novo_morador_na_fila_em_ms / UM_MINUTO_EM_MS)))
    print('Tempo para nova distribuição: {} minutos'.format(int(nova_distribuicao_em_ms / UM_MINUTO_EM_MS)))
    print('Quantidade de estações de distribuição: {}'.format(estacoes_de_distribuicao))
    print('------------------------------')

def informar_inicio_da_fila():
    print('São 20:00h, a van chegou')
    print('{} moradores já estão esperando na fila'.format(tamanho_da_fila_de_moradores()))

def informar_resultado_da_fila():
    print('------------------------------')
    print('Resultado do algoritmo: ')
    print('{} moradores foram alimentados'.format(tamanho_da_fila_de_moradores()))
    print('O tempo médio de espera é de {} s'.format(media_permanencia_na_fila() / UM_MINUTO_EM_MS))
    print('------------------------------')
