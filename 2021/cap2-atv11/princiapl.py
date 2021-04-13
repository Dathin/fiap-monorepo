from tempo import tempo_em_ms
from random import randrange
from info import informar_sobre_algoritmo, informar_inicio_da_fila, informar_resultado_da_fila
from constantes import UM_MINUTO_EM_MS
from moradores import popula_moradores, tamanho_da_fila_de_moradores, todos_moradores_alimentados, alimentar_moradores
from fila import iniciar_fila

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

iniciar_fila(hora_chegada_van, nova_distribuicao_em_ms, novo_morador_na_fila_em_ms, moradores_servidos_por_distribuicao)

informar_resultado_da_fila()