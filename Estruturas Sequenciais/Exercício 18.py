arquivo = float(input('Tamanho do arquivo (MB): '))
velocidade = float(input('Velocidade de Internet (MBps): '))
seg = (arquivo / velocidade)
min = seg/60
print(f'Tempo aproximado de download: {seg:.0f} segundos')
print(f'Tempo aproximado de download: {min:.0f} minutos')