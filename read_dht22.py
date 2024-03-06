# import libraries

import time
import adafruit_dht
import board


# declare variables

dht_device = adafruit_dht.DHT22(board.D4)

# declare functions

def read_sensor(max_attempts=5):
        for attempt in range(max_attempts):
                try:
                        temperature = dht_device.temperature
                        humidity = dht_device.humidity

                        if humidity is not None and temperature is not None:
                                return temperature, humidity

                        else:
                                raise Exception("Read failed, try again")

                except RuntimeError as error:
                        print(f"{datetime.now()}: {error}")

        raise Exception(f"Sensor failed more than {max_attempts} times.")

while True:
        temperature, humidity = read_sensor()
        print(f"Temperatur: {temperature}°C | Humidity: {humidity}")
        time.sleep(2.0)
