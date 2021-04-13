import tempo, sortear, time

# Dois minutos em milésimo de segundos para adicionar baseado no laço de repetição
novo_morador_na_fila_em_ms = 120000

# Valor baseado no RM em milésimo de segundos 
nova_distribuicao_em_ms = ((55 % 3) + 1) * 60000 

# Para fins de testar o algoritmo podemos alterar esse valor entre 1 e 2, representando a estação de entrega auxiliar
estacoes_de_distribuicao = 1

# Qunatidade de moradores servidos por entrega
moradores_servidos_por_distribuicao = estacoes_de_distribuicao * 3

# Tempo em que o programa dá início, equivalente as 8 horas no
hora_inicial = tempo.tempo_em_ms()

# Tempo para a van chegar, são dez minutor para deixar a simulação mais real, mas para testar esse valor pode ser reduzido
hora_chegada_van = hora_inicial + 600000

quantidade_moradores_iniciando_na_fila = sortear.sortear_moradores_iniciando_na_fila()

print('Informações do algoritmo: ')
print('Tempo para novo morador entrar na fila: {} minutos'.format(int(novo_morador_na_fila_em_ms / 60000)))
print('Tempo para nova distribuição: {} minutos'.format(int(nova_distribuicao_em_ms/ 60000)))
print('Quantidade de estações de distribuição: {}'.format(estacoes_de_distribuicao))
print('------------------------------')

def todos_moradores_alimentados(fila_de_moradores):
    todos_moradores_alimentados = True
    for morador in fila_de_moradores:
        if not morador['alimentado']:
            todos_moradores_alimentados = False
            break
    return todos_moradores_alimentados

def alimentar_moradores(fila_de_moradores, saida_fila, quantidade):
    quantidade_restante = quantidade
    for morador in fila_de_moradores:
        if not morador['alimentado'] and quantidade_restante > 0:
            morador['alimentado'] = True
            morador['saida_fila'] = saida_fila
            quantidade_restante -= 1
    print('{} moradores alimentados'.format(abs(quantidade_restante - quantidade)))


# Valor inicado como false que será atualizado uma quando a distribuição for iniciada
distribuica_iniciada = False

# Valor iniciado como None para representar que não ocorreu, cada distribuição atualiza esse valor sendo inicada pela chegada da van
ultima_distribuicao = None

#Inicio do fluxo lógico
fila_de_moradores = []
for item in range(quantidade_moradores_iniciando_na_fila):
    fila_de_moradores.append({"alimentado": False, "entrada_fila": hora_inicial, "saida_fila": None})
print('São 20:00h a van chegou')
print('{} moradores já estão esperando na fila'.format(len(fila_de_moradores)))

while not todos_moradores_alimentados(fila_de_moradores):
    tempo_atual_em_ms = tempo.tempo_em_ms()
    if not distribuica_iniciada and tempo_atual_em_ms > hora_chegada_van:
        print('São 20:10 a van chegou, papeis foram destribuídos e começamos a preparar a distribuição')
        distribuica_iniciada = True
        ultima_distribuicao = tempo_atual_em_ms
    
    if fila_de_moradores[len(fila_de_moradores) - 1]['entrada_fila'] + novo_morador_na_fila_em_ms < tempo_atual_em_ms:
        fila_de_moradores.append({"alimentado": False, "entrada_fila": tempo_atual_em_ms, "saida_fila": None})
        print('Um morador entrou na fila, totalizando {} moradores'.format(len(fila_de_moradores)))

    if ultima_distribuicao and ultima_distribuicao + nova_distribuicao_em_ms < tempo_atual_em_ms:
        alimentar_moradores(fila_de_moradores, tempo_atual_em_ms, 3)

    time.sleep(1) # Aguardamos um segundo para evitar loops desnecessários