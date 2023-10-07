import numpy as np

temperaturaMedia = [36.6, 40.1, 36.8, 32.5, 31.0, 28.6, 32.9]
temperatura = np.array(temperaturaMedia)

media = temperatura.mean()
maxima = temperatura.max()
minima = temperatura.min()
print('''
      Média {:.1f}
      Máxima {}
      Minima {}'''.format(media, maxima, minima))