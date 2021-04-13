import tempo, time, statistics
from info import informar_sobre_algoritmo
from sortear import sortear_moradores_iniciando_na_fila
from constantes import UM_MINUTO_EM_MS
from moradores import popula_moradores, tamanho_da_fila_de_moradores, todos_moradores_alimentados, moradores as fila_de_moradores

novo_morador_na_fila_em_ms =  UM_MINUTO_EM_MS * 2

nova_distribuicao_em_ms = ((55 % 3) + 1) * UM_MINUTO_EM_MS 

estacoes_de_distribuicao = 1

moradores_servidos_por_distribuicao = estacoes_de_distribuicao * 3

hora_inicial = tempo.tempo_em_ms()

hora_chegada_van = hora_inicial + UM_MINUTO_EM_MS * 10

informar_sobre_algoritmo(novo_morador_na_fila_em_ms, nova_distribuicao_em_ms, estacoes_de_distribuicao)

quantidade_moradores_iniciando_na_fila = sortear_moradores_iniciando_na_fila()

distribuica_iniciada = False

ultima_distribuicao = None

# def todos_moradores_alimentados(fila_de_moradores):
#     todos_moradores_alimentados = True
#     for morador in fila_de_moradores:
#         if not morador['alimentado']:
#             todos_moradores_alimentados = False
#             break
#     return todos_moradores_alimentados

def alimentar_moradores(fila_de_moradores, saida_fila, quantidade):
    quantidade_restante = quantidade
    for morador in fila_de_moradores:
        if not morador['alimentado'] and quantidade_restante > 0:
            morador['alimentado'] = True
            morador['saida_fila'] = saida_fila
            quantidade_restante -= 1
    print('{} moradores alimentados'.format(abs(quantidade_restante - quantidade)))

#Inicio do fluxo lógico
# fila_de_moradores = []
# for item in range(quantidade_moradores_iniciando_na_fila):
#     fila_de_moradores.append({"alimentado": False, "entrada_fila": hora_inicial, "saida_fila": None})
popula_moradores(quantidade_moradores_iniciando_na_fila, hora_inicial)
print('São 20:00h, a van chegou')
print('{} moradores já estão esperando na fila'.format(tamanho_da_fila_de_moradores()))

while not todos_moradores_alimentados():
    tempo_atual_em_ms = tempo.tempo_em_ms()
    if not distribuica_iniciada and tempo_atual_em_ms > hora_chegada_van:
        print('São 20:10h, a distribuição começa a ser preparada')
        distribuica_iniciada = True
        ultima_distribuicao = tempo_atual_em_ms
    
    if fila_de_moradores[len(fila_de_moradores) - 1]['entrada_fila'] + novo_morador_na_fila_em_ms < tempo_atual_em_ms:
        fila_de_moradores.append({"alimentado": False, "entrada_fila": tempo_atual_em_ms, "saida_fila": None})
        print('Um morador entrou na fila, totalizando {} moradores'.format(len(fila_de_moradores)))

    if ultima_distribuicao and ultima_distribuicao + nova_distribuicao_em_ms < tempo_atual_em_ms:
        alimentar_moradores(fila_de_moradores, tempo_atual_em_ms, moradores_servidos_por_distribuicao)
        ultima_distribuicao = tempo_atual_em_ms

    time.sleep(1) # Aguardamos um segundo para evitar loops desnecessários

tempo_entrada_saida = []
for morador in fila_de_moradores:
    tempo_entrada_saida.append(morador['saida_fila'] - morador['entrada_fila'])

print('------------------------------')
print('Resultado do algoritmo: ')
print('{} moradores foram alimentados'.format(len(fila_de_moradores)))
print('O tempo médio de espera é de {} s'.format(statistics.mean(tempo_entrada_saida) / 60000))
print('------------------------------')