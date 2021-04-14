# Atividade avaliativa FIAP SI 2
Algoritmo de cálculo de filament

### Versão de programas utilizadas e testadas
- python 3.6.9

### Como rodar
```bash
python princiapl.py
```

### Simulação real e como rodar mais rápido

Todos os cálculos de tempo são feitos com base em um minuto representado em milisegundos. Por padrão valores reais são utilizados,
ou seja, para a van chegar levará 10 minutos por exemplo, para servir os moradores levará e entrarem novos na fila levará 2.
Para agilizar o processo você pode dividir esse valor por bases de 10, com por exemplo:

```python3
# contants.py
UM_MINUTO_EM_MS = 60000 / 10 # 100, 1000...
```