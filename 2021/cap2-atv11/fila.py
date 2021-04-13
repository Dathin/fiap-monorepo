from tempo import tempo_em_ms, aguardar_um_segundo
from moradores import todos_moradores_alimentados, ultima_entrada_em_fila, adiciona_morador

distribuicao_iniciada = False
ultima_distribuicao = None

def iniciar_fila(hora_chegada_van, nova_distribuicao_em_ms, novo_morador_na_fila_em_ms, moradores_servidos_por_distribuicao):
    while not todos_moradores_alimentados():
        tempo_atual_em_ms = tempo_em_ms()
        if van_deve_iniciar_preparacao(tempo_atual_em_ms, hora_chegada_van):
            iniciar_preparacao(tempo_atual_em_ms)
        
        if novo_morador_entrou_na_fila(tempo_atual_em_ms, novo_morador_na_fila_em_ms):
            adiciona_morador(tempo_atual_em_ms)

        if distribuicao_pronta(tempo_atual_em_ms):
            alimentar_moradores(tempo_atual_em_ms, moradores_servidos_por_distribuicao)
            ultima_distribuicao = tempo_atual_em_ms

        aguardar_um_segundo()

def van_deve_iniciar_preparacao(tempo_atual_em_ms, hora_chegada_van):
    return not distribuicao_iniciada and tempo_atual_em_ms > hora_chegada_van

def iniciar_preparacao(tempo_atual_em_ms):
    print('São 20:10h, a distribuição começa a ser preparada')
    distribuica_iniciada = True
    ultima_distribuicao = tempo_atual_em_ms

def novo_morador_entrou_na_fila(tempo_atual_em_ms, novo_morador_na_fila_em_ms):
    return ultima_entrada_em_fila() + novo_morador_na_fila_em_ms < tempo_atual_em_ms

def distribuicao_pronta(tempo_atual_em_ms):
    return ultima_distribuicao and ultima_distribuicao + nova_distribuicao_em_ms < tempo_atual_em_ms