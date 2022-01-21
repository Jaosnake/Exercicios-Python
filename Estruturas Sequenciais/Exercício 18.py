arquivo = float(input('Tamanho do arquivo (MB): '))
velocidade = float(input('Velocidade de Internet (MBps): '))
seg = (arquivo / velocidade)
minutos = seg / 60
print(f'Tempo aproximado de download: {seg:.0f} segundos')
print(f'Tempo aproximado de download: {minutos:.0f} minutos')
