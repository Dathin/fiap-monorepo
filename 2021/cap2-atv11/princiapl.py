import tempo, sortear

# Dois minutos em milésimo de segundos para adicionar baseado no laço de repetição
novo_morador_na_fila_em_ms = 120000

# Valor baseado no RM em milésimo de segundos 
servir_sopa_em_ms = ((55 % 3) + 1) * 60000

# Para fins de testar o algoritmo podemos alterar esse valor entre 1 e 2, representando a estação de entrega auxiliar
estacoes_de_entrega = 1

# Tempo em que o programa dá início, equivalente as 8 horas no
hora_inicial = tempo.tempo_em_ms()

# Tempo para a van chegar, são dez minutor para deixar a simulação mais real, mas para testar esse valor pode ser reduzido
hora_chegada_van = hora_inicial + 100;

quantidade_moradores_iniciando_na_fila = sortear.sortear_moradores_iniciando_na_fila()

fila_de_moradores = []
for item in range(quantidade_moradores_iniciando_na_fila):
    fila_de_moradores.append({"alimentado": False, "fila": hora_inicial})

print('Simulação iniciada')
print('Tempo para novo morador entrar na fila: {} minutos'.format(int(novo_morador_na_fila_em_ms / 60000)))
print('Tempo de servir sopa: {} minutos'.format(int(servir_sopa_em_ms/ 60000)))
print('Quantidade de estações de entrega: {}'.format(estacoes_de_entrega))
print('Quantidade de moradores iniciando na fila: {}'.format(len(fila_de_moradores)))

def todos_moradores_alimentados(fila_de_moradores):
    todos_moradores_alimentados = True
    for morador in fila_de_moradores:
        if not morador['alimentado']:
            todos_moradores_alimentados = False
            break
    return todos_moradores_alimentados

# Valor iniciado como false que será atualizado um vez
van_ja_chegou = False

while not todos_moradores_alimentados(fila_de_moradores):
    if not van_ja_chegou and tempo.tempo_em_ms() > hora_chegada_van:
        print('A van chegou')
        van_ja_chegou = True