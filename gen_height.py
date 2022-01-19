# скрипт для создание тестовых файлов записи альтиметра 
# импорт библиотек
from time import time, sleep
# обознаяение начального времени 
init_time = time()
# формирование файла
with open('test_height.txt', 'a+') as f:
    for i in range(100):
        data = [round(time() - init_time, 3), i]
        f.write('\t'.join([str(a) for a in data])+ '\n')
        sleep(0.05)
