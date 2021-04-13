import time

def tempo_em_ms():
    return int(time.time() * 1000)

def aguardar_um_segundo():
    time.sleep(1)