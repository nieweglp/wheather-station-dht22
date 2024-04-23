from time import sleep
import board
import adafruit_dht
import logging
from random import randint
from wheather import Wheather


def main():
    logger = logging.Logger("dht_main")
    sensor = adafruit_dht.DHT22(board.D4)
    while True:
        try:
            temperature = sensor.temperature
            humidity = sensor.humidity
            wheather = Wheather(temperature, humidity)
            logger.warn(f"Temperature: {temperature} , Humidity: {humidity}")
            sleep(1)
        except RuntimeError as e:
            logger.error(e)


if __name__ == "__main__":
    main()
