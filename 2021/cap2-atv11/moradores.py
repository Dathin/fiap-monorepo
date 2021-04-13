from statistics import mean

moradores = []

def popula_moradores(quantidade_moradores_iniciando_na_fila, hora_inicial):
    for item in range(quantidade_moradores_iniciando_na_fila):
        moradores.append({"alimentado": False, "entrada_fila": hora_inicial, "saida_fila": None})

def tamanho_da_fila_de_moradores():
    return len(moradores)

def todos_moradores_alimentados():
    todos_moradores_alimentados = True
    for morador in moradores:
        if not morador['alimentado']:
            todos_moradores_alimentados = False
            break
    return todos_moradores_alimentados

def alimentar_moradores(saida_fila, quantidade):
    quantidade_restante = quantidade
    for morador in moradores:
        if not morador['alimentado'] and quantidade_restante > 0:
            morador['alimentado'] = True
            morador['saida_fila'] = saida_fila
            quantidade_restante -= 1
    print('{} moradores alimentados'.format(abs(quantidade_restante - quantidade)))


def media_permanencia_na_fila():
    media_permanencia_na_fila = []
    for morador in moradores:
        media_permanencia_na_fila.append(morador['saida_fila'] - morador['entrada_fila'])
    return mean(media_permanencia_na_fila)

def ultima_entrada_em_fila():
    return moradores[len(moradores) - 1]['entrada_fila']

def adiciona_morador(tempo_atual_em_ms):
    moradores.append({"alimentado": False, "entrada_fila": tempo_atual_em_ms, "saida_fila": None})
    print('Um morador entrou na fila, totalizando {} moradores'.format(tamanho_da_fila_de_moradores()))

