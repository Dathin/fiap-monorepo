from tempo import tempo_em_ms, aguardar_um_segundo
from random import randrange
from info import informar_sobre_algoritmo, informar_inicio_da_fila, informar_resultado_da_fila
from constantes import UM_MINUTO_EM_MS
from moradores import popula_moradores, tamanho_da_fila_de_moradores, todos_moradores_alimentados, alimentar_moradores, ultima_entrada_em_fila, adiciona_morador

novo_morador_na_fila_em_ms =  UM_MINUTO_EM_MS * 2

nova_distribuicao_em_ms = ((55 % 3) + 1) * UM_MINUTO_EM_MS 

estacoes_de_distribuicao = 1

moradores_servidos_por_distribuicao = estacoes_de_distribuicao * 3

hora_inicial = tempo_em_ms()

hora_chegada_van = hora_inicial + UM_MINUTO_EM_MS * 10

quantidade_moradores_iniciando_na_fila = randrange(1, 16)

informar_sobre_algoritmo(novo_morador_na_fila_em_ms, nova_distribuicao_em_ms, estacoes_de_distribuicao)

popula_moradores(quantidade_moradores_iniciando_na_fila, hora_inicial)

informar_inicio_da_fila()

distribuicao_iniciada = False

ultima_distribuicao = None

while not todos_moradores_alimentados():
    tempo_atual_em_ms = tempo_em_ms()
    if not distribuicao_iniciada and tempo_atual_em_ms > hora_chegada_van: #van deve iniciar preparacao
        print('São 20:10 a van chegou, papeis foram destribuídos e começamos a preparar a distribuição')
        distribuicao_iniciada = True
        ultima_distribuicao = tempo_atual_em_ms
    
    if ultima_entrada_em_fila() + novo_morador_na_fila_em_ms < tempo_atual_em_ms: #novo morador deve entrar na fila
        adiciona_morador(tempo_atual_em_ms)

    if ultima_distribuicao and ultima_distribuicao + nova_distribuicao_em_ms < tempo_atual_em_ms: #distribuição disponível
        alimentar_moradores(tempo_atual_em_ms, moradores_servidos_por_distribuicao)
        ultima_distribuicao = tempo_atual_em_ms

    aguardar_um_segundo()

informar_resultado_da_fila()