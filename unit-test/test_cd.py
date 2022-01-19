import os
import board
import busio 
import digitalio
import storage
import adafruit_sdcard
import microcontroller
from time import sleep

SD_CS = board.GP13
 
# инициализация шины для работы с модулем sd карты 
spi = busio.SPI(board.GP10, board.GP11, board.GP12)
cs = digitalio.DigitalInOut(SD_CS)
sdcard = adafruit_sdcard.SDCard(spi, cs)
vfs = storage.VfsFat(sdcard)
storage.mount(vfs, "/sd")

# тест записи 
with open("/sd/testfile.txt", "w") as writefile:
    print("First Line", file=writefile)
    writefile.close()
# тест дозаписи
with open("/sd/testfile.txt", "a") as appendfile:
    print("Second Line", file=appendfile)
    appendfile.close
# тест чтения 
with open("/sd/testfile.txt", "r") as inputfile:
    for line in inputfile:
        print(line)
    inputfile.close
