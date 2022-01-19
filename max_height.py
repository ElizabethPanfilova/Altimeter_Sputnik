# имрорт библиотек
import matplotlib.pyplot as plt
import numpy as np

# путь до файла 
path = 'test_height.txt'

# чтение текстового файла 
with open(path, 'r') as fil:
    mass = fil.readlines()
    data = list(map(lambda i: [float(b) for b in i.split('\t')], mass))
    
# формирование массивов времени и высоты 
mass_time = np.array([i[0] for i in data])
mass_height = np.array([i[1] for i in data])
# определение максимальной высоты 
max_height = max(mass_height)

# отрисовка графика 
plt.plot(mass_time,mass_height)
plt.grid()
plt.title(f'Height graph, maximum height: {max_height}m')
plt.xlabel('Time')
plt.ylabel('Height')
plt.show()