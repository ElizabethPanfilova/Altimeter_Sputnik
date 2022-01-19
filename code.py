import board
import busio
import os
import digitalio
import storage
import microcontroller
from time import sleep, time
import adafruit_sdcard
from adafruit_bme280 import basic as adafruit_bme280

def init_led():
    global led
    led = digitalio.DigitalInOut(board.LED)
    led.direction = digitalio.Direction.OUTPUT

def init_sd():
    try:
        # инициализация шины SPI для работы с модулем sd карты
        SD_CS = board.GP13
        spi = busio.SPI(board.GP10, board.GP11, board.GP12)
        cs = digitalio.DigitalInOut(SD_CS)
        sdcard = adafruit_sdcard.SDCard(spi, cs)
        vfs = storage.VfsFat(sdcard)
        storage.mount(vfs, "/sd")
    except:
        print('no-init-cd-module')


def init_bme280_logger():
    global bme280
    try:
        # инициализация шины i2c для работы с модулем амемометра bme280
        i2c = busio.I2C(board.GP3, board.GP2)  # SCL, SDA
        bme280 = adafruit_bme280.Adafruit_BME280_I2C(i2c, address=0x76)
        bme280.sea_level_pressure = 1013.25
    except:
        print('no-init-bme280')


def main_logger():
    # установка начального времени
    init_time = time()
    try:
        # открытие и запись в файл 
        with open(f"/sd/data-log-{init_time}.txt", "a") as appendfile:
            while True:
                led.value = True
                data = [time() - init_time, round(bme280.altitude, 2)]
                appendfile.write('\t'.join(data))
                led.value = False
    except:
        while True:
            led.value = True
            print('ERROR_WRITE')
            time.sleep(1)
            led.value = False

# запуск функций 
init_led()
init_sd() 
init_bme280_logger()
main_logger()


