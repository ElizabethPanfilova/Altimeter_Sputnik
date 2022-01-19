import time
import board
import busio
from adafruit_bme280 import basic as adafruit_bme280

# инициализация шины i2c
i2c = busio.I2C(board.GP3, board.GP2)  # SCL, SDA
bme280 = adafruit_bme280.Adafruit_BME280_I2C(i2c, address=0x76)

bme280.sea_level_pressure = 1013.25

# опрос датчика в бесконечном цыкле 
while True:
    print("\nTemperature: %0.1f C" % bme280.temperature)
    print("Humidity: %0.1f %%" % bme280.relative_humidity)
    print("Pressure: %0.1f hPa" % bme280.pressure)
    print("Altitude = %0.2f meters" % bme280.altitude)
    time.sleep(2)