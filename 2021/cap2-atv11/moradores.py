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